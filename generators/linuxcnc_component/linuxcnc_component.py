
import os
import sys

def generate(project):
    print("generating linux-cnc component")

    rio_data = []
    rio_data.append("#ifndef RIO_H")
    rio_data.append("#define RIO_H")
    rio_data.append("")
    transport = project['jdata'].get('transport', 'SPI')
    if transport == 'UDP':
        rio_data.append("#define TRANSPORT_UDP")
        rio_data.append(f"#define UDP_IP \"{project['jdata'].get('ip', '192.168.10.132')}\"")
    elif transport == 'SERIAL':
        rio_data.append("#define TRANSPORT_SERIAL")
        rio_data.append(f"#define SERIAL_PORT \"{project['jdata'].get('tty', '/dev/ttyUSB1')}\"")
        rio_data.append(f"#define SERIAL_SPEED B{project['jdata']['interface'][0].get('baud', '1000000')}")
    elif transport == 'SPI':
        rio_data.append("#define TRANSPORT_SPI")
        #rio_data.append("#define SPI_SPEED BCM2835_SPI_CLOCK_DIVIDER_128")
        rio_data.append("#define SPI_SPEED BCM2835_SPI_CLOCK_DIVIDER_256")
    else:
        print("ERROR: UNKNOWN transport protocol:", transport)
        sys.exit(1)
    rio_data.append("")
    rio_data.append(f"#define JOINTS               {project['joints']}")
    rio_data.append(f"#define JOINT_ENABLE_BYTES   {project['joints_en_total'] // 8}")
    rio_data.append(f"#define VARIABLE_OUTPUTS     {project['vouts']}")
    rio_data.append(f"#define VARIABLE_INPUTS      {project['vins']}")
    rio_data.append(f"#define VARIABLES            {max(project['vins'], project['vouts'])}")
    rio_data.append(f"#define DIGITAL_OUTPUTS      {project['douts']}")
    rio_data.append(f"#define DIGITAL_OUTPUT_BYTES {project['douts_total'] // 8}")
    rio_data.append(f"#define DIGITAL_INPUTS       {project['dins']}")
    rio_data.append(f"#define DIGITAL_INPUT_BYTES  {project['dins_total'] // 8}")
    rio_data.append(f"#define SPIBUFSIZE           {project['data_size'] // 8}")
    index_num = 0
    for num in range(project['dins']):
        dname = project['dinnames'][num]["_name"]
        if dname.endswith("-index-enable-out"):
            index_num += 1
    if index_num > 0:
        rio_data.append(f"#define INDEX_MAX            {index_num}")
        rio_data.append(f"#define INDEX_INIT           {{{','.join(['0.0'] * index_num)}}}")

    rio_data.append("")
    rio_data.append("#define PRU_DATA            0x64617461")
    rio_data.append("#define PRU_READ            0x72656164")
    rio_data.append("#define PRU_WRITE           0x77726974")
    rio_data.append("#define PRU_ESTOP           0x65737470")
    rio_data.append("#define STEPBIT             22")
    rio_data.append("#define STEP_MASK           (1L<<STEPBIT)")
    rio_data.append("#define STEP_OFFSET         (1L<<(STEPBIT-1))")
    rio_data.append(f"#define PRU_BASEFREQ        100000000")
    rio_data.append(f"#define PRU_OSC             {project['jdata']['clock']['speed']}")
    rio_data.append("")

    rio_data.append("#define TYPE_VOUT_RAW  0")
    rio_data.append("#define TYPE_VOUT_PWM  1")
    rio_data.append("#define TYPE_VOUT_PWMDIR  2")
    rio_data.append("#define TYPE_VOUT_RCSERVO 3")
    rio_data.append("#define TYPE_VOUT_SINE 4")
    rio_data.append("#define TYPE_VOUT_FREQ 5")
    rio_data.append("#define TYPE_VOUT_UDPOTI 6")

    rio_data.append("#define TYPE_VIN_RAW  0")
    rio_data.append("#define TYPE_VIN_FREQ 1")
    rio_data.append("#define TYPE_VIN_TIME 2")
    rio_data.append("#define TYPE_VIN_SONAR 3")
    rio_data.append("#define TYPE_VIN_ADC 4")
    rio_data.append("#define TYPE_VIN_ENCODER 5")
    rio_data.append("#define TYPE_VIN_NTC 6")

    rio_data.append("#define JOINT_FB_REL 0")
    rio_data.append("#define JOINT_FB_ABS 1")

    rio_data.append("#define JOINT_STEPPER 0")
    rio_data.append("#define JOINT_RCSERVO 1")
    rio_data.append("#define JOINT_PWMDIR  2")

    rio_data.append("#define DTYPE_IO 0")
    rio_data.append("#define DTYPE_INDEX 1")

    vouts_min = []
    vouts_max = []
    vouts_type = []
    vouts_freq = []
    for vout in project["voutnames"]:
        freq = vout.get('frequency', 10000)
        if vout.get('type') == "sine":
            vouts_min.append(str(vout.get("min", -100)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append("30")
        elif vout.get('type') == "pwm":
            if vout.get('dir'):
                vouts_min.append("0")
            else:
                vouts_min.append(str(vout.get("min", 0)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append(str(vout.get("frequency", freq)))
        elif vout.get('type') == "rcservo":
            freq = vout.get('frequency', 100)
            vouts_min.append(str(vout.get("min", -100)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append(str(vout.get("frequency", freq)))
        else:
            vouts_min.append(str(vout.get("min", 0)))
            vouts_max.append(str(vout.get("max", 10.0)))
            vouts_freq.append(str(vout.get("frequency", freq)))

        if vout.get('type') == "vout_pwm" and vout.get('dir'):
            vouts_type.append(f"TYPE_{vout['type'].upper()}DIR")
        elif vout.get('type') == "vout_frequency":
            vouts_type.append(f"TYPE_VOUT_FREQ")
        elif vout.get('type') == "vout_pwm":
            vouts_type.append(f"TYPE_VOUT_PWM")
        elif vout.get('type') == "vout_sine":
            vouts_type.append(f"TYPE_VOUT_SINE")
        elif vout.get('type') == "vout_udpoti":
            vouts_type.append(f"TYPE_VOUT_UDPOTI")
        else:
            vouts_type.append(f"TYPE_VOUT_RAW")

    vins_type = []
    for vin in project["vinnames"]:
        if vin.get('type') == "vin_frequency":
            vins_type.append(f"TYPE_VIN_FREQ")
        elif vin.get('type') == "vin_pwmcounter":
            vins_type.append(f"TYPE_VIN_TIME")
        elif vin.get('type') == "vin_ads1115" and vin.get('sensor') == "NTC":
            vins_type.append(f"TYPE_VIN_NTC")
        elif vin.get('type') == "vin_ads1115":
            vins_type.append(f"TYPE_VIN_ADC")
        elif vin.get('type') in ("vin_quadencoder", "vin_quadencoderz"):
            vins_type.append(f"TYPE_VIN_ENCODER")
        else:
            vins_type.append(f"TYPE_VIN_RAW")

    rio_data.append(f"float vout_min[VARIABLE_OUTPUTS] = {{{', '.join(vouts_min)}}};")
    rio_data.append(f"float vout_max[VARIABLE_OUTPUTS] = {{{', '.join(vouts_max)}}};")
    rio_data.append(f"float vout_freq[VARIABLE_OUTPUTS] = {{{', '.join(vouts_freq)}}};")
    rio_data.append(f"uint8_t vout_type[VARIABLE_OUTPUTS] = {{{', '.join(vouts_type)}}};")
    rio_data.append(f"uint8_t vin_type[VARIABLE_INPUTS] = {{{', '.join(vins_type)}}};")
    rio_data.append("")

    joints_fb_type = []
    for num, joint in enumerate(project["jointnames"]):
        if joint.get('type') == "joint_rcservo":
            joints_fb_type.append("JOINT_FB_ABS")
        else:
            joints_fb_type.append("JOINT_FB_REL")
    rio_data.append(f"uint8_t joints_fb_type[JOINTS] = {{{', '.join(joints_fb_type)}}};")
    rio_data.append("")

    joints_type = []
    for num, joint in enumerate(project["jointnames"]):
        if joint.get('type') == "joint_rcservo":
            joints_type.append("JOINT_RCSERVO")
        elif joint.get('type') == "joint_pwmdir":
            joints_type.append("JOINT_PWMDIR")
        else:
            joints_type.append("JOINT_STEPPER")
    rio_data.append(f"uint8_t joints_type[JOINTS] = {{{', '.join(joints_type)}}};")
    rio_data.append("")

    rio_data.append("typedef union {")
    rio_data.append("    struct {")
    rio_data.append("        uint8_t txBuffer[SPIBUFSIZE];")
    rio_data.append("    };")
    rio_data.append("    struct {")
    rio_data.append("        int32_t header;")
    rio_data.append("        int32_t jointFreqCmd[JOINTS];")
    rio_data.append("        int32_t setPoint[VARIABLE_OUTPUTS];")
    rio_data.append("        uint8_t jointEnable[JOINT_ENABLE_BYTES];")
    rio_data.append("        uint8_t outputs[DIGITAL_OUTPUT_BYTES];")
    rio_data.append("    };")
    rio_data.append("} txData_t;")
    rio_data.append("")
    rio_data.append("typedef union")
    rio_data.append("{")
    rio_data.append("    struct {")
    rio_data.append("        uint8_t rxBuffer[SPIBUFSIZE];")
    rio_data.append("    };")
    rio_data.append("    struct {")
    rio_data.append("        int32_t header;")
    rio_data.append("        int32_t jointFeedback[JOINTS];")
    rio_data.append("        int32_t processVariable[VARIABLE_INPUTS];")
    rio_data.append("        uint8_t inputs[DIGITAL_INPUT_BYTES];")
    rio_data.append("    };")
    rio_data.append("} rxData_t;")
    rio_data.append("")
    rio_data.append("#endif")
    rio_data.append("")

    rio_data.append("const char vin_names[][32] = {")
    for num in range(project['vins']):
        dname = project['vinnames'][num]["_name"]
        rio_data.append(f"    \"{dname}\",")
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char vout_names[][32] = {")
    for num in range(project['vouts']):
        dname = project['voutnames'][num]["_name"]
        rio_data.append(f"    \"{dname}\",")
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char din_names[][32] = {")
    for num in range(project['dins']):
        dname = project['dinnames'][num]["_name"]
        rio_data.append(f"    \"{dname}\",")
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char dout_names[][32] = {")
    for num in range(project['douts']):
        dname = project['doutnames'][num]["_name"]
        rio_data.append(f"    \"{dname}\",")
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char din_types[] = {")
    for num in range(project['dins']):
        dname = project['dinnames'][num]["_name"]
        if dname.endswith("-index-enable-out"):
            rio_data.append(f"    DTYPE_INDEX,")
        else:
            rio_data.append(f"    DTYPE_IO,")

    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char dout_types[] = {")
    for num in range(project['douts']):
        dname = project['doutnames'][num]["_name"]
        if dname.endswith("-index-enable"):
            rio_data.append(f"    DTYPE_INDEX,")
        else:
            rio_data.append(f"    DTYPE_IO,")
    rio_data.append("};")
    rio_data.append("")


    open(f"{project['LINUXCNC_PATH']}/Components/rio.h", "w").write("\n".join(rio_data))

    os.system(f"cp -a generators/linuxcnc_component/*.c {project['LINUXCNC_PATH']}/Components/")
    os.system(f"cp -a generators/linuxcnc_component/*.h {project['LINUXCNC_PATH']}/Components/")
