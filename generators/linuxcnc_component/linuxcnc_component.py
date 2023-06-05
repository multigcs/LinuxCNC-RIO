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
        rio_data.append("#define UDP_IP \"192.168.10.132\"")
    elif transport == 'SERIAL':
        rio_data.append("#define TRANSPORT_SERIAL")
        rio_data.append("#define SERIAL_PORT \"/dev/ttyUSB0\"")
        rio_data.append("#define SERIAL_SPEED B2000000")
    elif transport == 'SPI':
        rio_data.append("#define TRANSPORT_SPI")
        rio_data.append("#define SPI_SPEED BCM2835_SPI_CLOCK_DIVIDER_128")
    else:
        print("ERROR: UNKNOWN transport protocol:", transport)
        sys.exit(1)
    rio_data.append("")
    rio_data.append(f"#define JOINTS               {project['joints']}")
    rio_data.append(f"#define JOINT_ENABLE_BYTES   {project['joints_en_total'] // 8}")
    rio_data.append(f"#define VARIABLE_OUTPUTS     {project['vouts']}")
    rio_data.append(f"#define VARIABLE_INPUTS      {project['vins']}")
    rio_data.append(f"#define VARIABLES            {max(project['vins'], project['vouts'])}")
    rio_data.append(f"#define DIGITAL_OUTPUTS      {project['douts_total']}")
    rio_data.append(f"#define DIGITAL_OUTPUT_BYTES {project['douts_total'] // 8}")
    rio_data.append(f"#define DIGITAL_INPUTS       {project['dins_total']}")
    rio_data.append(f"#define DIGITAL_INPUT_BYTES  {project['dins_total'] // 8}")
    rio_data.append(f"#define SPIBUFSIZE           {project['data_size'] // 8}")
    rio_data.append("")
    rio_data.append("#define PRU_DATA            0x64617461")
    rio_data.append("#define PRU_READ            0x72656164")
    rio_data.append("#define PRU_WRITE           0x77726974")
    rio_data.append("#define PRU_ESTOP           0x65737470")
    rio_data.append("#define STEPBIT             22")
    rio_data.append("#define STEP_MASK           (1L<<STEPBIT)")
    rio_data.append("#define STEP_OFFSET         (1L<<(STEPBIT-1))")
    rio_data.append(f"#define PRU_BASEFREQ        20000000")
    rio_data.append(f"#define PRU_OSC             {project['jdata']['clock']['speed']}")
    rio_data.append("")

    rio_data.append("#define VOUT_TYPE_PWM  0")
    rio_data.append("#define VOUT_TYPE_RCSERVO 1")
    rio_data.append("#define VOUT_TYPE_SINE 2")
    rio_data.append("#define VOUT_TYPE_FREQ 3")
    rio_data.append("#define VOUT_TYPE_UDPOTI 4")

    rio_data.append("#define JOINT_FB_REL 0")
    rio_data.append("#define JOINT_FB_ABS 1")

    rio_data.append("#define JOINT_STEPPER 0")
    rio_data.append("#define JOINT_RCSERVO 1")
    rio_data.append("#define JOINT_PWMDIR  2")

    vouts_min = []
    vouts_max = []
    vouts_type = []
    vouts_freq = []
    for vout in project['jdata']["vout"]:
        freq = vout.get('freq', 10000)
        if vout.get('type') == "sine":
            vouts_min.append(str(vout.get("min", -100)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append("30")
        elif vout.get('type') == "pwm":
            vouts_min.append(str(vout.get("min", -100)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append(str(vout.get("freq", freq)))
        elif vout.get('type') == "rcservo":
            freq = vout.get('freq', 100)
            vouts_min.append(str(vout.get("min", -100)))
            vouts_max.append(str(vout.get("max", 100.0)))
            vouts_freq.append(str(vout.get("freq", freq)))
        else:
            vouts_min.append(str(vout.get("min", 0)))
            vouts_max.append(str(vout.get("max", 10.0)))
            vouts_freq.append(str(vout.get("freq", freq)))
        vouts_type.append(f"VOUT_TYPE_{vout.get('type', 'freq').upper()}")

    rio_data.append(f"float vout_min[VARIABLE_OUTPUTS] = {{{', '.join(vouts_min)}}};")
    rio_data.append(f"float vout_max[VARIABLE_OUTPUTS] = {{{', '.join(vouts_max)}}};")
    rio_data.append(f"float vout_freq[VARIABLE_OUTPUTS] = {{{', '.join(vouts_freq)}}};")
    rio_data.append(f"uint8_t vout_type[VARIABLE_OUTPUTS] = {{{', '.join(vouts_type)}}};")
    rio_data.append("")

    joints_fb_type = []
    for num, joint in enumerate(project['jdata']["joints"]):
        if joint.get('type') == "rcservo":
            joints_fb_type.append("JOINT_FB_ABS")
        else:
            joints_fb_type.append("JOINT_FB_REL")
    rio_data.append(f"uint8_t joints_fb_type[JOINTS] = {{{', '.join(joints_fb_type)}}};")
    rio_data.append("")

    joints_type = []
    for num, joint in enumerate(project['jdata']["joints"]):
        if joint.get('type') == "rcservo":
            joints_type.append("JOINT_RCSERVO")
        elif joint.get('type') == "pwmdir":
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
    open(f"{project['LINUXCNC_PATH']}/Components/rio.h", "w").write("\n".join(rio_data))




    rio_data = []

    rio_data.append("""
enum {
    OUTTYPE_JOINT,
    OUTTYPE_JOINT_ENABLE,
    OUTTYPE_VARIABLE,
    OUTTYPE_BIT,
};

enum {
    OUTCALC_PWM,
    OUTCALC_RCSERVO,
    OUTCALC_FREQUENCY,
    OUTCALC_LINEAR,
};

enum {
    INTYPE_JOINT_FB,
    INTYPE_VARIABLE,
    INTYPE_BIT,
};
""")
    rio_data.append("")

    rio_data.append(f"#define BUFFERSIZE {(32 + project['total_inout']) // 8}")
    rio_data.append("")
    for vsize in project["variables_out"]:
        rio_data.append(f"#define OUTPUTS_{vsize}BIT {len(project['variables_out'][vsize])}")
    for vsize in project["variables_in"]:
        rio_data.append(f"#define INPUTS_{vsize}BIT  {len(project['variables_in'][vsize])}")
    rio_data.append(f"#define OUTPUTS_BITMASK {project['onebit_out']}")
    rio_data.append(f"#define INPUTS_BITMASK  {project['onebit_in']}")
    rio_data.append("")

    output_types = []
    for outp in project["variables_out"].get(32, []):
        output_types.append(f"OUTTYPE_{outp.get('type')}")

    output_calcs = []
    for outp in project["variables_out"].get(32, []):
        output_calcs.append(f"OUTCALC_{outp.get('calc')}")

    input_types = []
    for inp in project["variables_in"].get(32, []):
        input_types.append(f"{inp.get('dir')}TYPE_{inp.get('type')}")

    output_variable_nums = []
    for outp in project["variables_out"].get(32, []):
        output_variable_nums.append(f"{outp.get('joint', outp.get('vout', -1))}")

    input_variable_nums = []
    for inp in project["variables_in"].get(32, []):
        input_variable_nums.append(f"{inp.get('joint', inp.get('vin', -1))}")

    output_bittypes = []
    for outp in project["variables_out"].get(1, []):
        output_bittypes.append(f"{outp.get('dir')}TYPE_{outp.get('type')}")

    input_bittypes = []
    for inp in project["variables_in"].get(1, []):
        input_bittypes.append(f"{inp.get('dir')}TYPE_{inp.get('type')}")

    output_bit_nums = []
    for outp in project["variables_out"].get(1, []):
        output_bit_nums.append(f"{outp.get('joint', outp.get('dout', -1))}")

    input_bit_nums = []
    for inp in project["variables_in"].get(1, []):
        input_bit_nums.append(f"{inp.get('joint', inp.get('din', -1))}")

    rio_data.append(f"uint8_t out_variable_types[] = {{{', '.join(output_types)}}};")
    rio_data.append(f"uint8_t out_variable_calcs[] = {{{', '.join(output_calcs)}}};")
    rio_data.append(f"uint8_t in_variable_types[] = {{{', '.join(input_types)}}};")
    rio_data.append(f"uint8_t out_bit_types[] = {{{', '.join(output_bittypes)}}};")
    rio_data.append(f"uint8_t in_bit_types[] = {{{', '.join(input_bittypes)}}};")
    rio_data.append("")

    rio_data.append(f"int8_t out_variable_nums[] = {{{', '.join(output_variable_nums)}}};")
    rio_data.append(f"int8_t in_variable_nums[] = {{{', '.join(input_variable_nums)}}};")
    rio_data.append(f"int8_t out_bit_nums[] = {{{', '.join(output_bit_nums)}}};")
    rio_data.append(f"int8_t in_bit_joints[] = {{{', '.join(input_bit_nums)}}};")
    rio_data.append("")


    rio_data.append("""
typedef union {
    struct {
        uint8_t txBuffer[BUFFERSIZE];
    };
    struct {
        int32_t header;""")

    if len(project["variables_out"].get(32)) > 0:
        rio_data.append(f"        int32_t out_variables[OUTPUTS_32BIT];")
    if project["onebit_out"] > 0:
        rio_data.append(f"        uint8_t out_bitmasks[OUTPUTS_BITMASK];")

    rio_data.append("""    };
} txData_t;
""")


    rio_data.append("""
typedef union {
    struct {
        uint8_t rxBuffer[BUFFERSIZE];
    };
    struct {
        int32_t header;""")

    if len(project["variables_in"].get(32)) > 0:
        rio_data.append(f"        int32_t in_variables[INPUTS_32BIT];")
    if project["onebit_in"] > 0:
        rio_data.append(f"        uint8_t in_bitmasks[INPUTS_BITMASK];")

    rio_data.append("""    };
} rxData_t;
""")


    rio_data.append("")
    open(f"{project['LINUXCNC_PATH']}/Components/_new_rio.h", "w").write("\n".join(rio_data))



    os.system(f"cp -a generators/linuxcnc_component/*.c {project['LINUXCNC_PATH']}/Components/")
    os.system(f"cp -a generators/linuxcnc_component/*.h {project['LINUXCNC_PATH']}/Components/")
