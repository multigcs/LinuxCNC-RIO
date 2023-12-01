
import argparse
import time
from struct import *
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel,QSlider,QCheckBox
from PyQt5.QtCore import QTimer,QDateTime, Qt

import projectLoader


parser = argparse.ArgumentParser()
parser.add_argument(
    "json", help="json config", type=str, default=None
)
parser.add_argument(
    "--baud", "-b", help="baudrate", type=int, default=1000000
)
parser.add_argument(
    "--port", "-p", help="udp port", type=int, default=2390
)
parser.add_argument(
    "device", help="device like: /dev/ttyUSB0 | 192.168.10.13", nargs="?", type=str, default=None
)
args = parser.parse_args()


project = projectLoader.load(args.json)
print(args.baud)

SHM_FILE = ''
SERIAL = ''
NET_IP = ''
if args.device and args.device.startswith('/dev/tty'):
    import serial
    SERIAL = args.device
    BAUD = args.baud
    ser = serial.Serial(SERIAL, BAUD, timeout=0.001)
elif args.device and args.device.startswith('/dev/shm/'):
    SHM_FILE = args.device
elif args.device and args.device != '':
    NET_IP = args.device
    NET_PORT = args.port
    print('IP:', NET_IP)
    import socket
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
else:
    import spidev
    bus = 0
    device = 1
    spi = spidev.SpiDev()
    spi.open(bus, device)
    spi.max_speed_hz = project['jdata']['interface'][0].get('max', args.baud)
    spi.mode = 0
    spi.lsbfirst = False

INTERVAL = 50

data = [0] * (project['data_size'] // 8)
data[0] = 0x74
data[1] = 0x69
data[2] = 0x72
data[3] = 0x77

JOINTS = project['joints']
VOUTS = project['vouts']
VINS = project['vins']
DOUTS = project['douts']
DINS = project['dins']

VIN_NAMES = project['vinnames']
VOUT_NAMES = project['voutnames']
DIN_NAMES = project['dinnames']
DOUT_NAMES = project['doutnames']
JOINT_TYPES = project['jointtypes']

joints = [0] * project['joints']
vouts = [0] * project['vouts']
douts = [0] * project['douts']

PRU_OSC = int(project['jdata']['clock']['speed'])

vinminmax = []
for num, vin in enumerate(project["vinnames"]):
    if vin.get("type") == "frequency":
        vinminmax.append((vin.get('min', -100), vin.get('max', 100), 'frequency', 0))
    elif vin.get("type") == "pwm":
        vinminmax.append((vin.get('min', -100), vin.get('max', 100), 'pwm', 0))
    elif vin.get("type") == "sonar":
        vinminmax.append((vin.get('min', 0),  vin.get('max', 100000), 'sonar', 0))
    else:
        vinminmax.append((vin.get('min', -100), vin.get('max', 100), '', 0))


vout_types = []
for num, vout in enumerate(project["voutnames"]):
    vout_types.append(vout['type'])


vin_types = []
for num, vin in enumerate(project["vinnames"]):
    vin_types.append(vin['type'])


voutminmax = []
for num, vout in enumerate(project["voutnames"]):
    if vout.get('type') == "vout_sine":
        voutminmax.append((vout.get('min', -100), vout.get('max', 100), 'sine', 30))
    elif vout.get('type') == "pwm":
        freq = vout.get('vout_frequency', 10000)
        if "dir" in vout:
            voutminmax.append((0, vout.get('max', 100), 'pwmdir', freq))
        else:
            voutminmax.append((vout.get('min', 0), vout.get('max', 100), 'pwm', freq))
    elif vout.get('type') == "vout_rcservo":
        freq = vout.get('frequency', 100)
        voutminmax.append((vout.get('min', -100), vout.get('max', 100), 'rcservo', freq))
    elif vout.get('type') == "vout_frequency":
        voutminmax.append((vout.get('min', 0), vout.get('max', 100000), 'frequency', 0))
    elif vout.get('type') == "vout_udpoti":
        voutminmax.append((vout.get('min', 0), vout.get('max', 100), 'udpoti', 0))
    elif vout.get('type') == "vout_spipoti":
        voutminmax.append((vout.get('min', 0), vout.get('max', 255), 'spipoti', 0))
    else:
        voutminmax.append((vout.get('min', 0), vout.get('max', 10), 'scale', 1))

JOINT_ENABLE_BYTES = project['joints_en_total'] // 8
DIGITAL_OUTPUT_BYTES = project['douts_total'] // 8
DIGITAL_INPUT_BYTES = project['dins_total'] // 8






class modbus_vfd():
    FUNCTION_READ       =    0x01
    FUNCTION_WRITE      =    0x02
    WRITE_CONTROL_DATA  =    0x03
    READ_CONTROL_STATUS =    0x04
    WRITE_FREQ_DATA     =    0x05
    LOOP_TEST           =    0x08
    FUNCTION_PD005      =    5
    FUNCTION_PD011      =    11
    FUNCTION_PD144      =    144
    CONTROL_Run_Fwd     =    0x01
    CONTROL_Run_Rev     =    0x11
    CONTROL_Stop        =    0x08
    CONTROL_Run         =    0x01
    CONTROL_Jog         =    0x02
    CONTROL_Command_rf  =    0x04
    CONTROL_Running     =    0x08
    CONTROL_Jogging     =    0x10
    CONTROL_Running_rf  =    0x20
    CONTROL_Bracking    =    0x40
    CONTROL_Track_Start =    0x80

    rpm = 0
    modbus_interval = 1
    modbus_counter = 0
    cmd_counter = 0
    maxFrequency = 0
    minFrequency = 0
    min_rpm = 0
    max_rpm = 0
    maxRpmAt50Hz = 0
    frq_set = 0
    frq_get = 0
    ampere = 0
    srpm = 0
    dc_volt = 0
    ac_volt = 0
    condition = 0
    temp = 0
    addr = 1

    def __init__(self, addr):
        self.spindle_start_fwd        = [0x01, self.WRITE_CONTROL_DATA, 0x01, self.CONTROL_Run_Fwd]
        self.spindle_start_rev        = [0x01, self.WRITE_CONTROL_DATA, 0x01, self.CONTROL_Run_Rev]
        self.spindle_stop             = [0x01, self.WRITE_CONTROL_DATA, 0x01, self.CONTROL_Stop]
        self.spindle_speed            = [0x01, self.WRITE_FREQ_DATA, 0x02, 0x0, 0x0]
        self.spindle_PD005            = [0x01, self.FUNCTION_READ, 0x03, 5, 0x00, 0x00]
        self.spindle_PD011            = [0x01, self.FUNCTION_READ, 0x03, 11, 0x00, 0x00]
        self.spindle_PD144            = [0x01, self.FUNCTION_READ, 0x03, 144, 0x00, 0x00]
        self.spindle_status_frq_set   = [0x01, self.READ_CONTROL_STATUS, 0x03, 0x00, 0x00, 0x00]
        self.spindle_status_frq_get   = [0x01, self.READ_CONTROL_STATUS, 0x03, 0x01, 0x00, 0x00]
        self.spindle_status_ampere    = [0x01, self.READ_CONTROL_STATUS, 0x03, 0x02, 0x00, 0x00]
        self.spindle_status_rpm       = [0x01, self.READ_CONTROL_STATUS, 0x03, 0x03, 0x00, 0x00]
        self.spindle_status_dc_volt   = [0x01, self.READ_CONTROL_STATUS, 0x03, 0x04, 0x00, 0x00]
        self.spindle_status_ac_volt   = [0x01, self.READ_CONTROL_STATUS, 0x03, 0x05, 0x00, 0x00]
        self.spindle_status_condition = [0x01, self.READ_CONTROL_STATUS, 0x03, 0x06, 0x00, 0x00]
        self.spindle_status_temp      = [0x01, self.READ_CONTROL_STATUS, 0x03, 0x07, 0x00, 0x00]
        self.run_cmd = self.spindle_stop
        self.addr = addr

    def crc16(self, data : bytearray, offset, length):
        if data is None or offset < 0 or offset > len(data) - 1 and offset + length > len(data):
            return 0
        crc = 0xFFFF
        for i in range(length):
            crc ^= data[offset + i]
            for j in range(8):
                if ((crc & 0x1) == 1):
                    crc = int((crc / 2)) ^ 40961
                else:
                    crc = int(crc / 2)
        return crc & 0xFFFF

    def set_speed(self, rpm):
        self.rpm = abs(rpm)
        if rpm > 0:
            self.run_cmd = self.spindle_start_fwd
        elif rpm < 0:
            self.run_cmd = self.spindle_start_rev
        else:
            self.run_cmd = self.spindle_stop

    def transmit(self):
        data = [0] * 9
        if self.modbus_counter > self.modbus_interval:
            self.modbus_counter = 0

            cmds = [
                self.spindle_PD005,
                self.spindle_PD011,
                self.spindle_PD144,

                self.spindle_speed,
                self.run_cmd,

                self.spindle_status_ampere,
                self.spindle_status_rpm,
                self.spindle_status_frq_set,
                self.spindle_status_frq_get,

                self.spindle_speed,
                self.run_cmd,

                self.spindle_status_ac_volt,
                self.spindle_status_dc_volt,
                self.spindle_status_condition,
                self.spindle_status_temp,

                self.spindle_speed,
                self.run_cmd,

            ]
            cmd = cmds[self.cmd_counter]
            cmd[0] = self.addr

            if cmd == self.spindle_speed and self.maxRpmAt50Hz > 0:
                value = self.rpm * 5000 // self.maxRpmAt50Hz;
                cmd[3] = (value >> 8) & 0xFF;
                cmd[4] = (value & 0xFF);

            if self.cmd_counter < len(cmds) - 1:
                self.cmd_counter += 1
            else:
                self.cmd_counter = 0

            crc = self.crc16(cmd, 0, len(cmd))
            crcH = crc & 0xFF
            crcL = crc>>8 & 0xFF
            #print("#########", cmd, crcH, crcL, len(cmd) + 2)

            data[0] = len(cmd) + 2
            for n in range(len(cmd)):
                data[n+1] = cmd[n]
                print("### ", data[n+1])
            data[n+2] = crcH
            print("### ", data[n+2])
            data[n+3] = crcL
            print("### ", data[n+3])

        else:
            self.modbus_counter += 1
        return data

    def feedback(self):
        feedback = {
            "rpm": self.rpm,
            "maxFrequency": self.maxFrequency,
            "minFrequency": self.minFrequency,
            "min_rpm": self.min_rpm,
            "max_rpm": self.max_rpm,
            "maxRpmAt50Hz": self.maxRpmAt50Hz,
            "frq_set": self.frq_set,
            "frq_get": self.frq_get,
            "ampere": self.ampere,
            "srpm": self.srpm,
            "dc_volt": self.dc_volt,
            "ac_volt": self.ac_volt,
            "condition": self.condition,
            "temp": self.temp,
            "addr": self.addr,
        }
        return feedback

    def receive(self, data):
        pkglen = data[0]
        if self.addr != data[1]:
            print("WRONG ADDR: ", self.addr, data[1])
            return
        crc = self.crc16(data[1:pkglen-1], 0, pkglen-2)
        crcH = crc & 0xFF
        crcL = crc>>8 & 0xFF
        if data[pkglen-1] != crcH or data[pkglen] != crcL:
            print("CSUM ERROR")
            return

        if data[2] == self.READ_CONTROL_STATUS and data[3] == 0x03:
            value = (data[5] << 8) | data[6]
            print(value)
            if data[4] == 0x00:
                self.frq_set = value
            elif data[4] == 0x01:
                self.frq_get = value
            elif data[4] == 0x02:
                self.ampere = value
            elif data[4] == 0x03:
                self.srpm = value
            elif data[4] == 0x04:
                self.dc_volt = value
            elif data[4] == 0x05:
                self.ac_volt = value
            elif data[4] == 0x06:
                self.condition = value
            elif data[4] == 0x07:
                self.temp = value

        elif data[2] == self.FUNCTION_READ and data[3] == 0x03:
            value = (data[5] << 8) | data[6];
            if data[4] == self.FUNCTION_PD005:
                self.maxFrequency = value
            elif data[4] == self.FUNCTION_PD011:
                self.minFrequency = value
            elif data[4] == self.FUNCTION_PD144:
                self.maxRpmAt50Hz = value
            if self.minFrequency > self.maxFrequency:
                self.minFrequency = self.maxFrequency
            self.min_rpm = self.minFrequency * self.maxRpmAt50Hz / 5000
            self.max_rpm = self.maxFrequency * self.maxRpmAt50Hz / 5000
    

class WinForm(QWidget):

    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('SPI-Test')
        self.listFile=QListWidget()
        layout=QGridLayout()
        self.widgets = {}
        self.animation = 0
        self.doutcounter = 0
        self.error_counter_spi = 0
        self.error_counter_net = 0
        self.time_trx = 0
        self.vfd = {}
        
        # boutnames
        for num, bout in enumerate(project["boutnames"]):
            boutsize = bout['size']
            if bout["type"] == "modbus":
                name = bout["name"]
                for protocol in bout["protocols"]:
                    if protocol["type"] == "hyvfd":
                        addr = protocol["addr"]
                        self.vfd[addr] = modbus_vfd(addr)

        gpy = 0


        self.widgets["connection"] = QLabel(f'CONNECTION:')
        layout.addWidget(self.widgets["connection"], gpy, 0)
        gpy += 1


        layout.addWidget(QLabel(f'JOINTS:'), gpy, 0)
        for jn in range(JOINTS):
            layout.addWidget(QLabel(f'JOINT{jn}'), gpy, jn + 3)
        gpy += 1
        for jn in range(JOINTS):
            layout.addWidget(QLabel(JOINT_TYPES[jn]), gpy, jn + 3)
        gpy += 1
        for jn in range(JOINTS):
            key = f'jcs{jn}'
            self.widgets[key] = QSlider(Qt.Horizontal)
            self.widgets[key].setMinimum(-1000)
            self.widgets[key].setMaximum(1000)
            self.widgets[key].setValue(0)
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1
        layout.addWidget(QLabel(f'SET'), gpy, 1)
        for jn in range(JOINTS):
            key = f'jcraw{jn}'
            self.widgets[key] = QLabel(f'cmd: {jn}')
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1
        layout.addWidget(QLabel(f'OUT'), gpy, 1)
        for jn in range(JOINTS):
            key = f'jc{jn}'
            self.widgets[key] = QLabel(f'cmd: {jn}')
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1
        layout.addWidget(QLabel(f'FB'), gpy, 1)
        for jn in range(JOINTS):
            key = f'jf{jn}'
            self.widgets[key] = QLabel(f'joint: {jn}')
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1
        layout.addWidget(QLabel(''), gpy, 1)
        gpy += 1

        layout.addWidget(QLabel(f'VOUT:'), gpy, 0)
        for vn in range(VOUTS):
            layout.addWidget(QLabel(VOUT_NAMES[vn]['_name']), gpy, vn + 3)
        gpy += 1
        for vn in range(VOUTS):
            layout.addWidget(QLabel(vout_types[vn]), gpy, vn + 3)
        gpy += 1
        for vn in range(VOUTS):
            key = f'vos{vn}'
            self.widgets[key] = QSlider(Qt.Horizontal)
            if voutminmax[vn][2] == "pwmdir":
                self.widgets[key].setMinimum(-int(voutminmax[vn][1]))
            else:
                self.widgets[key].setMinimum(int(voutminmax[vn][0]))
            self.widgets[key].setMaximum(int(voutminmax[vn][1]))
            self.widgets[key].setValue(0)
            layout.addWidget(self.widgets[key], gpy, vn + 3)
        gpy += 1
        layout.addWidget(QLabel(f'SET'), gpy, 1)
        for vn in range(VOUTS):
            key = f'vo{vn}'
            self.widgets[key] = QLabel(f'vo: {vn}')
            layout.addWidget(self.widgets[key], gpy, vn + 3)
        gpy += 1
        layout.addWidget(QLabel(''), gpy, 1)
        gpy += 1

        layout.addWidget(QLabel(f'VIN:'), gpy, 0)
        for vn in range(VINS):
            layout.addWidget(QLabel(VIN_NAMES[vn]['_name']), gpy, vn + 3)
        gpy += 1
        for vn in range(VINS):
            layout.addWidget(QLabel(vin_types[vn]), gpy, vn + 3)
        gpy += 1
        layout.addWidget(QLabel(f'IN'), gpy, 1)
        for vn in range(VINS):
            key = f'vi{vn}'
            self.widgets[key] = QLabel(f'vin: {vn}')
            layout.addWidget(self.widgets[key], gpy, vn + 3)
        gpy += 1
        layout.addWidget(QLabel(''), gpy, 1)
        gpy += 1

        if project['douts']:
            for dbyte in range(DIGITAL_OUTPUT_BYTES):
                if dbyte == 0:
                    layout.addWidget(QLabel(f'DOUT:'), gpy, 0)
                    self.widgets["dout_auto"] = QCheckBox()
                    layout.addWidget(self.widgets["dout_auto"], gpy, 2)
                for dn in range(8):
                    key = f'doc{dbyte}{dn}'
                    self.widgets[key] = QCheckBox(DOUT_NAMES[dbyte * 8 + dn]['_name'])
                    self.widgets[key].setChecked(False)
                    layout.addWidget(self.widgets[key], gpy, dn + 3)
                    if dbyte * 8 + dn == DOUTS - 1:
                        break
                gpy += 1
            layout.addWidget(QLabel(''), gpy, 1)
            gpy += 1


        for dbyte in range(DIGITAL_INPUT_BYTES):
            if dbyte == 0:
                layout.addWidget(QLabel(f'DIN:'), gpy, 0)
            for dn in range(8):
                layout.addWidget(QLabel(DIN_NAMES[dbyte * 8 + dn]['_name']), gpy, dn + 3)
                if dbyte * 8 + dn == DINS - 1:
                    break
            gpy += 1
            for dn in range(8):
                key = f'dic{dbyte}{dn}'
                self.widgets[key] = QLabel("0")
                layout.addWidget(self.widgets[key], gpy, dn + 3)
                if dbyte * 8 + dn == DINS - 1:
                    break
            gpy += 1


        # boutnames
        for num, bout in enumerate(project["boutnames"]):
            boutsize = bout['size']
            if bout["type"] == "modbus":
                name = bout["name"]
                for protocol in bout["protocols"]:
                    if protocol["type"] == "hyvfd":
                        layout.addWidget(QLabel(f'HYVFD:'), gpy, 0)
                        self.widgets[f"{name}-hyvfd"] = QSlider(Qt.Horizontal)
                        self.widgets[f"{name}-hyvfd"].setMinimum(-20000)
                        self.widgets[f"{name}-hyvfd"].setMaximum(20000)
                        self.widgets[f"{name}-hyvfd"].setValue(0)
                        layout.addWidget(self.widgets[f"{name}-hyvfd"], gpy, 3)
                        gpy += 1

                        for vn, vname in enumerate(["rpm","maxFrequency","minFrequency","min_rpm","max_rpm","maxRpmAt50Hz","frq_set","frq_get","ampere","srpm","dc_volt","ac_volt","condition","temp","addr"]):
                            layout.addWidget(QLabel(vname), gpy, 3)
                            self.widgets[f"{name}-hyvfd-{vname}"] = QLabel(vname)
                            layout.addWidget(self.widgets[f"{name}-hyvfd-{vname}"], gpy, 4)
                            gpy += 1


        layout.addWidget(QLabel(''), gpy, 0)
        gpy += 1

        layout.addWidget(QLabel(f'ERRORS:'), gpy, 0)
        layout.addWidget(QLabel(f'SPI:'), gpy, 1)
        self.widgets["errors_spi"] = QLabel("0")
        layout.addWidget(self.widgets["errors_spi"], gpy, 2)

        layout.addWidget(QLabel(f'NET:'), gpy, 3)
        self.widgets["errors_net"] = QLabel("0")
        layout.addWidget(self.widgets["errors_net"], gpy, 4)

        layout.addWidget(QLabel(f'TIME:'), gpy, 5)
        self.widgets["time_trx"] = QLabel("0")
        layout.addWidget(self.widgets["time_trx"], gpy, 6)
        gpy += 1

        self.setLayout(layout)

        self.timer=QTimer()
        self.timer.timeout.connect(self.runTimer)
        self.timer.start(INTERVAL)

    def runTimer(self):
        data[0] = 0x74
        data[1] = 0x69
        data[2] = 0x72
        data[3] = 0x77

        try:
            for jn in range(JOINTS):
                key = f"jcs{jn}"
                joints[jn] = int(self.widgets[key].value())

                key = f"jcraw{jn}"
                self.widgets[key].setText(str(joints[jn]))

            for vn in range(VOUTS):
                key = f"vos{vn}"
                vouts[vn] = int(self.widgets[key].value())
                key = f"vo{vn}"
                self.widgets[key].setText(str(vouts[vn]))

            douts = []
            if project['douts']:
                if self.widgets["dout_auto"].isChecked():
                    for dbyte in range(DIGITAL_OUTPUT_BYTES):
                        for dn in range(8):
                            key = f"doc{dbyte}{dn}"
                            stat = (self.animation - 1) == dbyte * 8 + dn
                            self.widgets[key].setChecked(stat)
                            if dbyte * 8 + dn == DOUTS - 1:
                                break
                    if self.doutcounter > 3:
                        self.doutcounter = 0
                        if self.animation >= DOUTS:
                            self.animation = 0
                        else:
                            self.animation += 1
                    else:
                        self.doutcounter += 1

                for dbyte in range(DIGITAL_OUTPUT_BYTES):
                    douts.append(0)
                    for dn in range(8):
                        key = f"doc{dbyte}{dn}"
                        if self.widgets[key].isChecked():
                            douts[dbyte] |= (1<<(7-dn))
                        if dbyte * 8 + dn == DOUTS - 1:
                            break

            bn = 4
            for jn, value in enumerate(joints):
                # precalc
                if value == 0:
                    value = 0
                else:
                    if JOINT_TYPES[jn] == 'joint_pwmdir':
                        value = value
                    else:
                        value = int(PRU_OSC / value)

                key = f"jc{jn}"
                self.widgets[key].setText(str(value))

                joint = list(pack('<i', value))
                for byte in range(4):
                    data[bn + byte] = joint[byte]
                bn += 4

            for vn, value in enumerate(vouts):
                if voutminmax[vn][2] == 'sine':
                    if value != 0:
                        value = int(PRU_OSC / value / voutminmax[vn][3])
                    else:
                        value = 0
                elif voutminmax[vn][2] == 'pwmdir':
                    value = int((value) * (PRU_OSC / voutminmax[vn][3]) / (voutminmax[vn][1]))
                elif voutminmax[vn][2] == 'pwm':
                    value = int((value - voutminmax[vn][0]) * (PRU_OSC / voutminmax[vn][3]) / (voutminmax[vn][1] - voutminmax[vn][0]))
                elif voutminmax[vn][2] == 'rcservo':
                    value = int(((value + 300)) * (PRU_OSC / 200000))
                elif voutminmax[vn][2] == 'udpoti':
                    value = value
                elif voutminmax[vn][2] == 'spipoti':
                    value = value
                elif voutminmax[vn][2] == 'frequency':
                    if value != 0:
                        value = int(PRU_OSC / value)
                    else:
                        value = 0

                vout = list(pack('<i', (value)))
                for byte in range(4):
                    data[bn + byte] = vout[byte]
                bn += 4

            # boutnames
            for num, bout in enumerate(project["boutnames"]):
                boutsize = bout['size']
                if bout["type"] == "modbus":
                    name = bout["name"]
                    for protocol in bout["protocols"]:
                        if protocol["type"] == "hyvfd":
                            speed = self.widgets[f"{name}-hyvfd"].value()
                            addr = protocol["addr"]
                            self.vfd[addr].set_speed(speed)
                            package = self.vfd[addr].transmit()
                            for boutn in range(boutsize // 8):
                                data[bn] = package[boutn]
                                bn += 1

            # jointEnable and dout (TODO: split in bits)
            for dbyte in range(JOINT_ENABLE_BYTES):
                data[bn] = 0xFF
                bn += 1

            # dout
            if project['douts']:
                for dbyte in range(DIGITAL_OUTPUT_BYTES):
                    data[bn] = douts[dbyte]
                    bn += 1

            print("")
            print("tx:", data)
            start = time.time()
            if NET_IP:
                UDPClientSocket.sendto(bytes(data), (NET_IP, NET_PORT))
                UDPClientSocket.settimeout(0.2)
                msgFromServer = UDPClientSocket.recvfrom(len(data))
                rec = list(msgFromServer[0])
            elif SERIAL:
                ser.write(bytes(data))
                msgFromServer = ser.read(len(data))
                rec = list(msgFromServer)
            elif SHM_FILE:
                fd = open(f"{SHM_FILE}.tx", "wb")
                fd.write(bytes(data))
                fd.close()
                fd = open(f"{SHM_FILE}.rx", "rb")
                msgFromServer = fd.read(len(data))
                fd.close()
                rec = list(msgFromServer)
            else:
                rec = spi.xfer2(data)

            self.time_trx = (time.time() - start)
            print(f"Duration: {self.time_trx * 1000:02.02f}ms")
            print("rx:", rec)

            jointFeedback = [0] * JOINTS
            processVariable = [0] * VINS

            pos = 0
            header = unpack('<i', bytes(rec[pos:pos+4]))[0]
            pos += 4

            for num in range(JOINTS):
                jointFeedback[num] = unpack('<i', bytes(rec[pos:pos+4]))[0]
                pos += 4

            for num in range(VINS):
                processVariable[num] = unpack('<i', bytes(rec[pos:pos+4]))[0]
                pos += 4

            # binnames
            binValues = {}
            for num, bins in enumerate(project["binnames"]):
                binValues[num] = []
                binsize = bins['size']
                for binn in range(binsize // 8):
                    binValues[num].append(unpack('<B', bytes(rec[pos:pos+1]))[0])
                    pos += 1
                if bins["type"] == "modbus":
                    name = bins["name"]
                    for protocol in bins["protocols"]:
                        if protocol["type"] == "hyvfd":
                            addr = protocol["addr"]
                            self.vfd[addr].receive(binValues[num])
                            fbdata = self.vfd[addr].feedback()
                            for vname, vvalue in fbdata.items():
                                if f"{name}-hyvfd-{vname}" in self.widgets:
                                    self.widgets[f"{name}-hyvfd-{vname}"].setText(str(vvalue))


            inputs = []
            for dbyte in range(DIGITAL_INPUT_BYTES):
                inputs.append(unpack('<B', bytes(rec[pos:pos+1]))[0])
                pos += 1

            if header == 0x64617461:
                print(f'PRU_DATA: 0x{header:x}')
                #for num in range(JOINTS):
                #    print(f' Joint({num}): {jointFeedback[num]} // 1')
                #for num in range(VINS):
                #    print(f' Var({num}): {processVariable[num]}')
                #print(f'inputs {inputs:08b}')
                self.widgets["connection"].setText("CONNECTED")
                self.widgets["connection"].setStyleSheet("background-color: green")
            else:
                print(f'ERROR: Unknown Header: 0x{header:x}')
                self.error_counter_spi += 1
                self.widgets["connection"].setText(f'ERROR: 0x{header:x}')
                self.widgets["connection"].setStyleSheet("background-color: red")

            for jn, value in enumerate(joints):
                key = f"jf{jn}"
                self.widgets[key].setText(str(jointFeedback[jn]))

            for vn in range(VINS):
                key = f"vi{vn}"
                unit = ""
                value = processVariable[vn]
                if vinminmax[vn][2] == 'frequency':
                    unit = "Hz"
                    if value != 0:
                        value = PRU_OSC / value
                elif vinminmax[vn][2] == 'pwm':
                    unit = "ms"
                    if value != 0:
                        value = 1000 / (PRU_OSC / value)
                elif vinminmax[vn][2] == 'sonar':
                    unit = "mm"
                    if value != 0:
                        value = 1000 / PRU_OSC / 20 * value * 343.2
                self.widgets[key].setText(f"{round(value, 2)}{unit}")

            for dbyte in range(DIGITAL_INPUT_BYTES):
                for dn in range(8):
                    key = f"dic{dbyte}{dn}"

                    value = "0"
                    if inputs[dbyte] & (1<<(7-dn)) != 0:
                        value = "1"

                    self.widgets[key].setText(value)
                    if value == "0":
                        self.widgets[key].setStyleSheet("background-color: lightgreen")
                    else:
                        self.widgets[key].setStyleSheet("background-color: yellow")

                    if dbyte * 8 + dn == DINS - 1:
                        break

        except Exception as e:
            print("ERROR", e)
            self.error_counter_net += 1
            self.widgets["connection"].setText(f'ERROR: {e}')
            self.widgets["connection"].setStyleSheet("background-color: red")

        self.widgets["errors_spi"].setText(str(self.error_counter_spi))
        self.widgets["errors_net"].setText(str(self.error_counter_net))
        self.widgets["time_trx"].setText(f"{self.time_trx * 1000:02.02f}ms")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



