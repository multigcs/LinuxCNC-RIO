import os

def generate(project):
    print("generating linux-cnc config")

    cfgini_data = []

    axis_names = ["X", "Y", "Z", "A", "C", "B", "U", "V", "W"]
    axis_str = ""
    axis_str2 = ""
    for num in range(min(project['joints'], len(axis_names))):
        axis_str += axis_names[num]
        axis_str2 += " " + axis_names[num]


    cfgini_data.append(f"""
# Basic LinuxCNC config for testing of RIO firmware

[EMC]
MACHINE = Rio-XYZAC
DEBUG = 0
VERSION = 1.1

[DISPLAY]
PYVCP = port-tester.xml
DISPLAY = axis
EDITOR = gedit
POSITION_OFFSET = RELATIVE
POSITION_FEEDBACK = ACTUAL
ARCDIVISION = 64
GRIDS = 10mm 20mm 50mm 100mm
MAX_FEED_OVERRIDE = 5.0
MIN_SPINDLE_OVERRIDE = 0.5
MAX_SPINDLE_OVERRIDE = 1.2
INTRO_GRAPHIC = linuxcnc.gif
INTRO_TIME = 5
PROGRAM_PREFIX = ~/linuxcnc/nc_files
INCREMENTS = 50mm 10mm 5mm 1mm .5mm .1mm .05mm .01mm

MIN_LINEAR_VELOCITY = 0
DEFAULT_LINEAR_VELOCITY = 10.0
MAX_LINEAR_VELOCITY = 40.0

DEFAULT_ANGULAR_VELOCITY = 5.0
MIN_ANGULAR_VELOCITY = 0
MAX_ANGULAR_VELOCITY = 5


[KINS]
JOINTS = {project['joints']}
#KINEMATICS =trivkins coordinates={axis_str} kinstype=BOTH
KINEMATICS =trivkins coordinates={axis_str}

[FILTER]
PROGRAM_EXTENSION = .py Python Script
py = python

[TASK]
TASK = milltask
CYCLE_TIME = 0.010

[RS274NGC]
PARAMETER_FILE = linuxcnc.var

[EMCMOT]
EMCMOT = motmod
COMM_TIMEOUT = 1.0
COMM_WAIT = 0.010
BASE_PERIOD = 0
SERVO_PERIOD = 1000000

[HAL]
HALFILE = rio.hal
POSTGUI_HALFILE = postgui_call_list.hal

[TRAJ]
COORDINATES =  {axis_str2}
LINEAR_UNITS = mm
ANGULAR_UNITS = degree
CYCLE_TIME = 0.010
DEFAULT_LINEAR_VELOCITY = 50.00
MAX_LINEAR_VELOCITY = 50.00
NO_FORCE_HOMING = 1 

[EMCIO]
EMCIO = io
CYCLE_TIME = 0.100
TOOL_TABLE = tool.tbl

    """)

    for num, joint in enumerate(project['jdata']["joints"]):
        if joint.get("type") == "rcservo":
            SCALE = 80.0
            MIN_LIMIT = -110
            MAX_LIMIT = 110
        else:
            if num > 2:
                SCALE = 223.0
                MIN_LIMIT = -360
                MAX_LIMIT = 360
            else:
                SCALE = 800.0
                MIN_LIMIT = -1300
                MAX_LIMIT = 1300

        OUTPUT_SCALE = joint.get("scale", SCALE)
        INPUT_SCALE = joint.get("enc_scale", OUTPUT_SCALE)
        MIN_LIMIT = joint.get("min_limit", MIN_LIMIT)
        MAX_LIMIT = joint.get("max_limit", MAX_LIMIT)
        cfgini_data.append(f"[AXIS_{axis_names[num]}]")

        if num > 2:
            cfgini_data.append(f"""MAX_VELOCITY = 50
MAX_ACCELERATION = 400.0
MIN_LIMIT = {MIN_LIMIT}
MAX_LIMIT = {MAX_LIMIT}

""")
        else:
            cfgini_data.append(f"""MAX_VELOCITY = 50
MAX_ACCELERATION = 400.0
MIN_LIMIT = {MIN_LIMIT}
MAX_LIMIT = {MAX_LIMIT}

""")

        cfgini_data.append(f"[JOINT_{num}]")
        scales = f"SCALE = {OUTPUT_SCALE}"

        if joint.get("cl", False):
            for key, default in {
                "P": "1",
                "I": "0.0",
                "D": "0.0",
                "FF0": "0.0",
                "FF1": "1.00025",
                "FF2": "0.01",
                "BIAS": "0.0",
                "DEADBAND": "2.0",
            }.items():
                value = joint.get("pid", {}).get(key, default)
                cfgini_data.append(f"{key} = {value}")

            scales = f"OUTPUT_SCALE = {OUTPUT_SCALE}\nINPUT_SCALE = {INPUT_SCALE}"

        if num > 2:
            cfgini_data.append(f"""
TYPE = ANGULAR
MIN_LIMIT = {MIN_LIMIT}
MAX_LIMIT = {MAX_LIMIT}
MAX_VELOCITY = 50.0
MAX_ACCELERATION = 20.0
STEPGEN_MAXACCEL = 4000.0
{scales}
FERROR = 1.0
MIN_FERROR = 0.5

HOME_OFFSET = 0.0
HOME_SEARCH_VEL = 0
HOME_LATCH_VEL = 0
HOME_SEQUENCE = 0

#HOME_SEARCH_VEL = 20.0
#HOME_LATCH_VEL = 3.0
#HOME_FINAL_VEL = -20
#HOME_IGNORE_LIMITS = YES
#HOME_USE_INDEX = NO
#HOME_OFFSET = 6.5
#HOME = 0.0
#HOME_SEQUENCE = 4

""")
        else:
            cfgini_data.append(f"""
TYPE = LINEAR
MIN_LIMIT = {MIN_LIMIT}
MAX_LIMIT = {MAX_LIMIT}
MAX_VELOCITY = 50.0
MAX_ACCELERATION = 20.0
STEPGEN_MAXACCEL = 4000.0
{scales}
FERROR = 1.0
MIN_FERROR = 0.5

HOME_OFFSET = 0.0
HOME_SEARCH_VEL = 0
HOME_LATCH_VEL = 0
HOME_SEQUENCE = 0

#HOME_SEARCH_VEL = 20.0
#HOME_LATCH_VEL = 3.0
#HOME_FINAL_VEL = -20
#HOME_IGNORE_LIMITS = YES
#HOME_USE_INDEX = NO
#HOME_OFFSET = 6.5
#HOME = 0.0
#HOME_SEQUENCE = 4

""")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio.ini", "w").write("\n".join(cfgini_data))

    cfghal_data = []
    ctrl_types = []

    num_pids = 0
    for num, joint in enumerate(project['jdata']["joints"]):
        if joint.get("cl", False):
            num_pids += 1
            ctrl_types.append("v") # velocity mode
        else:
            ctrl_types.append("p") # position mode
    
    cfghal_data.append(f"""
# load the realtime components
loadrt [KINS]KINEMATICS
loadrt [EMCMOT]EMCMOT base_period_nsec=[EMCMOT]BASE_PERIOD servo_period_nsec=[EMCMOT]SERVO_PERIOD num_joints=[KINS]JOINTS

loadrt rio ctrl_type={','.join(ctrl_types)}

# estop loopback, SPI comms enable and feedback
net user-enable-out 	<= iocontrol.0.user-enable-out		=> rio.SPI-enable
net user-request-enable <= iocontrol.0.user-request-enable	=> rio.SPI-reset
net rio-status 	<= rio.SPI-status 			=> iocontrol.0.emc-enable-in

# add the rio and motion functions to threads
addf motion-command-handler servo-thread
addf motion-controller servo-thread
addf rio.update-freq servo-thread
addf rio.readwrite servo-thread

    """)

    if num_pids > 0:
        cfghal_data.append(f"loadrt pid num_chan={num_pids}")
        for pidn in range(num_pids):
            cfghal_data.append(f"addf pid.{pidn}.do-pid-calcs        servo-thread")
    cfghal_data.append("")

    for num, vout in enumerate(project['jdata']["vout"]):
        vname = f"SP.{num}"
        vout_name = vout.get("name", vname)
        vout_net = vout.get("net")
        if vout_net:
            cfghal_data.append(f"net {vout_name} <= {vout_net}")
            cfghal_data.append(f"net {vout_name} => rio.{vname}")
    cfghal_data.append("")

    for num, din in enumerate(project['jdata']["din"]):
        dname = project['dinnames'][num].lower()
        invert = din.get("invert", False)
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            cfghal_data.append(f"net {din_name} <= rio.{dname}")
            cfghal_data.append(f"net {din_name} => {din_net}")
        elif din_type == "alarm" and din_joint:
            cfghal_data.append(f"net din{num} joint.{din_joint}.amp-fault-in <= rio.{dname}")
        elif din_type == "home" and din_joint:
            cfghal_data.append(f"net home-{axis_names[int(din_joint)].lower()} <= rio.{dname}")
            cfghal_data.append(f"net home-{axis_names[int(din_joint)].lower()} => joint.{din_joint}.home-sw-in")
        elif din_type == "probe":
            cfghal_data.append(f"net toolprobe <= rio.input.{dname}")
            cfghal_data.append(f"net toolprobe => motion.probe-input")
    cfghal_data.append("")

    for num, dout in enumerate(project['jdata']["dout"]):
        dname = project['doutnames'][num].lower()
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            cfghal_data.append(f"net {dout_name} <= {dout_net}")
            cfghal_data.append(f"net {dout_name} => rio.{dname}")
    cfghal_data.append("")

    pidn = 0
    for num, joint in enumerate(project['jdata']["joints"]):
        if joint.get("cl", False):
            cfghal_data.append(f"""# Joint {num} setup

setp pid.{pidn}.maxoutput 300
setp pid.{pidn}.Pgain [JOINT_{num}]P
setp pid.{pidn}.Igain [JOINT_{num}]I
setp pid.{pidn}.Dgain [JOINT_{num}]D
setp pid.{pidn}.bias [JOINT_{num}]BIAS
setp pid.{pidn}.FF0 [JOINT_{num}]FF0
setp pid.{pidn}.FF1 [JOINT_{num}]FF1
setp pid.{pidn}.FF2 [JOINT_{num}]FF2
setp pid.{pidn}.deadband [JOINT_{num}]DEADBAND

setp rio.joint.{num}.scale 		[JOINT_{num}]OUTPUT_SCALE
setp rio.joint.{num}.fb-scale 	[JOINT_{num}]INPUT_SCALE
setp rio.joint.{num}.maxaccel 	[JOINT_{num}]STEPGEN_MAXACCEL

net {axis_names[num].lower()}vel-cmd 		<= pid.{pidn}.output 	=> rio.joint.{num}.vel-cmd  
net {axis_names[num].lower()}pos-cmd 		<= joint.{num}.motor-pos-cmd 	=> pid.{pidn}.command
net j{num}pos-fb 		<= rio.joint.{num}.pos-fb 	=> joint.{num}.motor-pos-fb
net j{num}pos-fb 		=> pid.{pidn}.feedback

net j{num}enable 		<= joint.{num}.amp-enable-out 	=> rio.joint.{num}.enable
net j{num}enable 		=> pid.{pidn}.enable

""")

            pidn += 1
        else:


            cfghal_data.append(f"""# Joint {num} setup

setp rio.joint.{num}.scale 		[JOINT_{num}]SCALE
setp rio.joint.{num}.maxaccel 	[JOINT_{num}]STEPGEN_MAXACCEL

net {axis_names[num].lower()}pos-cmd 		<= joint.{num}.motor-pos-cmd 	=> rio.joint.{num}.pos-cmd  
net j{num}pos-fb 		<= rio.joint.{num}.pos-fb 	=> joint.{num}.motor-pos-fb
net j{num}enable 		<= joint.{num}.amp-enable-out 	=> rio.joint.{num}.enable

""")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio.hal", "w").write("\n".join(cfghal_data))



    cfghal_data = []
    cfghal_data.append("loadrt rio")
    cfghal_data.append("loadusr -Wn ptest pyvcp -c ptest port-tester.xml")
    cfghal_data.append("loadrt threads name1=porttest period1=1000000")
    cfghal_data.append("addf rio.readwrite porttest")
    cfghal_data.append("")

    for num in range(project['dins']):
        dname = project['dinnames'][num]
        if not dname.endswith("INDEX_OUT"):
            cfghal_data.append(f"net {dname.lower()} rio.{dname} ptest.led-in{num}")


    for num, vout in enumerate(project['jdata']["vout"]):
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        if vout_net:
            continue
        cfghal_data.append(f"net vout{num} ptest.vout{num}-f rio.SP.{num}")

    cfghal_data.append("start")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/port-tester.hal", "w").write("\n".join(cfghal_data))



    cfghal_data = []
    cfghal_data.append("")

    for num in range(project['douts']):
        dname = project['doutnames'][num].lower()
        dout = {}
        if dname.startswith("dout"):
            dout = project['jdata']["dout"][num]
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            pass
        elif not dname.endswith("INDEX_ENABLE"):
            cfghal_data.append(f"net {dname.lower()} pyvcp.btn{num} rio.{dname}")

    for num in range(project['dins']):
        dname = project['dinnames'][num]
        din = {}
        if dname.startswith("DIN"):
            din = project['jdata']["din"][num]
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            pass
        elif din_type == "alarm" and din_joint:
            pass
        elif din_type == "home" and din_joint:
            pass
        elif not dname.endswith("INDEX_OUT"):
            cfghal_data.append(f"net {dname.lower()} rio.{dname.lower()} pyvcp.led-in{num}")

    for num, vout in enumerate(project['jdata']["vout"]):
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        if vout_net:
            continue
        cfghal_data.append(f"net vout{num} pyvcp.vout{num}-f rio.SP.{num}")

    for num in range(project['vins']):
        cfghal_data.append(f"net vin{num} rio.PV.{num} pyvcp.vin{num}")

    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/custom_postgui.hal", "w").write("\n".join(cfghal_data))




    cfgxml_data = []
    cfgxml_data.append("<pyvcp>")


    cfgxml_data.append("  <hbox>")
    cfgxml_data.append("    <relief>RIDGE</relief>")
    cfgxml_data.append("    <bd>2</bd>")
    cfgxml_data.append("    <label>")
    cfgxml_data.append(f"      <text>\"DOUT\"</text>")
    cfgxml_data.append("      <font>(\"Helvetica\",12)</font>")
    cfgxml_data.append("    </label>")

    for num in range(project['douts']):
        dname = project['doutnames'][num]
        dout = {}
        if dname.startswith("DOUT"):
            dout = project['jdata']["dout"][num]
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            continue
        elif dname.endswith("INDEX_ENABLE"):
            continue
        cfgxml_data.append("    <checkbutton>")
        cfgxml_data.append(f"      <halpin>\"btn{num}\"</halpin>")
        cfgxml_data.append(f"      <text>\"{num}\"</text>")
        cfgxml_data.append("    </checkbutton>")
        if (num+1) % 8 == 0 and num+1 < project['douts']:
            cfgxml_data.append("  </hbox>")
            cfgxml_data.append("  <hbox>")
            cfgxml_data.append("    <relief>RIDGE</relief>")
            cfgxml_data.append("    <bd>2</bd>")
            cfgxml_data.append("    <label>")
            cfgxml_data.append(f"      <text>\"DOUT\"</text>")
            cfgxml_data.append("      <font>(\"Helvetica\",12)</font>")
            cfgxml_data.append("    </label>")
    cfgxml_data.append("  </hbox>")

    cfgxml_data.append("  <hbox>")
    cfgxml_data.append("    <relief>RIDGE</relief>")
    cfgxml_data.append("    <bd>2</bd>")
    cfgxml_data.append("    <label>")
    cfgxml_data.append(f"      <text>\"DIN\"</text>")
    cfgxml_data.append("      <font>(\"Helvetica\",12)</font>")
    cfgxml_data.append("    </label>")

    for num in range(project['dins']):
        dname = project['dinnames'][num]
        if dname.endswith("INDEX_OUT"):
            continue
        din = {}
        if dname.startswith("DIN"):
            din = project['jdata']["din"][num]

        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            pass
        elif din_type == "alarm" and din_joint:
            pass
        elif din_type == "home" and din_joint:
            pass
        else:
            cfgxml_data.append("    <led>")
            cfgxml_data.append(f"      <halpin>\"led-in{num}\"</halpin>")
            cfgxml_data.append("      <size>25</size>")
            cfgxml_data.append("      <on_color>\"green\"</on_color>")
            cfgxml_data.append("      <off_color>\"red\"</off_color>")
            cfgxml_data.append("    </led>")

            if (num+1) % 8 == 0 and num+1 < project['dins']:
                cfgxml_data.append("  </hbox>")
                cfgxml_data.append("  <hbox>")
                cfgxml_data.append("    <relief>RIDGE</relief>")
                cfgxml_data.append("    <bd>2</bd>")
                cfgxml_data.append("    <label>")
                cfgxml_data.append(f"      <text>\"DIN\"</text>")
                cfgxml_data.append("      <font>(\"Helvetica\",12)</font>")
                cfgxml_data.append("    </label>")

    cfgxml_data.append("  </hbox>")

    for num, vout in enumerate(project['jdata']["vout"]):
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        if vout_net:
            continue

        cfgxml_data.append("  <scale>")
        cfgxml_data.append("    <font>(\"Helvetica\",12)</font>")
        cfgxml_data.append("    <width>\"25\"</width>")
        cfgxml_data.append(f"    <halpin>\"vout{num}\"</halpin>")
        cfgxml_data.append("    <resolution>0.1</resolution>")
        cfgxml_data.append("    <orient>HORIZONTAL</orient>")
        cfgxml_data.append("    <initval>0</initval>")

        if vout.get('type') == "sine":
            cfgxml_data.append(f"    <min_>{str(vout.get('min', -100))}</min_>")
            cfgxml_data.append(f"    <max_>{str(vout.get('max', 100))}</max_>")
        elif vout.get('type') == "pwm":
            if "dir" in vout:
                cfgxml_data.append(f"    <min_>{str(vout.get('min', -100))}</min_>")
            else:
                cfgxml_data.append(f"    <min_>{str(vout.get('min', 0))}</min_>")
            cfgxml_data.append(f"    <max_>{str(vout.get('max', 100))}</max_>")
        elif vout.get('type') == "rcservo":
            cfgxml_data.append(f"    <min_>{str(vout.get('min', -100))}</min_>")
            cfgxml_data.append(f"    <max_>{str(vout.get('max', 100))}</max_>")
        else:
            cfgxml_data.append(f"    <min_>{str(vout.get('min', 0))}</min_>")
            cfgxml_data.append(f"    <max_>{str(vout.get('max', 10))}</max_>")

        cfgxml_data.append("    <param_pin>1</param_pin>")
        cfgxml_data.append("  </scale>")

    for num, vin in enumerate(project['jdata']["vin"]):

        if False:
            cfgxml_data.append("<meter>")
            cfgxml_data.append(f"    <halpin>\"vin{num}\"</halpin>")
            cfgxml_data.append(f"    <text>\"VIN{num}\"</text>")
            cfgxml_data.append(f"    <subtext>\"{vin.get('type', '-')}\"</subtext>")
            cfgxml_data.append("    <size>150</size>")
            cfgxml_data.append("    <min_>-32800</min_>")
            cfgxml_data.append("    <max_>32800</max_>")
            cfgxml_data.append("    <majorscale>10000</majorscale>")
            cfgxml_data.append("    <minorscale>1000</minorscale>")
            cfgxml_data.append("    <region1>(-32800,0,\"red\")</region1>")
            cfgxml_data.append("    <region2>(0,32800,\"green\")</region2>")
            cfgxml_data.append("</meter>")
        elif False:
            cfgxml_data.append("<bar>")
            cfgxml_data.append(f"    <halpin>\"vin{num}\"</halpin>")
            cfgxml_data.append("    <min_>-32800</min_>")
            cfgxml_data.append("    <max_>32800</max_>")
            cfgxml_data.append("    <format>\"05d\"</format>")
            cfgxml_data.append("    <bgcolor>\"grey\"</bgcolor>")
            cfgxml_data.append("    <fillcolor>\"red\"</fillcolor>")
            cfgxml_data.append("    <range1>0,100,\"green\"</range1>")
            cfgxml_data.append("    <range2>101,135,\"orange\"</range2>")
            cfgxml_data.append("    <range3>136, 150,\"red\"</range3>")
            cfgxml_data.append("    <canvas_width>200</canvas_width>")
            cfgxml_data.append("    <canvas_height>50</canvas_height>")
            cfgxml_data.append("    <bar_height>30</bar_height>")
            cfgxml_data.append("    <bar_width>150</bar_width>")
            cfgxml_data.append("</bar>")
        else:
            cfgxml_data.append("<number>")
            cfgxml_data.append(f"    <halpin>\"vin{num}\"</halpin>")
            cfgxml_data.append("    <font>(\"Helvetica\",24)</font>")
            cfgxml_data.append("    <format>\"05d\"</format>")
            cfgxml_data.append("</number>")

    cfgxml_data.append("</pyvcp>")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/port-tester.xml", "w").write("\n".join(cfgxml_data))

    os.system(f"cp -a generators/linuxcnc_config/linuxcnc.var {project['LINUXCNC_PATH']}/ConfigSamples/rio")
    os.system(f"cp -a generators/linuxcnc_config/postgui_call_list.hal {project['LINUXCNC_PATH']}/ConfigSamples/rio")
    os.system(f"cp -a generators/linuxcnc_config/tool.tbl {project['LINUXCNC_PATH']}/ConfigSamples/rio")

