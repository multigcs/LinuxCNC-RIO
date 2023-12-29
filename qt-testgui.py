import argparse
import sys
import time
from functools import partial
from struct import *
import traceback

from PyQt5 import QtGui
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QGridLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSlider,
    QWidget,
)

import projectLoader

parser = argparse.ArgumentParser()
parser.add_argument("json", help="json config", type=str, default=None)
parser.add_argument("--graph", "-g", help="graph", type=bool, default=False)
parser.add_argument("--baud", "-b", help="baudrate", type=int, default=1000000)
parser.add_argument("--port", "-p", help="udp port", type=int, default=2390)
parser.add_argument("--debug", "-d", help="debug", type=bool, default=False)
parser.add_argument(
    "device",
    help="device like: /dev/ttyUSB0 | 192.168.10.13",
    nargs="?",
    type=str,
    default=None,
)
args = parser.parse_args()


class CH341():

    DEFAULT_TIMEOUT         = 1000     # 1000mS for USB timeouts
    BULK_WRITE_ENDPOINT     = 0x02
    BULK_READ_ENDPOINT      = 0x82

    PACKET_LENGTH     = 0x20
    MAX_PACKETS       = 256
    MAX_PACKET_LEN    = (PACKET_LENGTH * MAX_PACKETS)
    USB_VENDOR       = 0x1A86
    USB_PRODUCT      = 0x5512

    CMD_SET_OUTPUT   = 0xA1
    CMD_IO_ADDR      = 0xA2
    CMD_PRINT_OUT    = 0xA3
    CMD_SPI_STREAM   = 0xA8
    CMD_SIO_STREAM   = 0xA9
    CMD_I2C_STREAM   = 0xAA
    CMD_UIO_STREAM   = 0xAB

    CMD_I2C_STM_STA  = 0x74
    CMD_I2C_STM_STO  = 0x75
    CMD_I2C_STM_OUT  = 0x80
    CMD_I2C_STM_IN   = 0xC0
    CMD_I2C_STM_MAX  = min(0x3F, PACKET_LENGTH)
    CMD_I2C_STM_SET  = 0x60
    CMD_I2C_STM_US   = 0x40
    CMD_I2C_STM_MS   = 0x50
    CMD_I2C_STM_DLY  = 0x0F
    CMD_I2C_STM_END  = 0x00

    CMD_UIO_STM_IN   = 0x00
    CMD_UIO_STM_DIR  = 0x40
    CMD_UIO_STM_OUT  = 0x80
    CMD_UIO_STM_US   = 0xC0
    CMD_UIO_STM_END  = 0x20

    STM_I2C_20K      = 0x00
    STM_I2C_100K     = 0x01
    STM_I2C_400K     = 0x02
    STM_I2C_750K     = 0x03
    STM_SPI_DBL      = 0x04

    reverse_table = [
        0x00, 0x80, 0x40, 0xc0, 0x20, 0xa0, 0x60, 0xe0,
        0x10, 0x90, 0x50, 0xd0, 0x30, 0xb0, 0x70, 0xf0,
        0x08, 0x88, 0x48, 0xc8, 0x28, 0xa8, 0x68, 0xe8,
        0x18, 0x98, 0x58, 0xd8, 0x38, 0xb8, 0x78, 0xf8,
        0x04, 0x84, 0x44, 0xc4, 0x24, 0xa4, 0x64, 0xe4,
        0x14, 0x94, 0x54, 0xd4, 0x34, 0xb4, 0x74, 0xf4,
        0x0c, 0x8c, 0x4c, 0xcc, 0x2c, 0xac, 0x6c, 0xec,
        0x1c, 0x9c, 0x5c, 0xdc, 0x3c, 0xbc, 0x7c, 0xfc,
        0x02, 0x82, 0x42, 0xc2, 0x22, 0xa2, 0x62, 0xe2,
        0x12, 0x92, 0x52, 0xd2, 0x32, 0xb2, 0x72, 0xf2,
        0x0a, 0x8a, 0x4a, 0xca, 0x2a, 0xaa, 0x6a, 0xea,
        0x1a, 0x9a, 0x5a, 0xda, 0x3a, 0xba, 0x7a, 0xfa,
        0x06, 0x86, 0x46, 0xc6, 0x26, 0xa6, 0x66, 0xe6,
        0x16, 0x96, 0x56, 0xd6, 0x36, 0xb6, 0x76, 0xf6,
        0x0e, 0x8e, 0x4e, 0xce, 0x2e, 0xae, 0x6e, 0xee,
        0x1e, 0x9e, 0x5e, 0xde, 0x3e, 0xbe, 0x7e, 0xfe,
        0x01, 0x81, 0x41, 0xc1, 0x21, 0xa1, 0x61, 0xe1,
        0x11, 0x91, 0x51, 0xd1, 0x31, 0xb1, 0x71, 0xf1,
        0x09, 0x89, 0x49, 0xc9, 0x29, 0xa9, 0x69, 0xe9,
        0x19, 0x99, 0x59, 0xd9, 0x39, 0xb9, 0x79, 0xf9,
        0x05, 0x85, 0x45, 0xc5, 0x25, 0xa5, 0x65, 0xe5,
        0x15, 0x95, 0x55, 0xd5, 0x35, 0xb5, 0x75, 0xf5,
        0x0d, 0x8d, 0x4d, 0xcd, 0x2d, 0xad, 0x6d, 0xed,
        0x1d, 0x9d, 0x5d, 0xdd, 0x3d, 0xbd, 0x7d, 0xfd,
        0x03, 0x83, 0x43, 0xc3, 0x23, 0xa3, 0x63, 0xe3,
        0x13, 0x93, 0x53, 0xd3, 0x33, 0xb3, 0x73, 0xf3,
        0x0b, 0x8b, 0x4b, 0xcb, 0x2b, 0xab, 0x6b, 0xeb,
        0x1b, 0x9b, 0x5b, 0xdb, 0x3b, 0xbb, 0x7b, 0xfb,
        0x07, 0x87, 0x47, 0xc7, 0x27, 0xa7, 0x67, 0xe7,
        0x17, 0x97, 0x57, 0xd7, 0x37, 0xb7, 0x77, 0xf7,
        0x0f, 0x8f, 0x4f, 0xcf, 0x2f, 0xaf, 0x6f, 0xef,
        0x1f, 0x9f, 0x5f, 0xdf, 0x3f, 0xbf, 0x7f, 0xff
    ]

    def __init__(self, vid=USB_VENDOR, pid=USB_PRODUCT):
        dev = usb.core.find(idVendor=vid, idProduct=pid)

        if dev is None:
            raise ConnectionError("Device not found (%x:%x)" % (vid, pid))
        print(f'Found CH341 device ({vid:x}:{pid:x})')
        if (dev.bNumConfigurations != 1):
            raise ConnectionError("Device configuration error")
        dev.set_configuration()
        self.dev = dev


        #cmd = [self.CMD_I2C_STREAM, self.CMD_UIO_STM_US | 100, self.CMD_UIO_STM_END]
        #cnt = self.dev.write(self.BULK_WRITE_ENDPOINT, cmd)
        #if (cnt != len(cmd)):
        #    raise ConnectionError("Failed to issue Command")

        cmd = [self.CMD_UIO_STREAM, self.CMD_UIO_STM_DIR | 0x3F, self.CMD_UIO_STM_END]
        cnt = self.dev.write(self.BULK_WRITE_ENDPOINT, cmd)
        if (cnt != len(cmd)):
            raise ConnectionError("Failed to issue dir command")


    def spi_trans(self, data):
        cmd = [self.CMD_UIO_STREAM, self.CMD_UIO_STM_OUT | 0x36, self.CMD_UIO_STM_END]
        cnt = self.dev.write(self.BULK_WRITE_ENDPOINT, cmd)
        if (cnt != len(cmd)):
            raise ConnectionError("Failed to issue select cs")

        cmd = [self.CMD_SPI_STREAM]
        for c in data:
            cmd.append(self.reverse_table[c])

        cnt = self.dev.write(self.BULK_WRITE_ENDPOINT, cmd)
        #if (cnt != len(cmd)):
        #    raise ConnectionError("Failed to write data")

        data = self.dev.read(self.BULK_READ_ENDPOINT, cnt-1)

        cmd = [self.CMD_UIO_STREAM, self.CMD_UIO_STM_OUT | 0x37, self.CMD_UIO_STM_END]
        cnt = self.dev.write(self.BULK_WRITE_ENDPOINT, cmd)
        if (cnt != len(cmd)):
            raise ConnectionError("Failed to issue unselect cs")

        ret = []
        for c in data:
            ret.append(self.reverse_table[c])

        return list(ret)



project = projectLoader.load(args.json)

SHM_FILE = ""
SERIAL = ""
NET_IP = ""
SPI_CH341 = None
SPI_FTDI = None
if args.device and args.device.startswith("/dev/tty"):
    import serial
    SERIAL = args.device
    BAUD = args.baud
    ser = serial.Serial(SERIAL, BAUD, timeout=0.01)

elif args.device and args.device.startswith("/dev/shm/"):
    SHM_FILE = args.device
    fd = open(f"{SHM_FILE}.rx", "wb")
    fd.write(b'0'*10)
    fd.close()

elif args.device and args.device.startswith("CH341"):
    import usb.core
    import usb.util
    SPI_CH341 = CH341()

elif args.device and args.device.startswith("FTDI"):
    from pyftdi.spi import SpiController
    spi = SpiController(cs_count=2)
    spi.configure('ftdi://ftdi:2232h/2')
    SPI_FTDI = spi.get_port(cs=0, freq=1E6, mode=0)

elif args.device and args.device != "":
    NET_IP = args.device
    NET_PORT = args.port
    print("IP:", NET_IP)
    import socket

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.bind(('0.0.0.0', args.port))
    # clear buffer
    try:
        UDPClientSocket.settimeout(0.2)
        UDPClientSocket.recvfrom(100000)
    except:
        pass

else:
    import spidev

    bus = 0
    device = 1
    spi = spidev.SpiDev()
    spi.open(bus, device)
    spi.max_speed_hz = project["jdata"]["interface"][0].get("max", args.baud)
    spi.mode = 0
    spi.lsbfirst = False

INTERVAL = 100


data = [0] * (project["data_size"] // 8)
data[0] = 0x74
data[1] = 0x69
data[2] = 0x72
data[3] = 0x77

JOINTS = project["joints"]
VOUTS = project["vouts"]
VINS = project["vins"]
DOUTS = project["douts"]
DINS = project["dins"]

VIN_NAMES = project["vinnames"]
VOUT_NAMES = project["voutnames"]
DIN_NAMES = project["dinnames"]
DOUT_NAMES = project["doutnames"]
JOINT_TYPES = project["jointtypes"]

joints = [0] * project["joints"]
vouts = [0] * project["vouts"]
douts = [0] * project["douts"]

PRU_OSC = int(project["jdata"]["clock"]["speed"])

vout_types = []
for num, vout in enumerate(project["voutnames"]):
    vout_types.append(vout["type"])

vin_types = []
for num, vin in enumerate(project["vinnames"]):
    vin_types.append(vin["type"])

JOINT_ENABLE_BYTES = project["joints_en_total"] // 8
DIGITAL_OUTPUT_BYTES = project["douts_total"] // 8
DIGITAL_INPUT_BYTES = project["dins_total"] // 8


class modbus_vfd:
    FUNCTION_READ = 0x01
    FUNCTION_WRITE = 0x02
    WRITE_CONTROL_DATA = 0x03
    READ_CONTROL_STATUS = 0x04
    WRITE_FREQ_DATA = 0x05
    LOOP_TEST = 0x08
    FUNCTION_PD004 = 4
    FUNCTION_PD005 = 5
    FUNCTION_PD011 = 11
    FUNCTION_PD141 = 141
    FUNCTION_PD142 = 142
    FUNCTION_PD143 = 143
    FUNCTION_PD144 = 144
    CONTROL_Run_Fwd = 0x01
    CONTROL_Run_Rev = 0x11
    CONTROL_Stop = 0x08
    CONTROL_Run = 0x01
    CONTROL_Jog = 0x02
    CONTROL_Command_rf = 0x04
    CONTROL_Running = 0x08
    CONTROL_Jogging = 0x10
    CONTROL_Running_rf = 0x20
    CONTROL_Bracking = 0x40
    CONTROL_Track_Start = 0x80

    speed_command = 0
    spindle_speed_fb = 0
    freq_cmd = 0
    modbus_interval = 1
    modbus_counter = 0
    cmd_counter = 0

    rated_motor_voltage = 0
    rated_motor_current = 0
    base_freq = 0
    max_freq = 0
    freq_lower_limit = 0
    min_rpm = 0
    max_rpm = 0
    rated_motor_rev = 0
    rpm_at_50hz = 0
    motor_poles = 0
    SetF = 0
    OutF = 0
    OutA = 0
    RoTT = 0
    DCV = 0
    ACV = 0
    Cont = 0
    Tmp = 0
    addr = 1

    def __init__(self, addr):
        self.spindle_start_fwd = [
            0x01,
            self.WRITE_CONTROL_DATA,
            0x01,
            self.CONTROL_Run_Fwd,
        ]
        self.spindle_start_rev = [
            0x01,
            self.WRITE_CONTROL_DATA,
            0x01,
            self.CONTROL_Run_Rev,
        ]
        self.spindle_stop = [0x01, self.WRITE_CONTROL_DATA, 0x01, self.CONTROL_Stop]
        self.spindle_speed = [0x01, self.WRITE_FREQ_DATA, 0x02, 0x0, 0x0]
        self.spindle_PD005 = [0x01, self.FUNCTION_READ, 0x03, 5, 0x00, 0x00]
        self.spindle_PD011 = [0x01, self.FUNCTION_READ, 0x03, 11, 0x00, 0x00]
        self.spindle_PD141 = [0x01, self.FUNCTION_READ, 0x03, 141, 0x00, 0x00]
        self.spindle_PD142 = [0x01, self.FUNCTION_READ, 0x03, 142, 0x00, 0x00]
        self.spindle_PD143 = [0x01, self.FUNCTION_READ, 0x03, 143, 0x00, 0x00]
        self.spindle_PD144 = [0x01, self.FUNCTION_READ, 0x03, 144, 0x00, 0x00]
        self.spindle_status_SetF = [
            0x01,
            self.READ_CONTROL_STATUS,
            0x03,
            0x00,
            0x00,
            0x00,
        ]
        self.spindle_status_OutF = [
            0x01,
            self.READ_CONTROL_STATUS,
            0x03,
            0x01,
            0x00,
            0x00,
        ]
        self.spindle_status_OutA = [
            0x01,
            self.READ_CONTROL_STATUS,
            0x03,
            0x02,
            0x00,
            0x00,
        ]
        self.spindle_status_RoTT = [
            0x01,
            self.READ_CONTROL_STATUS,
            0x03,
            0x03,
            0x00,
            0x00,
        ]
        self.spindle_status_DCV = [
            0x01,
            self.READ_CONTROL_STATUS,
            0x03,
            0x04,
            0x00,
            0x00,
        ]
        self.spindle_status_ACV = [
            0x01,
            self.READ_CONTROL_STATUS,
            0x03,
            0x05,
            0x00,
            0x00,
        ]
        self.spindle_status_Cont = [
            0x01,
            self.READ_CONTROL_STATUS,
            0x03,
            0x06,
            0x00,
            0x00,
        ]
        self.spindle_status_Tmp = [
            0x01,
            self.READ_CONTROL_STATUS,
            0x03,
            0x07,
            0x00,
            0x00,
        ]
        self.run_cmd = self.spindle_stop
        self.addr = addr

    def crc16(self, data: bytearray, offset, length):
        if (
            data is None
            or offset < 0
            or offset > len(data) - 1
            and offset + length > len(data)
        ):
            return 0
        crc = 0xFFFF
        for i in range(length):
            crc ^= data[offset + i]
            for j in range(8):
                if (crc & 0x1) == 1:
                    crc = int((crc / 2)) ^ 40961
                else:
                    crc = int(crc / 2)
        return crc & 0xFFFF

    def set_speed(self, rpm):
        self.speed_command = abs(rpm)
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
                self.spindle_PD141,
                self.spindle_PD142,
                self.spindle_PD143,
                self.spindle_PD144,
                self.spindle_speed,
                self.run_cmd,
                self.spindle_status_OutA,
                self.spindle_status_RoTT,
                self.spindle_status_SetF,
                self.spindle_status_OutF,
                self.spindle_speed,
                self.run_cmd,
                self.spindle_status_ACV,
                self.spindle_status_DCV,
                self.spindle_status_Cont,
                self.spindle_status_Tmp,
                self.spindle_speed,
                self.run_cmd,
            ]
            cmd = cmds[self.cmd_counter]
            cmd[0] = self.addr

            if (
                cmd == self.spindle_speed
                and self.rpm_at_50hz > 0
                and self.rated_motor_rev > 0
            ):
                freq_comp = 0
                hz_per_rpm = self.max_freq / self.rated_motor_rev
                self.freq_cmd = int(
                    abs((self.speed_command + freq_comp) * hz_per_rpm * 100)
                )
                cmd[3] = (self.freq_cmd >> 8) & 0xFF
                cmd[4] = self.freq_cmd & 0xFF

            if self.cmd_counter < len(cmds) - 1:
                self.cmd_counter += 1
            else:
                self.cmd_counter = 0

            crc = self.crc16(cmd, 0, len(cmd))
            crcH = crc & 0xFF
            crcL = crc >> 8 & 0xFF
            # print("#########", cmd, crcH, crcL, len(cmd) + 2)

            data[0] = len(cmd) + 2
            for n in range(len(cmd)):
                data[n + 1] = cmd[n]
                print("### ", data[n + 1])
            data[n + 2] = crcH
            print("### ", data[n + 2])
            data[n + 3] = crcL
            print("### ", data[n + 3])

        else:
            self.modbus_counter += 1
        return data

    def feedback(self):
        feedback = {
            "speed_command": self.speed_command,
            "spindle_speed_fb": self.spindle_speed_fb,
            "freq_cmd": self.freq_cmd,
            "base_freq": self.base_freq,
            "max_freq": self.max_freq,
            "freq_lower_limit": self.freq_lower_limit,
            "min_rpm": self.min_rpm,
            "max_rpm": self.max_rpm,
            "rpm_at_50hz": self.rpm_at_50hz,
            "rated_motor_rev": self.rated_motor_rev,
            "SetF": self.SetF,
            "OutF": self.OutF,
            "OutA": self.OutA,
            "RoTT": self.RoTT,
            "DCV": self.DCV,
            "ACV": self.ACV,
            "motor_poles": self.motor_poles,
            "Cont": self.Cont,
            "Tmp": self.Tmp,
            "addr": self.addr,
        }
        return feedback

    def receive(self, data):
        pkglen = data[0]
        if self.addr != data[1]:
            print("WRONG ADDR: ", self.addr, data[1])
            return
        crc = self.crc16(data[1 : pkglen - 1], 0, pkglen - 2)
        crcH = crc & 0xFF
        crcL = crc >> 8 & 0xFF
        if data[pkglen - 1] != crcH or data[pkglen] != crcL:
            print("CSUM ERROR")
            return

        if data[2] == self.READ_CONTROL_STATUS and data[3] == 0x03:
            value = (data[5] << 8) | data[6]
            print(value)
            if data[4] == 0x00:
                self.SetF = value * 0.01
            elif data[4] == 0x01:
                self.OutF = value * 0.01
                self.spindle_speed_fb = (
                    self.OutF / self.max_freq
                ) * self.rated_motor_rev
                self.spindle_speed_fb_rps = self.spindle_speed_fb / 60.0
            elif data[4] == 0x02:
                self.OutA = value * 0.1
            elif data[4] == 0x03:
                self.RoTT = value
            elif data[4] == 0x04:
                self.DCV = value
            elif data[4] == 0x05:
                self.ACV = value
            elif data[4] == 0x06:
                self.Cont = value
            elif data[4] == 0x07:
                self.Tmp = value

        elif data[2] == self.FUNCTION_READ and data[3] == 0x03:
            value = (data[5] << 8) | data[6]
            if data[4] == self.FUNCTION_PD005:
                self.max_freq = value * 0.01
            elif data[4] == self.FUNCTION_PD004:
                self.base_freq = value * 0.01
            elif data[4] == self.FUNCTION_PD011:
                self.freq_lower_limit = value * 0.01
            elif data[4] == self.FUNCTION_PD141:
                self.rated_motor_voltage = value
            elif data[4] == self.FUNCTION_PD142:
                self.rated_motor_current = value
            elif data[4] == self.FUNCTION_PD143:
                self.motor_poles = value
            elif data[4] == self.FUNCTION_PD144:
                self.rpm_at_50hz = value
                self.rated_motor_rev = (self.rpm_at_50hz / 50.0) * self.max_freq

            if self.freq_lower_limit > self.max_freq:
                self.freq_lower_limit = self.max_freq


class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle(f"SPI-Test ({project['jdata']['name']} @ {args.device})")
        self.listFile = QListWidget()
        layout = QGridLayout()
        self.widgets = {}
        self.vbuffer = {}
        self.vminmax = {}
        self.animation = 0
        self.doutcounter = 0
        self.error_counter_spi = 0
        self.error_counter_net = 0
        self.time_trx = 0
        self.time_trx_max = 0
        self.vfd = {}
        self.pkg_in = 0
        self.pkg_out = 0

        # boutnames
        for num, bout in enumerate(project["boutnames"]):
            boutsize = bout["size"]
            if bout["type"] == "modbus":
                name = bout["name"]
                for protocol in bout["protocols"]:
                    if protocol["type"] == "hyvfd":
                        addr = protocol["addr"]
                        self.vfd[addr] = modbus_vfd(addr)

        gpy = 0

        self.widgets["connection"] = QLabel(f"CONNECTION:")
        layout.addWidget(self.widgets["connection"], gpy, 0)
        gpy += 1

        layout.addWidget(QLabel(f"JOINTS:"), gpy, 0)
        for jn in range(JOINTS):
            layout.addWidget(QLabel(f"JOINT{jn}"), gpy, jn + 3)
        gpy += 1
        for jn in range(JOINTS):
            layout.addWidget(QLabel(JOINT_TYPES[jn]), gpy, jn + 3)
        gpy += 1
        for jn in range(JOINTS):
            key = f"jcs{jn}"
            self.widgets[key] = QSlider(Qt.Horizontal)
            if JOINT_TYPES[jn] == "joint_rcservo":
                self.widgets[key].setMinimum(-100)
                self.widgets[key].setMaximum(100)
            else:
                self.widgets[key].setMinimum(-2000)
                self.widgets[key].setMaximum(2000)
            self.widgets[key].setValue(0)
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1

        for jn in range(JOINTS):
            key = f"jcs_reset{jn}"
            self.widgets[key] = QPushButton("0")
            self.widgets[key].clicked.connect(partial(self.slider_reset, f"jcs{jn}"))
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1

        layout.addWidget(QLabel(f"SET"), gpy, 1)
        for jn in range(JOINTS):
            key = f"jcraw{jn}"
            self.widgets[key] = QLabel(f"cmd: {jn}")
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1
        layout.addWidget(QLabel(f"OUT"), gpy, 1)
        for jn in range(JOINTS):
            key = f"jc{jn}"
            self.widgets[key] = QLabel(f"cmd: {jn}")
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1
        layout.addWidget(QLabel(f"FB"), gpy, 1)
        for jn in range(JOINTS):
            key = f"jf{jn}"
            self.widgets[key] = QLabel(f"joint: {jn}")
            layout.addWidget(self.widgets[key], gpy, jn + 3)
        gpy += 1
        layout.addWidget(QLabel(""), gpy, 1)
        gpy += 1

        layout.addWidget(QLabel(f"VOUT:"), gpy, 0)
        for vn in range(VOUTS):
            layout.addWidget(QLabel(VOUT_NAMES[vn]["_name"]), gpy, vn + 3)
        gpy += 1
        for vn in range(VOUTS):
            layout.addWidget(QLabel(vout_types[vn]), gpy, vn + 3)
        gpy += 1
        for vn in range(VOUTS):
            plugin_data = VOUT_NAMES[vn]
            plugin_name = plugin_data["_plugin"]
            vmin = 0
            vmax = 100
            if hasattr(project["plugins"][plugin_name], "vminmax"):
                (vmin, vmax) = project["plugins"][plugin_name].vminmax(plugin_data)

            key = f"vos{vn}"
            self.widgets[key] = QSlider(Qt.Horizontal)
            self.widgets[key].setMinimum(int(vmin))
            self.widgets[key].setMaximum(int(vmax))
            self.widgets[key].setValue(0)
            layout.addWidget(self.widgets[key], gpy, vn + 3)
        gpy += 1

        for vn in range(VOUTS):
            key = f"vos_reset{vn}"
            self.widgets[key] = QPushButton("0")
            self.widgets[key].clicked.connect(partial(self.slider_reset, f"vos{vn}"))
            layout.addWidget(self.widgets[key], gpy, vn + 3)
        gpy += 1

        layout.addWidget(QLabel(f"SET"), gpy, 1)
        for vn in range(VOUTS):
            key = f"vo{vn}"
            self.widgets[key] = QLabel(f"vo: {vn}")
            layout.addWidget(self.widgets[key], gpy, vn + 3)
        gpy += 1
        layout.addWidget(QLabel(""), gpy, 1)
        gpy += 1

        layout.addWidget(QLabel(f"VIN:"), gpy, 0)
        for vn in range(VINS):
            layout.addWidget(QLabel(VIN_NAMES[vn]["_name"]), gpy, vn + 3)
        gpy += 1
        for vn in range(VINS):
            layout.addWidget(QLabel(vin_types[vn]), gpy, vn + 3)
        gpy += 1
        layout.addWidget(QLabel(f"IN"), gpy, 1)
        for vn in range(VINS):
            key = f"vi{vn}"
            self.widgets[key] = QLabel(f"vin: {vn}")
            layout.addWidget(self.widgets[key], gpy, vn + 3)
        gpy += 1

        if args.graph:
            layout.addWidget(QLabel(f"Graph"), gpy, 1)
            for vn in range(VINS):
                key = f"vi{vn}_g"
                self.widgets[key] = QLabel()
                self.vbuffer[key] = [0] * 100
                self.vminmax[key] = [100000000, -100000000]
                layout.addWidget(self.widgets[key], gpy, vn + 3)
            gpy += 1

        layout.addWidget(QLabel(""), gpy, 1)
        gpy += 1

        if project["douts"]:
            for dbyte in range(DIGITAL_OUTPUT_BYTES):
                if dbyte == 0:
                    layout.addWidget(QLabel(f"DOUT:"), gpy, 0)
                    self.widgets["dout_auto"] = QCheckBox()
                    layout.addWidget(self.widgets["dout_auto"], gpy, 2)
                for dn in range(8):
                    key = f"doc{dbyte}{dn}"
                    self.widgets[key] = QCheckBox(DOUT_NAMES[dbyte * 8 + dn]["_name"])
                    self.widgets[key].setChecked(False)
                    layout.addWidget(self.widgets[key], gpy, dn + 3)
                    if dbyte * 8 + dn == DOUTS - 1:
                        break
                gpy += 1
            layout.addWidget(QLabel(""), gpy, 1)
            gpy += 1

        for dbyte in range(DIGITAL_INPUT_BYTES):
            if dbyte == 0:
                layout.addWidget(QLabel(f"DIN:"), gpy, 0)
            for dn in range(8):
                if dbyte * 8 + dn < len(DIN_NAMES):
                    layout.addWidget(
                        QLabel(DIN_NAMES[dbyte * 8 + dn]["_name"]), gpy, dn + 3
                    )
                if dbyte * 8 + dn == DINS - 1:
                    break
            gpy += 1
            for dn in range(8):
                key = f"dic{dbyte}{dn}"
                self.widgets[key] = QLabel("0")
                layout.addWidget(self.widgets[key], gpy, dn + 3)
                if dbyte * 8 + dn == DINS - 1:
                    break
            gpy += 1

        # boutnames
        for num, bout in enumerate(project["boutnames"]):
            boutsize = bout["size"]
            if bout["type"] == "modbus":
                name = bout["name"]
                for protocol in bout["protocols"]:
                    if protocol["type"] == "hyvfd":
                        layout.addWidget(QLabel(f"HYVFD:"), gpy, 0)
                        self.widgets[f"{name}-hyvfd"] = QSlider(Qt.Horizontal)
                        self.widgets[f"{name}-hyvfd"].setMinimum(-20000)
                        self.widgets[f"{name}-hyvfd"].setMaximum(20000)
                        self.widgets[f"{name}-hyvfd"].setValue(0)
                        layout.addWidget(self.widgets[f"{name}-hyvfd"], gpy, 3)

                        self.widgets[f"{name}-hyvfd-rst"] = QPushButton("0")
                        self.widgets[f"{name}-hyvfd-rst"].clicked.connect(
                            partial(self.slider_reset, f"{name}-hyvfd")
                        )
                        layout.addWidget(self.widgets[f"{name}-hyvfd-rst"], gpy, 4)
                        gpy += 1

                        for vn, vname in enumerate(
                            [
                                "speed_command",
                                "spindle_speed_fb",
                                "freq_cmd",
                                "max_freq",
                                "freq_lower_limit",
                                "min_rpm",
                                "max_rpm",
                                "rpm_at_50hz",
                                "rated_motor_rev",
                                "SetF",
                                "OutF",
                                "OutA",
                                "RoTT",
                                "DCV",
                                "ACV",
                                "Cont",
                                "Tmp",
                                "addr",
                                "motor_poles",
                            ]
                        ):
                            layout.addWidget(QLabel(vname), gpy, 3)
                            self.widgets[f"{name}-hyvfd-{vname}"] = QLabel(vname)
                            layout.addWidget(
                                self.widgets[f"{name}-hyvfd-{vname}"], gpy, 4
                            )
                            gpy += 1

        layout.addWidget(QLabel(""), gpy, 0)
        gpy += 1

        layout.addWidget(QLabel(f"ERRORS:"), gpy, 0)
        layout.addWidget(QLabel(f"SPI:"), gpy, 1)
        self.widgets["errors_spi"] = QLabel("0")
        layout.addWidget(self.widgets["errors_spi"], gpy, 2)

        layout.addWidget(QLabel(f"NET:"), gpy, 3)
        self.widgets["errors_net"] = QLabel("0")
        layout.addWidget(self.widgets["errors_net"], gpy, 4)

        layout.addWidget(QLabel(f"TIME:"), gpy, 5)
        self.widgets["time_trx"] = QLabel("0")
        layout.addWidget(self.widgets["time_trx"], gpy, 6)

        layout.addWidget(QLabel(f"MAX:"), gpy, 7)
        self.widgets["time_trx_max"] = QLabel("0")
        layout.addWidget(self.widgets["time_trx_max"], gpy, 8)

        layout.addWidget(QLabel(f"RATE:"), gpy, 9)
        self.widgets["error_rate"] = QLabel("0")
        layout.addWidget(self.widgets["error_rate"], gpy, 10)
        gpy += 1

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.runTimer)
        self.timer.start(INTERVAL)

    def slider_reset(self, key):
        self.widgets[key].setValue(0)

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
            if project["douts"]:
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
                            douts[dbyte] |= 1 << (7 - dn)
                        if dbyte * 8 + dn == DOUTS - 1:
                            break

            bn = 4
            for jn, value in enumerate(joints):
                # precalc
                if value == 0:
                    value = 0
                else:
                    if JOINT_TYPES[jn] == "joint_pwmdir":
                        value = value
                    else:
                        value = int(PRU_OSC / value / 2)

                key = f"jc{jn}"
                self.widgets[key].setText(str(value))

                joint = list(pack("<i", value))
                for byte in range(4):
                    data[bn + byte] = joint[byte]
                bn += 4

            for vn, value in enumerate(vouts):
                plugin_data = VOUT_NAMES[vn]
                plugin = plugin_data["type"]
                if hasattr(project["plugins"][plugin], "calculation_vout"):
                    value = int(project["plugins"][plugin].calculation_vout(plugin_data, value))

                vout = list(pack("<i", (value)))
                for byte in range(4):
                    data[bn + byte] = vout[byte]
                bn += 4

            # boutnames
            for num, bout in enumerate(project["boutnames"]):
                boutsize = bout["size"]
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
            if project["douts"]:
                for dbyte in range(DIGITAL_OUTPUT_BYTES):
                    data[bn] = douts[dbyte]
                    bn += 1


            self.pkg_out += 1
            if args.debug:
                print("")
                print(f"tx ({self.pkg_out}): {data}")
            start = time.time()
            if NET_IP:
                UDPClientSocket.sendto(bytes(data), (NET_IP, NET_PORT))
                UDPClientSocket.settimeout(0.2)
                msgFromServer = UDPClientSocket.recvfrom(len(data)*4)
                if len(msgFromServer[0]) == len(data):
                    rec = list(msgFromServer[0])
                else:
                    print(f"{self.pkg_out}/{self.pkg_in} WRONG DATASIZE: {len(msgFromServer[0])} / {len(data)}")
                    rec = list(msgFromServer[0])
            elif SERIAL:
                # clean_buffer
                while ser.inWaiting() > 0:
                    ser.read(1)
                ser.write(bytes(data))
                msgFromServer = ser.read(len(data))
                rec = list(msgFromServer)

            elif SPI_CH341 is not None:
                rec = SPI_CH341.spi_trans(data)

            elif SPI_FTDI is not None:
                rec = list(SPI_FTDI.exchange(data, duplex=True))

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

            self.time_trx = time.time() - start
            self.time_trx_max = max(self.time_trx, self.time_trx_max)

            pos = 0
            header = unpack("<i", bytes(rec[pos : pos + 4]))[0]
            pos += 4

            if header == 0x64617461:
                self.pkg_in += 1
                if args.debug:
                    print(f"PRU_DATA: 0x{header:x}")
                    # for num in range(JOINTS):
                    #    print(f' Joint({num}): {jointFeedback[num]} // 1')
                    # for num in range(VINS):
                    #    print(f' Var({num}): {processVariable[num]}')
                    # print(f'inputs {inputs:08b}')
                self.widgets["connection"].setText("CONNECTED")
                self.widgets["connection"].setStyleSheet("background-color: green")
            else:
                print(f"ERROR: Unknown Header: 0x{header:x}")
                self.error_counter_spi += 1
                self.widgets["connection"].setText(f"ERROR: 0x{header:x}")
                self.widgets["connection"].setStyleSheet("background-color: red")

            if args.debug:
                print(f"Duration: {self.time_trx * 1000:02.02f}ms / {self.time_trx_max * 1000:02.02f}ms")
                print(f"rx ({self.pkg_in}): {rec}")

            jointFeedback = [0] * JOINTS
            processVariable = [0] * VINS

            for num in range(JOINTS):
                jointFeedback[num] = unpack("<i", bytes(rec[pos : pos + 4]))[0]
                pos += 4

            for bitsize in (32, 16, 8):
                for num in range(VINS):
                    vin = project["vinnames"][num]
                    bits = vin.get("_bits", 32)
                    if bitsize != bits:
                        continue
                    size = (bits // 8)
                    diff = (4 - size)
                    if diff > 0:
                        block = rec[pos : pos + size] + ([0] * diff)
                    else:
                        block = rec[pos : pos + size]
                    processVariable[num] = unpack("<i", bytes(block))[0]
                    pos += size

            # binnames
            binValues = {}
            for num, bins in enumerate(project["binnames"]):
                binValues[num] = []
                binsize = bins["size"]
                for binn in range(binsize // 8):
                    binValues[num].append(unpack("<B", bytes(rec[pos : pos + 1]))[0])
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
                                    self.widgets[f"{name}-hyvfd-{vname}"].setText(
                                        str(vvalue)
                                    )

            inputs = []
            for dbyte in range(DIGITAL_INPUT_BYTES):
                inputs.append(unpack("<B", bytes(rec[pos : pos + 1]))[0])
                pos += 1


            for jn, value in enumerate(joints):
                key = f"jf{jn}"
                self.widgets[key].setText(str(jointFeedback[jn]))

            for vn in range(VINS):
                key = f"vi{vn}"
                unit = ""
                value = processVariable[vn]

                plugin_data = VIN_NAMES[vn]
                plugin_name = plugin_data["_plugin"]
                if hasattr(project["plugins"][plugin_name], "calculation_vin"):
                    (value, unit) = project["plugins"][plugin_name].calculation_vin(plugin_data, value)

                self.widgets[key].setText(f"{value:0.3f}{unit}")

                if args.graph:
                    key = f"vi{vn}_g"
                    self.vbuffer[key].pop(0)
                    self.vbuffer[key].append(value)
                    for px, val in enumerate(self.vbuffer[key]):
                        self.vminmax[key][0] = min(self.vminmax[key][0], val)
                        self.vminmax[key][1] = max(self.vminmax[key][1], val)
                    vdiff = max(1, self.vminmax[key][1] - self.vminmax[key][0])

                    canvas = QtGui.QPixmap(100, 100)
                    canvas.fill(Qt.white)
                    self.widgets[key].setPixmap(canvas)
                    painter = QtGui.QPainter(self.widgets[key].pixmap())
                    last = 0
                    for px, val in enumerate(self.vbuffer[key]):
                        py = int(99 - (val * 99 / vdiff))
                        if px > 0:
                            painter.setPen(Qt.red)
                            painter.drawLine(px-1, last, px, py)
                        last = py
                    painter.end()

            for dbyte in range(DIGITAL_INPUT_BYTES):
                for dn in range(8):
                    key = f"dic{dbyte}{dn}"

                    value = "0"
                    if inputs[dbyte] & (1 << (7 - dn)) != 0:
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
            print(traceback.format_exc())
            self.error_counter_net += 1
            self.widgets["connection"].setText(f"ERROR: {e}")
            self.widgets["connection"].setStyleSheet("background-color: red")

        error_rate = self.pkg_in * 100 / self.pkg_out
        self.widgets["errors_spi"].setText(str(self.error_counter_spi))
        self.widgets["errors_net"].setText(str(self.error_counter_net))
        self.widgets["time_trx"].setText(f"{self.time_trx * 1000:02.02f}ms")
        self.widgets["time_trx_max"].setText(f"{self.time_trx_max * 1000:02.02f}ms")
        self.widgets["error_rate"].setText(f"{error_rate:0.2f}%")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())
