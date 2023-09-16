
def generate(project):
    print("generating qtgui")

    spitest_data = []
    spitest_data.append("")
    spitest_data.append("import time")
    spitest_data.append("from struct import *")
    spitest_data.append("import sys")
    spitest_data.append("from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel,QSlider,QCheckBox")
    spitest_data.append("from PyQt5.QtCore import QTimer,QDateTime, Qt")
    spitest_data.append("")
    spitest_data.append("SERIAL = ''")
    spitest_data.append("NET_IP = ''")
    spitest_data.append("if len(sys.argv) > 1 and sys.argv[1].startswith('/dev/tty'):")
    spitest_data.append("    import serial")
    spitest_data.append("    SERIAL = sys.argv[1]")
    spitest_data.append("    BAUD = 2000000")
    spitest_data.append("    ser = serial.Serial(SERIAL, BAUD, timeout=0.001)")
    spitest_data.append("elif len(sys.argv) > 1 and sys.argv[1] != '':")
    spitest_data.append("    NET_IP = sys.argv[1]")
    spitest_data.append("    NET_PORT = 2390")
    spitest_data.append("    print('IP:', NET_IP)")
    spitest_data.append("    import socket")
    spitest_data.append("else:")
    spitest_data.append("    import spidev")
    spitest_data.append("    bus = 0")
    spitest_data.append("    device = 1")
    spitest_data.append("    spi = spidev.SpiDev()")
    spitest_data.append("    spi.open(bus, device)")
    spitest_data.append(f"    spi.max_speed_hz = {project['jdata']['interface'][0].get('max', 2000000)}")
    spitest_data.append("    spi.mode = 0")
    spitest_data.append("    spi.lsbfirst = False")
    spitest_data.append("")
    spitest_data.append("INTERVAL = 100")
    spitest_data.append("")
    spitest_data.append(f"data = [0] * {project['data_size'] // 8}")
    spitest_data.append("data[0] = 0x74")
    spitest_data.append("data[1] = 0x69")
    spitest_data.append("data[2] = 0x72")
    spitest_data.append("data[3] = 0x77")
    spitest_data.append("")
    spitest_data.append(f"JOINTS = {project['joints']}")
    spitest_data.append(f"VOUTS = {project['vouts']}")
    spitest_data.append(f"VINS = {project['vins']}")
    spitest_data.append(f"DOUTS = {project['douts']}")
    spitest_data.append(f"DINS = {project['dins']}")
    spitest_data.append("")
    spitest_data.append(f"VIN_NAMES = {project['vinnames']}")
    spitest_data.append(f"VOUT_NAMES = {project['voutnames']}")
    spitest_data.append(f"DIN_NAMES = {project['dinnames']}")
    spitest_data.append(f"DOUT_NAMES = {project['doutnames']}")
    spitest_data.append(f"JOINT_TYPES = {project['jointtypes']}")
    spitest_data.append("")

    spitest_data.append("joints = [")
    for _num in range(project['joints']):
        spitest_data.append("    0,")
    spitest_data.append("]")
    spitest_data.append("")

    spitest_data.append("vouts = [")
    for _num in range(project['vouts']):
        spitest_data.append("    0,")
    spitest_data.append("]")
    spitest_data.append("")

    spitest_data.append("douts = [")
    for _num in range(project['douts']):
        spitest_data.append("    0,")
    spitest_data.append("]")
    spitest_data.append("")

    spitest_data.append(f"PRU_OSC = {project['jdata']['clock']['speed']}")
    spitest_data.append("")

    spitest_data.append("vinminmax = [")
    for num, vin in enumerate(project["vinnames"]):
        if vin.get("type") == "frequency":
            spitest_data.append(f"    ({vin.get('min', -100)}, {vin.get('max', 100)}, 'frequency', 0),")
        elif vin.get("type") == "pwm":
            spitest_data.append(f"    ({vin.get('min', -100)}, {vin.get('max', 100)}, 'pwm', 0),")
        elif vin.get("type") == "sonar":
            spitest_data.append(f"    ({vin.get('min', 0)}, {vin.get('max', 100000)}, 'sonar', 0),")
        else:
            spitest_data.append(f"    ({vin.get('min', -100)}, {vin.get('max', 100)}, '', 0),")

    spitest_data.append("]")
    spitest_data.append("")

    spitest_data.append("vout_types = [")
    for num, vout in enumerate(project["voutnames"]):
        spitest_data.append(f"    '{vout['type']}',")
    spitest_data.append("]")
    spitest_data.append("")

    spitest_data.append("vin_types = [")
    for num, vin in enumerate(project["vinnames"]):
        spitest_data.append(f"    '{vin['type']}',")
    spitest_data.append("]")
    spitest_data.append("")

    spitest_data.append("voutminmax = [")
    for num, vout in enumerate(project["voutnames"]):
        if vout.get('type') == "vout_sine":
            spitest_data.append(f"    ({vout.get('min', -100)}, {vout.get('max', 100)}, 'sine', 30),")
        elif vout.get('type') == "pwm":
            freq = vout.get('vout_frequency', 10000)
            if "dir" in vout:
                spitest_data.append(f"    (0, {vout.get('max', 100)}, 'pwmdir', {freq}),")
            else:
                spitest_data.append(f"    ({vout.get('min', 0)}, {vout.get('max', 100)}, 'pwm', {freq}),")
        elif vout.get('type') == "vout_rcservo":
            freq = vout.get('frequency', 100)
            spitest_data.append(f"    ({vout.get('min', -100)}, {vout.get('max', 100)}, 'rcservo', {freq}),")
        elif vout.get('type') == "vout_frequency":
            spitest_data.append(f"    ({vout.get('min', 0)}, {vout.get('max', 100000)}, 'frequency', 0),")
        elif vout.get('type') == "vout_udpoti":
            spitest_data.append(f"    ({vout.get('min', 0)}, {vout.get('max', 100)}, 'udpoti', 0),")
        elif vout.get('type') == "vout_spipoti":
            spitest_data.append(f"    ({vout.get('min', 0)}, {vout.get('max', 255)}, 'spipoti', 0),")
        else:
            spitest_data.append(f"    ({vout.get('min', 0)}, {vout.get('max', 10)}, 'scale', 1),")
    spitest_data.append("]")
    spitest_data.append("")
    spitest_data.append(f"JOINT_ENABLE_BYTES = {project['joints_en_total'] // 8}")
    spitest_data.append(f"DIGITAL_OUTPUT_BYTES = {project['douts_total'] // 8}")
    spitest_data.append(f"DIGITAL_INPUT_BYTES = {project['dins_total'] // 8}")
    spitest_data.append("")
    
    spitest_data.append("""

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

        gpy = 0

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
                self.widgets[key].setMinimum(-voutminmax[vn][1])
            else:
                self.widgets[key].setMinimum(voutminmax[vn][0])
            self.widgets[key].setMaximum(voutminmax[vn][1])
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

        #data = [0] * {project['data_size'] // 8}
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

            douts = []
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


            # jointEnable and dout (TODO: split in bits)
            for dbyte in range(JOINT_ENABLE_BYTES):
                data[bn] = 0xFF
                bn += 1

            # dout
            for dbyte in range(DIGITAL_OUTPUT_BYTES):
                data[bn] = douts[dbyte]
                bn += 1

            print("")
            print("tx:", data)
            start = time.time()
            if NET_IP:
                UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                UDPClientSocket.sendto(bytes(data), (NET_IP, NET_PORT))
                UDPClientSocket.settimeout(0.2)
                msgFromServer = UDPClientSocket.recvfrom(len(data))
                rec = list(msgFromServer[0])
            elif SERIAL:
                ser.write(bytes(data))
                msgFromServer = ser.read(len(data))
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
            else:
                print(f'ERROR: Unknown Header: 0x{header:x}')
                self.error_counter_spi += 1

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

        self.widgets["errors_spi"].setText(str(self.error_counter_spi))
        self.widgets["errors_net"].setText(str(self.error_counter_net))
        self.widgets["time_trx"].setText(f"{self.time_trx * 1000:02.02f}ms")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())


    """)

    open(f"{project['FIRMWARE_PATH']}/qt_spitest.py", "w").write("\n".join(spitest_data))



