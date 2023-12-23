import os
import sys


def generate(project):
    print("generating linux-cnc component")

    rio_data = []
    rio_data.append("#ifndef RIO_H")
    rio_data.append("#define RIO_H")
    rio_data.append("")

    for component_file in project["component_files"]:
        if component_file.endswith(".h"):
            rio_data.append(f'#include "{component_file}"')

    rio_data.append("")
    transport = project["jdata"].get("transport", "SPI")
    if transport == "UDP":
        rio_data.append("#define TRANSPORT_UDP")
        interface = project['jdata'].get('interface', {})
        if interface:
            ip = project['jdata'].get('ip', interface[0].get('ip', '192.168.10.132'))
        else:
            ip = project['jdata'].get('ip', '192.168.10.132')
        rio_data.append(
            f"#define UDP_IP \"{ip}\""
        )
    elif transport == "SERIAL":
        print("#####################################################################")
        print("# WARNING: do not use serial for real systems, this will not work ! #")
        print("#####################################################################")
        rio_data.append("#define TRANSPORT_SERIAL")
        rio_data.append(
            f"#define SERIAL_PORT \"{project['jdata'].get('tty', '/dev/ttyUSB1')}\""
        )
        rio_data.append(
            f"#define SERIAL_SPEED B{project['jdata']['interface'][0].get('baud', '1000000')}"
        )
    elif transport == "SPI":
        rpi_spi_mosi = project['jdata'].get('rpispi', {}).get('MOSI', 10)
        rpi_spi_miso = project['jdata'].get('rpispi', {}).get('MISO', 9)
        rpi_spi_clk = project['jdata'].get('rpispi', {}).get('CLK', 11)
        rpi_spi_cs = project['jdata'].get('rpispi', {}).get('CS', 7)
        rpi_spi_prescaler = project['jdata'].get('rpispi', {}).get('PRESCALER', 256)
        rio_data.append("#define TRANSPORT_SPI")
        rio_data.append("// for Raspberry 3 and 4")
        rio_data.append("// If you are using a different board refer to this for the pin mapping")
        rio_data.append("//       https://elinux.org/RPi_BCM2835_GPIOs")
        rio_data.append("// If you are using the RPi Compute Module, just use the GPIO number: there is no need to use one of these symbolic names")
        rio_data.append(f"#define SPI_PIN_MOSI {rpi_spi_mosi}")
        rio_data.append(f"#define SPI_PIN_MISO {rpi_spi_miso}")
        rio_data.append(f"#define SPI_PIN_CLK {rpi_spi_clk}")
        rio_data.append(f"#define SPI_PIN_CS {rpi_spi_cs}")
        rio_data.append(f"#define SPI_SPEED BCM2835_SPI_CLOCK_DIVIDER_{rpi_spi_prescaler}")
    elif transport == "FTDI":
        print("##################################################################")
        print("# WARNING: do not use usb for real systems, this will not work ! #")
        print("##################################################################")
        rio_data.append("#define TRANSPORT_FTDI")
    else:
        print(f"ERROR: UNKNOWN transport protocol: {transport} (UDP, SPI, SERIAL)")
        sys.exit(1)

    rio_data.append("")
    rio_data.append(f"#define JOINTS               {project['joints']}")
    rio_data.append(f"#define JOINT_ENABLE_BYTES   {project['joints_en_total'] // 8}")
    rio_data.append(f"#define VARIABLE_OUTPUTS     {project['vouts']}")

    vinBits = {
        32: 0,
        16: 0,
        8: 0,
    }
    for vin in project['vinnames']:
        bits = vin.get("_bits", 32)
        vinBits[bits] += 1

    for bits, num in vinBits.items():
        rio_data.append(f"#define VARIABLE_INPUTS_{bits}   {num}")
    rio_data.append(f"#define VARIABLE_INPUTS      {sum(vinBits.values())}")

    rio_data.append(
        f"#define VARIABLES            {max(project['vins'], project['vouts'])}"
    )
    rio_data.append(f"#define DIGITAL_OUTPUTS      {project['douts']}")
    rio_data.append(f"#define DIGITAL_OUTPUT_BYTES {project['douts_total'] // 8}")
    rio_data.append(f"#define DIGITAL_INPUTS       {project['dins']}")
    rio_data.append(f"#define DIGITAL_INPUT_BYTES  {project['dins_total'] // 8}")
    rio_data.append(f"#define SPIBUFSIZE           {project['data_size'] // 8}")
    index_num = 0
    for num in range(project["dins"]):
        dname = project["dinnames"][num]["_name"]
        if dname.endswith("-index-enable-out"):
            index_num += 1
    if index_num > 0:
        rio_data.append(f"#define INDEX_MAX            {index_num}")
        rio_data.append(
            f"#define INDEX_INIT           {{{','.join(['0.0'] * index_num)}}}"
        )

    rio_data.append("")
    rio_data.append("#define PRU_DATA            0x64617461")
    rio_data.append("#define PRU_READ            0x72656164")
    rio_data.append("#define PRU_WRITE           0x77726974")
    rio_data.append("#define PRU_ESTOP           0x65737470")
    rio_data.append("#define STEPBIT             22")
    rio_data.append("#define STEP_MASK           (1L<<STEPBIT)")
    rio_data.append("#define STEP_OFFSET         (1L<<(STEPBIT-1))")
    rio_data.append("#define PRU_BASEFREQ        100000000")
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
    rio_data.append("#define TYPE_VIN_DS18B20 7")
    rio_data.append("#define TYPE_VIN_MAX6675 8")

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
        freq = vout.get("frequency", 10000)
        if vout.get("type") == "sine":
            vouts_min.append(str(vout.get("min", -100)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append("30")
        elif vout.get("type") == "pwm":
            if vout.get("dir"):
                vouts_min.append("0")
            else:
                vouts_min.append(str(vout.get("min", 0)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append(str(vout.get("frequency", freq)))
        elif vout.get("type") == "rcservo":
            freq = vout.get("frequency", 100)
            vouts_min.append(str(vout.get("min", -100)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append(str(vout.get("frequency", freq)))
        else:
            vouts_min.append(str(vout.get("min", 0)))
            vouts_max.append(str(vout.get("max", 10.0)))
            vouts_freq.append(str(vout.get("frequency", freq)))

        if vout.get("type") == "vout_pwm" and vout.get("dir"):
            vouts_type.append(f"TYPE_{vout['type'].upper()}DIR")
        elif vout.get("type") == "vout_frequency":
            vouts_type.append("TYPE_VOUT_FREQ")
        elif vout.get("type") == "vout_pwm":
            vouts_type.append("TYPE_VOUT_PWM")
        elif vout.get("type") == "vout_sine":
            vouts_type.append("TYPE_VOUT_SINE")
        elif vout.get("type") == "vout_udpoti":
            vouts_type.append("TYPE_VOUT_UDPOTI")
        else:
            vouts_type.append("TYPE_VOUT_RAW")

    rio_data.append(f"float vout_min[VARIABLE_OUTPUTS] = {{{', '.join(vouts_min)}}};")
    rio_data.append(f"float vout_max[VARIABLE_OUTPUTS] = {{{', '.join(vouts_max)}}};")
    rio_data.append(f"float vout_freq[VARIABLE_OUTPUTS] = {{{', '.join(vouts_freq)}}};")
    rio_data.append(
        f"uint8_t vout_type[VARIABLE_OUTPUTS] = {{{', '.join(vouts_type)}}};"
    )
    rio_data.append("")

    joints_fb_type = []
    for num, joint in enumerate(project["jointnames"]):
        if joint.get("type") == "joint_rcservo":
            joints_fb_type.append("JOINT_FB_ABS")
        else:
            joints_fb_type.append("JOINT_FB_REL")
    rio_data.append(
        f"uint8_t joints_fb_type[JOINTS] = {{{', '.join(joints_fb_type)}}};"
    )
    rio_data.append("")

    joints_type = []
    for num, joint in enumerate(project["jointnames"]):
        if joint.get("type") == "joint_rcservo":
            joints_type.append("JOINT_RCSERVO")
        elif joint.get("type") == "joint_pwmdir":
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
    for num, bout in enumerate(project["boutnames"]):
        rio_data.append(f"        uint8_t {bout['_prefix']}[{bout['size'] // 8}];")
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

    for bits, num in vinBits.items():
        rio_data.append(f"        int{bits}_t processVariable{bits}[VARIABLE_INPUTS_{bits}];")

    for num, bins in enumerate(project["binnames"]):
        rio_data.append(f"        uint8_t {bins['_prefix']}[{bins['size'] // 8}];")

    rio_data.append("        uint8_t inputs[DIGITAL_INPUT_BYTES];")
    rio_data.append("    };")
    rio_data.append("} rxData_t;")
    rio_data.append("")
    rio_data.append("#endif")
    rio_data.append("")

    rio_data.append("const char vin_type[] = {")
    for bitsize, num in vinBits.items():
        for num in range(project["vins"]):
            vin = project["vinnames"][num]
            dname = vin["_name"]
            bits = vin.get("_bits", 32)
            if bits == bitsize:
                if vin.get("type") == "vin_frequency":
                    rio_data.append("    TYPE_VIN_FREQ,")
                elif vin.get("type") == "vin_pwmcounter":
                    rio_data.append("    TYPE_VIN_TIME,")
                elif vin.get("type") == "vin_ads1115" and vin.get("sensor") == "NTC":
                    rio_data.append("    TYPE_VIN_NTC,")
                elif vin.get("type") == "vin_ads1115":
                    rio_data.append("    TYPE_VIN_ADC,")
                elif vin.get("type") == "vin_sonar":
                    rio_data.append("    TYPE_VIN_SONAR,")
                elif vin.get("type") == "vin_ds18b20":
                    rio_data.append("    TYPE_VIN_DS18B20,")
                elif vin.get("type") == "vin_max6675":
                    rio_data.append("    TYPE_VIN_MAX6675,")
                elif vin.get("type") in ("vin_quadencoder", "vin_quadencoderz"):
                    rio_data.append("    TYPE_VIN_ENCODER,")
                else:
                    rio_data.append("    TYPE_VIN_RAW,")
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char vin_names[][32] = {")
    for bitsize, num in vinBits.items():
        for num in range(project["vins"]):
            vin = project["vinnames"][num]
            dname = vin["_name"]
            bits = vin.get("_bits", 32)
            if bits == bitsize:
                rio_data.append(f'    "{dname}",')
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const uint8_t vin_bits[] = {")
    for bitsize, num in vinBits.items():
        for num in range(project["vins"]):
            vin = project["vinnames"][num]
            dname = vin["_name"]
            bits = vin.get("_bits", 32)
            if bits == bitsize:
                rio_data.append(f'    {bits},')
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char vout_names[][32] = {")
    for num in range(project["vouts"]):
        dname = project["voutnames"][num]["_name"]
        rio_data.append(f'    "{dname}",')
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char din_names[][32] = {")
    for num in range(project["dins"]):
        dname = project["dinnames"][num]["_name"]
        rio_data.append(f'    "{dname}",')
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char dout_names[][32] = {")
    for num in range(project["douts"]):
        dname = project["doutnames"][num]["_name"]
        rio_data.append(f'    "{dname}",')
    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char din_types[] = {")
    for num in range(project["dins"]):
        dname = project["dinnames"][num]["_name"]
        if dname.endswith("-index-enable-out"):
            rio_data.append("    DTYPE_INDEX,")
        else:
            rio_data.append("    DTYPE_IO,")

    rio_data.append("};")
    rio_data.append("")

    rio_data.append("const char dout_types[] = {")
    for num in range(project["douts"]):
        dname = project["doutnames"][num]["_name"]
        if dname.endswith("-index-enable"):
            rio_data.append("    DTYPE_INDEX,")
        else:
            rio_data.append("    DTYPE_IO,")
    rio_data.append("};")
    rio_data.append("")

    bout_inits = []
    for num, bout in enumerate(project["boutnames"]):
        for callback in bout["inits"]:
            bout_inits.append(f"    {callback}")
    if bout_inits:
        rio_data.append("#define BOUT_INITS \\")
        rio_data.append(" \\\n".join(bout_inits))
        rio_data.append("")

    bout_callbacks = []
    for num, bout in enumerate(project["boutnames"]):
        for callback in bout["callbacks"]:
            bout_callbacks.append(f"    {callback}")
    if bout_callbacks:
        rio_data.append("#define BOUT_CALLBACKS \\")
        rio_data.append(" \\\n".join(bout_callbacks))
        rio_data.append("")

    bin_callbacks = []
    for num, binname in enumerate(project["binnames"]):
        for callback in binname["callbacks"]:
            bin_callbacks.append(f"    {callback}")
    if bin_callbacks:
        rio_data.append("#define BIN_CALLBACKS \\")
        rio_data.append(" \\\n".join(bin_callbacks))
        rio_data.append("")

    open(f"{project['LINUXCNC_PATH']}/Components/rio.h", "w").write("\n".join(rio_data))

    os.system(
        f"cp -a generators/linuxcnc_component/*.c {project['LINUXCNC_PATH']}/Components/"
    )
    os.system(
        f"cp -a generators/linuxcnc_component/*.h {project['LINUXCNC_PATH']}/Components/"
    )
