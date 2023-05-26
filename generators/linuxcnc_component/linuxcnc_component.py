import os

def generate(project):
    print("generating linux-cnc component")

    rio_data = []
    rio_data.append("#ifndef RIO_H")
    rio_data.append("#define RIO_H")
    rio_data.append("")
    if project['jdata'].get('transport', 'SPI') == 'UDP':
        rio_data.append("#define TRANSPORT_UDP")
        rio_data.append("#define UDP_IP \"192.168.10.132\"")
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
    joints_fb_scale = []
    for num, joint in enumerate(project['jdata']["joints"]):
        if joint.get('type') == "rcservo":
            joints_fb_type.append("JOINT_FB_ABS")
            joints_fb_scale.append("1.0")
        elif joint["type"] == "stepper":
            joints_fb_type.append("JOINT_FB_REL")
            if joint.get("cl", False):
                joints_fb_scale.append(joint.get("enc_scale", 1))
            else:
                joints_fb_scale.append("1.0")
        else:
            joints_fb_type.append("JOINT_FB_REL")
            joints_fb_scale.append("1.0")

    rio_data.append(f"uint8_t joints_fb_type[JOINTS] = {{{', '.join(joints_fb_type)}}};")
    rio_data.append(f"uint8_t joints_fb_scale[JOINTS] = {{{', '.join(joints_fb_scale)}}};")

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

    os.system(f"cp -a generators/linuxcnc_component/*.c {project['LINUXCNC_PATH']}/Components/")
    os.system(f"cp -a generators/linuxcnc_component/*.h {project['LINUXCNC_PATH']}/Components/")
