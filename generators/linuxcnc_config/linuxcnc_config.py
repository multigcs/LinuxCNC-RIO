
import os
import sys

axis_names = ["X", "Y", "Z", "A", "C", "B", "U", "V", "W"]

class qtdragon():
    def draw_scale(self, name, halpin, vmin, vmax):
        cfgxml_data = []
        cfgxml_data.append('  <item>')
        cfgxml_data.append(f'   <layout class="QHBoxLayout" name="layl_{halpin}">')
        cfgxml_data.append('    <item>')
        cfgxml_data.append('     <widget class="QLabel" name="label_22">')
        cfgxml_data.append('      <property name="text">')
        cfgxml_data.append(f'       <string>{name}</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="indent">')
        cfgxml_data.append('       <number>4</number>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('     </widget>')
        cfgxml_data.append('    </item>')
        cfgxml_data.append('    <item>')
        cfgxml_data.append(f'     <widget class="Slider" name="{halpin}">')
        cfgxml_data.append('      <property name="maximum">')
        cfgxml_data.append('       <number>100</number>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="orientation">')
        cfgxml_data.append('       <enum>Qt::Horizontal</enum>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('     </widget>')
        cfgxml_data.append('    </item>')
        cfgxml_data.append('   </layout>')
        cfgxml_data.append('  </item>')
        return cfgxml_data

    def draw_meter(self, name, halpin, setup={}, vmin=0, vmax=100):
        display_min = setup.get("min", vmin)
        display_max = setup.get("max", vmax)
        display_subtext = setup.get("subtext", '')
        display_region = setup.get("region", [])
        display_size = setup.get("size", 150)
        cfgxml_data = []
        cfgxml_data.append('   <item>')
        cfgxml_data.append(f'       <widget class="Gauge" name="gauge_{halpin}">')
        cfgxml_data.append('        <property name="minimumSize">')
        cfgxml_data.append('         <size>')
        cfgxml_data.append('          <width>150</width>')
        cfgxml_data.append('          <height>150</height>')
        cfgxml_data.append('         </size>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="threshold" stdset="0">')
        cfgxml_data.append('         <number>50</number>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="num_ticks" stdset="0">')
        cfgxml_data.append('         <number>9</number>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="gauge_label" stdset="0">')
        cfgxml_data.append(f'         <string>{name}</string>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="zone1_color" stdset="0">')
        cfgxml_data.append('         <color>')
        cfgxml_data.append('          <red>0</red>')
        cfgxml_data.append('          <green>100</green>')
        cfgxml_data.append('          <blue>0</blue>')
        cfgxml_data.append('         </color>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="zone2_color" stdset="0">')
        cfgxml_data.append('         <color>')
        cfgxml_data.append('          <red>200</red>')
        cfgxml_data.append('          <green>0</green>')
        cfgxml_data.append('          <blue>0</blue>')
        cfgxml_data.append('         </color>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('      <property name="halpin_name" stdset="0">')
        cfgxml_data.append(f'       <string>{halpin}</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="halpin_option" stdset="0">')
        cfgxml_data.append('       <bool>true</bool>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('       </widget>')
        cfgxml_data.append('   </item>')
        return cfgxml_data

    def draw_bar(self, name, halpin, setup={}, vmin=0, vmax=100):
        display_min = setup.get("min", vmin)
        display_max = setup.get("max", vmax)
        display_range = setup.get("range", [])
        display_format = setup.get("format", "05d")
        display_fillcolor = setup.get("fillcolor", "red")
        display_bgcolor = setup.get("fillcolor", "grey")
        cfgxml_data = []
        return cfgxml_data

    def draw_number(self, name, halpin, setup={}):
        display_format = setup.get("size", "05.2f")
        cfgxml_data = []
        cfgxml_data.append('  <item>')
        cfgxml_data.append(f'   <layout class="QHBoxLayout" name="layl_{halpin}">')
        cfgxml_data.append('    <item>')
        cfgxml_data.append('     <widget class="QLabel" name="label_22">')
        cfgxml_data.append('      <property name="text">')
        cfgxml_data.append(f'       <string>{name}</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="indent">')
        cfgxml_data.append('       <number>4</number>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('     </widget>')
        cfgxml_data.append('    </item>')
        cfgxml_data.append('    <item>')
        cfgxml_data.append(f'     <widget class="HALLabel" name="{halpin}">')
        cfgxml_data.append('      <property name="sizePolicy">')
        cfgxml_data.append('       <sizepolicy hsizetype="Minimum" vsizetype="Fixed">')
        cfgxml_data.append('        <horstretch>0</horstretch>')
        cfgxml_data.append('        <verstretch>0</verstretch>')
        cfgxml_data.append('       </sizepolicy>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('     </widget>')
        cfgxml_data.append('    </item>')
        cfgxml_data.append('   </layout>')
        cfgxml_data.append('  </item>')
        return cfgxml_data

    def draw_checkbutton(self, name, halpin):
        cfgxml_data = []
        cfgxml_data.append('  <item>')
        cfgxml_data.append(f'   <layout class="QHBoxLayout" name="layl_{halpin}">')
        cfgxml_data.append('    <item>')
        cfgxml_data.append('     <widget class="QLabel" name="label_22">')
        cfgxml_data.append('      <property name="text">')
        cfgxml_data.append(f'       <string>{name}</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="indent">')
        cfgxml_data.append('       <number>4</number>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('     </widget>')
        cfgxml_data.append('    </item>')
        cfgxml_data.append('    <item>')
        cfgxml_data.append(f'     <widget class="CheckBox" name="{halpin}">')
        cfgxml_data.append('      <property name="text">')
        cfgxml_data.append('       <string></string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('     </widget>')
        cfgxml_data.append('    </item>')
        cfgxml_data.append('   </layout>')
        cfgxml_data.append('  </item>')
        return cfgxml_data

    def draw_led(self, name, halpin):
        cfgxml_data = []
        cfgxml_data.append('  <item>')
        cfgxml_data.append(f'   <layout class="QHBoxLayout" name="layl_{halpin}">')
        cfgxml_data.append('    <item>')
        cfgxml_data.append('     <widget class="QLabel" name="label_22">')
        cfgxml_data.append('      <property name="text">')
        cfgxml_data.append(f'       <string>{name}</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="indent">')
        cfgxml_data.append('       <number>4</number>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('     </widget>')
        cfgxml_data.append('    </item>')
        cfgxml_data.append('<item>')
        cfgxml_data.append(f' <widget class="LED" name="hal_{halpin}">')
        cfgxml_data.append('  <property name="sizePolicy">')
        cfgxml_data.append('   <sizepolicy hsizetype="Fixed" vsizetype="Fixed">')
        cfgxml_data.append('    <horstretch>0</horstretch>')
        cfgxml_data.append('    <verstretch>0</verstretch>')
        cfgxml_data.append('   </sizepolicy>')
        cfgxml_data.append('  </property>')
        cfgxml_data.append('  <property name="minimumSize">')
        cfgxml_data.append('   <size>')
        cfgxml_data.append('    <width>24</width>')
        cfgxml_data.append('    <height>24</height>')
        cfgxml_data.append('   </size>')
        cfgxml_data.append('  </property>')
        cfgxml_data.append('  <property name="maximumSize">')
        cfgxml_data.append('   <size>')
        cfgxml_data.append('    <width>24</width>')
        cfgxml_data.append('    <height>24</height>')
        cfgxml_data.append('   </size>')
        cfgxml_data.append('  </property>')
        cfgxml_data.append('  <property name="pin_name" stdset="0">')
        cfgxml_data.append(f'   <string>{halpin}</string>')
        cfgxml_data.append('  </property>')
        cfgxml_data.append('  <property name="diameter">')
        cfgxml_data.append('   <number>15</number>')
        cfgxml_data.append('  </property>')
        cfgxml_data.append('  <property name="color">')
        cfgxml_data.append('   <color>')
        cfgxml_data.append('    <red>0</red>')
        cfgxml_data.append('    <green>255</green>')
        cfgxml_data.append('    <blue>0</blue>')
        cfgxml_data.append('   </color>')
        cfgxml_data.append('  </property>')
        cfgxml_data.append('  <property name="off_color" stdset="0">')
        cfgxml_data.append('   <color>')
        cfgxml_data.append('    <red>0</red>')
        cfgxml_data.append('    <green>0</green>')
        cfgxml_data.append('    <blue>0</blue>')
        cfgxml_data.append('   </color>')
        cfgxml_data.append('  </property>')
        cfgxml_data.append(' </widget>')
        cfgxml_data.append('</item>')
        cfgxml_data.append('   </layout>')
        cfgxml_data.append('  </item>')
        return cfgxml_data

class axis():
    def draw_scale(self, name, halpin, vmin, vmax):
        cfgxml_data = []
        cfgxml_data.append("  <hbox>")
        cfgxml_data.append("    <relief>RAISED</relief>")
        cfgxml_data.append("    <bd>2</bd>")
        cfgxml_data.append("    <scale>")
        cfgxml_data.append(f'      <halpin>"{halpin}"</halpin>')
        cfgxml_data.append("      <resolution>0.1</resolution>")
        cfgxml_data.append("      <orient>HORIZONTAL</orient>")
        cfgxml_data.append("      <initval>0</initval>")
        cfgxml_data.append(f"      <min_>{vmin}</min_>")
        cfgxml_data.append(f"      <max_>{vmax}</max_>")
        cfgxml_data.append("      <param_pin>1</param_pin>")
        cfgxml_data.append("    </scale>")
        cfgxml_data.append("    <label>")
        cfgxml_data.append(f'      <text>"{name}"</text>')
        cfgxml_data.append("    </label>")
        cfgxml_data.append("  </hbox>")
        return cfgxml_data

    def draw_meter(self, name, halpin, setup={}, vmin=0, vmax=100):
        display_min = setup.get("min", vmin)
        display_max = setup.get("max", vmax)
        display_subtext = setup.get("subtext", '')
        display_region = setup.get("region", [])
        display_size = setup.get("size", 150)
        cfgxml_data = []
        cfgxml_data.append("  <hbox>")
        cfgxml_data.append("    <relief>RAISED</relief>")
        cfgxml_data.append("    <bd>2</bd>")
        cfgxml_data.append("  <meter>")
        cfgxml_data.append(f'      <halpin>"{halpin}"</halpin>')
        cfgxml_data.append(f'      <text>"{name}"</text>')
        cfgxml_data.append(f"      <subtext>\"{display_subtext}\"</subtext>")
        cfgxml_data.append(f"      <size>{display_size}</size>")
        cfgxml_data.append(f"      <min_>{display_min}</min_>")
        cfgxml_data.append(f"      <max_>{display_max}</max_>")
        for rnum, region in enumerate(display_region):
            cfgxml_data.append(f'      <region{rnum + 1}>({region[0]},{region[1]},"{region[2]}")</region{rnum + 1}>')
        cfgxml_data.append("    </meter>")
        cfgxml_data.append("  </hbox>")
        return cfgxml_data

    def draw_bar(self, name, halpin, setup={}, vmin=0, vmax=100):
        display_min = setup.get("min", vmin)
        display_max = setup.get("max", vmax)
        display_range = setup.get("range", [])
        display_format = setup.get("format", "05d")
        display_fillcolor = setup.get("fillcolor", "red")
        display_bgcolor = setup.get("fillcolor", "grey")
        cfgxml_data = []
        cfgxml_data.append("  <hbox>")
        cfgxml_data.append("    <relief>RAISED</relief>")
        cfgxml_data.append("    <bd>2</bd>")
        cfgxml_data.append("    <label>")
        cfgxml_data.append(f'      <text>"{name}"</text>')
        cfgxml_data.append("    </label>")
        cfgxml_data.append("    <bar>")
        cfgxml_data.append(f'    <halpin>"{halpin}"</halpin>')
        cfgxml_data.append(f"    <min_>{display_min}</min_>")
        cfgxml_data.append(f"    <max_>{display_max}</max_>")
        cfgxml_data.append(f'    <format>"{display_format}"</format>')
        cfgxml_data.append(f'    <bgcolor>"{display_bgcolor}"</bgcolor>')
        cfgxml_data.append(f'    <fillcolor>"{display_fillcolor}"</fillcolor>')
        for rnum, brange in enumerate(display_range):
            cfgxml_data.append(f'    <range{rnum + 1}>({brange[0]},{brange[1]},"{brange[2]}")</range{rnum + 1}>')
        cfgxml_data.append("    </bar>")
        cfgxml_data.append("  </hbox>")
        return cfgxml_data

    def draw_number(self, name, halpin, setup={}):
        display_format = setup.get("size", "05.2f")
        cfgxml_data = []
        cfgxml_data.append("  <hbox>")
        cfgxml_data.append("    <relief>RAISED</relief>")
        cfgxml_data.append("    <bd>2</bd>")
        cfgxml_data.append("    <label>")
        cfgxml_data.append(f'      <text>"{name}"</text>')
        cfgxml_data.append("    </label>")
        cfgxml_data.append("    <number>")
        cfgxml_data.append(f'        <halpin>"{halpin}"</halpin>')
        cfgxml_data.append('        <font>("Helvetica",18)</font>')
        cfgxml_data.append(f'        <format>"{display_format}"</format>')
        cfgxml_data.append("    </number>")
        cfgxml_data.append("  </hbox>")
        return cfgxml_data

    def draw_checkbutton(self, name, halpin):
        cfgxml_data = []
        cfgxml_data.append("  <hbox>")
        cfgxml_data.append("    <relief>RAISED</relief>")
        cfgxml_data.append("    <bd>2</bd>")
        cfgxml_data.append("    <checkbutton>")
        cfgxml_data.append(f'      <halpin>"{halpin}"</halpin>')
        cfgxml_data.append(f'      <text>"{name}"</text>')
        cfgxml_data.append("    </checkbutton>")
        cfgxml_data.append("  </hbox>")
        return cfgxml_data

    def draw_led(self, name, halpin):
        cfgxml_data = []
        cfgxml_data.append("  <hbox>")
        cfgxml_data.append("    <relief>RAISED</relief>")
        cfgxml_data.append("    <bd>2</bd>")
        cfgxml_data.append("    <led>")
        cfgxml_data.append(f'      <halpin>"{halpin}"</halpin>')
        cfgxml_data.append("      <size>10</size>")
        cfgxml_data.append('      <on_color>"green"</on_color>')
        cfgxml_data.append('      <off_color>"red"</off_color>')
        cfgxml_data.append("    </led>")
        cfgxml_data.append("    <label>")
        cfgxml_data.append(f'      <text>"{name}"</text>')
        cfgxml_data.append("    </label>")
        cfgxml_data.append("  </hbox>")
        return cfgxml_data



def generate_rio_ini(project):
    gui = project["jdata"].get("gui", "axis")
    limit_joints = int(project["jdata"].get("axis", 9))
    num_joints = min(project['joints'], limit_joints)
    netlist = []
    for num, din in enumerate(project["dinnames"]):
        din_net = din.get("net")
        if din_net:
            netlist.append(din_net)

    axis_str = ""
    axis_str2 = ""
    for num in range(min(project["joints"], len(axis_names))):
        # limit axis configurations
        if num >= num_joints:
            continue
        axis_str += axis_names[num]
        axis_str2 += " " + axis_names[num]

    if gui == "qtdragon":
        basic_setup = {
            "EMC": {
                "MACHINE": "Rio",
                "DEBUG": 0,
                "VERSION": 1.1,
            },
            "DISPLAY": {
                "DISPLAY": "qtvcp -d rio_hd",
                "TITLE": "LinuxCNC - RIO",
                "ICON": "silver_dragon.png",
                "EDITOR": None,
                "PYVCP": None,
                "PREFERENCE_FILE_PATH": "WORKINGFOLDER/qtdragon_hd.pref",
                "POSITION_OFFSET": "RELATIVE",
                "POSITION_FEEDBACK": "ACTUAL",
                "ARCDIVISION": 64,
                "GRIDS": "10mm 20mm 50mm 100mm",
                "INTRO_GRAPHIC": "silver_dragon.png",
                "INTRO_TIME": 2,
                "CYCLE_TIME": 100,
                "NGCGUI_SUBFILE_PATH": "../../../nc_files/ngcgui_lib/",
                "NGCGUI_SUBFILE": "qpocket.ngc",
                "MDI_HISTORY_FILE": "mdi_history.dat",
                "LOG_FILE": "qtdragon_hd.log",
                "PROGRAM_PREFIX": "~/linuxcnc/nc_files",
                "INCREMENTS": "50mm 10mm 5mm 1mm .5mm .1mm .05mm .01mm",
                "SPINDLE_INCREMENT": 200,
                "MAX_SPINDLE_POWER": 2000,
                "MAX_FEED_OVERRIDE": 5.0,
                "MIN_SPINDLE_0_OVERRIDE": 0.5,
                "MAX_SPINDLE_0_OVERRIDE": 1.2,
                "MIN_SPINDLE_0_SPEED": 1000,
                "DEFAULT_SPINDLE_0_SPEED": 5000,
                "MAX_SPINDLE_0_SPEED": 20000,
                "MIN_LINEAR_VELOCITY": 0.0,
                "DEFAULT_LINEAR_VELOCITY": 10.0,
                "MAX_LINEAR_VELOCITY": 40.0,
                "MIN_ANGULAR_VELOCITY": 0.0,
                "DEFAULT_ANGULAR_VELOCITY": 2.5,
                "MAX_ANGULAR_VELOCITY": 5.0,
            },
            "MDI_COMMAND_LIST": {
                "MDI_COMMAND": "G0 Z25 X0 Y0;Z0,Goto\\nZero",
                "MDI_COMMAND": "G53 G0 Z0;G53 G0 X0 Y0,Goto\\nMach\\nZero",
            },
            "FILTER": {
                "PROGRAM_EXTENSION": ".ngc,.nc,.tap G-Code File (*.ngc,*.nc,*.tap)",
                "PROGRAM_EXTENSION": ".png,.gif,.jpg Greyscale Depth Image",
                "PROGRAM_EXTENSION": ".py Python Script",
                "png": "image-to-gcode",
                "gif": "image-to-gcode",
                "jpg": "image-to-gcode",
                "py": "python3",
            },

            "KINS": {
                "JOINTS": num_joints,
                "KINEMATICS": f"trivkins coordinates={axis_str}",
            },
            "TASK": {
                "TASK": "milltask",
                "CYCLE_TIME": 0.010,
            },
            "RS274NGC": {
                "PARAMETER_FILE": "linuxcnc.var",
                "RS274NGC_STARTUP_CODE": "G17 G21 G40 G43H0 G54 G64P0.0127 G80 G90 G94 G97 M5 M9",
                "SUBROUTINE_PATH": "./subroutines/",
                "USER_M_PATH": "./mcodes/",
                "ON_ABORT_COMMAND": "O <on_abort> call",
            },
            "EMCMOT": {
                "EMCMOT": "motmod",
                "COMM_TIMEOUT": 1.0,
                "COMM_WAIT": 0.010,
                "BASE_PERIOD": 0,
                "SERVO_PERIOD": 1000000,
            },
            "HAL": {
                "HALFILE": "rio.hal",
                "POSTGUI_HALFILE": "postgui_call_list.hal",
                "HALUI": "halui",
            },
            "HALUI": {
            },
            "PROBE": {
                "USE_PROBE": "basicprobe",
            },
            "TRAJ": {
                "COORDINATES": axis_str2,
                "LINEAR_UNITS": "mm",
                "ANGULAR_UNITS": "degree",
                "CYCLE_TIME": 0.010,
                "DEFAULT_LINEAR_VELOCITY": 50.00,
                "MAX_LINEAR_VELOCITY": 50.00,
                "SPINDLES": 1,
                "NO_FORCE_HOMING": 1,
            },
            "EMCIO": {
                "EMCIO": "io",
                "CYCLE_TIME": 0.100,
                "TOOL_TABLE": "tool.tbl",
            },
        }
    else:
        basic_setup = {
            "EMC": {
                "MACHINE": "Rio",
                "DEBUG": 0,
                "VERSION": 1.1,
            },
            "DISPLAY": {
                "DISPLAY": "axis",
                "TITLE": "LinuxCNC - RIO",
                "ICON": None,
                "EDITOR": "gedit",
                "PYVCP": "rio-gui.xml",
                "PREFERENCE_FILE_PATH": None,
                "POSITION_OFFSET": "RELATIVE",
                "POSITION_FEEDBACK": "ACTUAL",
                "ARCDIVISION": 64,
                "GRIDS": "10mm 20mm 50mm 100mm",
                "INTRO_GRAPHIC": "linuxcnc.gif",
                "INTRO_TIME": 2,
                "PROGRAM_PREFIX": "~/linuxcnc/nc_files",
                "INCREMENTS": "50mm 10mm 5mm 1mm .5mm .1mm .05mm .01mm",
                "MAX_FEED_OVERRIDE": 5.0,
                "MIN_SPINDLE_0_OVERRIDE": 0.5,
                "MAX_SPINDLE_0_OVERRIDE": 1.2,
                "MIN_SPINDLE_0_SPEED": 1000,
                "DEFAULT_SPINDLE_0_SPEED": 5000,
                "MAX_SPINDLE_0_SPEED": 20000,
                "MIN_LINEAR_VELOCITY": 0.0,
                "DEFAULT_LINEAR_VELOCITY": 10.0,
                "MAX_LINEAR_VELOCITY": 40.0,
                "MIN_ANGULAR_VELOCITY": 0.0,
                "DEFAULT_ANGULAR_VELOCITY": 2.5,
                "MAX_ANGULAR_VELOCITY": 5.0,
            },
            "KINS": {
                "JOINTS": num_joints,
                "KINEMATICS": f"trivkins coordinates={axis_str}",
            },
            "FILTER": {
                "PROGRAM_EXTENSION": ".py Python Script",
                "py": "python",
            },
            "TASK": {
                "TASK": "milltask",
                "CYCLE_TIME": 0.010,
            },
            "RS274NGC": {
                "PARAMETER_FILE": "linuxcnc.var",
                "SUBROUTINE_PATH": "./subroutines/",
                "USER_M_PATH": "./mcodes/",
            },
            "EMCMOT": {
                "EMCMOT": "motmod",
                "COMM_TIMEOUT": 1.0,
                "COMM_WAIT": 0.010,
                "BASE_PERIOD": 0,
                "SERVO_PERIOD": 1000000,
            },
            "HAL": {
                "HALFILE": "rio.hal",
                "POSTGUI_HALFILE": "postgui_call_list.hal",
                "HALUI": "halui",
            },
            "HALUI": {
                "MDI_COMMAND": [
                    "G92 X0 Y0",
                    "G92 Z0",
                    "o<z_touch> call",
                ],
            },
            "TRAJ": {
                "COORDINATES": axis_str2,
                "LINEAR_UNITS": "mm",
                "ANGULAR_UNITS": "degree",
                "CYCLE_TIME": 0.010,
                "DEFAULT_LINEAR_VELOCITY": 50.00,
                "MAX_LINEAR_VELOCITY": 50.00,
                "NO_FORCE_HOMING": 1,
            },
            "EMCIO": {
                "EMCIO": "io",
                "CYCLE_TIME": 0.100,
                "TOOL_TABLE": "tool.tbl",
            },
        }


    cfgini_data = []
    cfgini_data.append("# Basic LinuxCNC config for testing RIO firmware")
    cfgini_data.append("")
    for section, setup in basic_setup.items():
        cfgini_data.append(f"[{section}]")
        for key, value in setup.items():
            if isinstance(value, list):
                for entry in value:
                    cfgini_data.append(f"{key} = {entry}")
            elif value != None:
                cfgini_data.append(f"{key} = {value}")
        cfgini_data.append("")


    for num, joint in enumerate(project["jointnames"]):
        # limit axis configurations
        if num >= num_joints:
            continue

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
        MAX_VELOCITY = joint.get("max_velocity", 40)
        MAX_ACCELERATION = joint.get("max_acceleration", 70)
        cfgini_data.append(f"[AXIS_{axis_names[num]}]")

        if num > 2:
            cfgini_data.append(
                f"""MAX_VELOCITY = {MAX_VELOCITY}
MAX_ACCELERATION = {MAX_ACCELERATION}
MIN_LIMIT = {MIN_LIMIT}
MAX_LIMIT = {MAX_LIMIT}
"""
            )
        else:
            cfgini_data.append(
                f"""MAX_VELOCITY = {MAX_VELOCITY}
MAX_ACCELERATION = {MAX_ACCELERATION}
MIN_LIMIT = {MIN_LIMIT}
MAX_LIMIT = {MAX_LIMIT}
"""
            )

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
            # rotary axis
            cfgini_data.append(
                f"""TYPE = ANGULAR
MIN_LIMIT = {MIN_LIMIT}
MAX_LIMIT = {MAX_LIMIT}
MAX_VELOCITY = {MAX_VELOCITY}
MAX_ACCELERATION = {MAX_ACCELERATION}
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

"""
            )
        else:
            cfgini_data.append(
                f"""TYPE = LINEAR
MIN_LIMIT = {MIN_LIMIT}
MAX_LIMIT = {MAX_LIMIT}
MAX_VELOCITY = {MAX_VELOCITY}
MAX_ACCELERATION = {MAX_ACCELERATION}
STEPGEN_MAXACCEL = 4000.0
{scales}
FERROR = 1.0
MIN_FERROR = 0.5
"""
            )

            HOME_SEQUENCE = 1
            if num == 2:
                HOME_SEQUENCE = 0

            if f"joint.{num}.home-sw-in" in netlist:
                REV = 1.0
                if OUTPUT_SCALE < 0:
                    REV = -1.0
                #if num == 2:
                #    REV *= -1.0

                options = {
                    "HOME_SEARCH_VEL": 10.0 * REV,
                    "HOME_LATCH_VEL": 3.0 * REV,
                    "HOME_FINAL_VEL": -5.0 * REV,
                    "HOME_IGNORE_LIMITS": "YES",
                    "HOME_USE_INDEX": "NO",
                    "HOME_OFFSET": 0.0,
                    "HOME": 0.0,
                    "HOME_SEQUENCE": HOME_SEQUENCE,
                }
            else:
                options = {
                    "HOME_OFFSET": "0.0",
                    "HOME_SEARCH_VEL": "0",
                    "HOME_LATCH_VEL": "0",
                    "HOME_SEQUENCE": "0",
                    "#HOME_SEARCH_VEL": 10.0,
                    "#HOME_LATCH_VEL": 3.0,
                    "#HOME_FINAL_VEL": -5.0,
                    "#HOME_IGNORE_LIMITS": "YES",
                    "#HOME_USE_INDEX": "NO",
                    "#HOME_OFFSET": 0.0,
                    "#HOME": 0.0,
                    "#HOME_SEQUENCE": 4,
                }

            for key, value in options.items():
                cfgini_data.append(f"{key} = {value}")

            cfgini_data.append("")

    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio.ini", "w").write(
        "\n".join(cfgini_data)
    )

def generate_rio_hal(project):
    netlist = []
    gui = project["jdata"].get("gui", "axis")
    limit_joints = int(project["jdata"].get("axis", 9))
    num_joints = min(project['joints'], limit_joints)

    axis_str = ""
    axis_str2 = ""
    for num in range(min(project["joints"], len(axis_names))):
        # limit axis configurations
        if num >= num_joints:
            continue
        axis_str += axis_names[num]
        axis_str2 += " " + axis_names[num]

    cfghal_data = []
    ctrl_types = []
    num_pids = 0
    for num, joint in enumerate(project["jointnames"]):
        if joint.get("cl", False):
            num_pids += 1
            ctrl_types.append("v")  # velocity mode
        else:
            ctrl_types.append("p")  # position mode

    cfghal_data.append(
        f"""
# load the realtime components
loadrt [KINS]KINEMATICS
loadrt [EMCMOT]EMCMOT base_period_nsec=[EMCMOT]BASE_PERIOD servo_period_nsec=[EMCMOT]SERVO_PERIOD num_joints=[KINS]JOINTS

# set joint modes (p=postion, v=velocity)
loadrt rio ctrl_type={','.join(ctrl_types)}

# add the rio and motion functions to threads
addf motion-command-handler servo-thread
addf motion-controller servo-thread
addf rio.update-freq servo-thread
addf rio.readwrite servo-thread

# estop loopback, SPI comms enable and feedback
net user-enable-out 	<= iocontrol.0.user-enable-out		=> rio.SPI-enable
net user-request-enable <= iocontrol.0.user-request-enable	=> rio.SPI-reset
"""
    )

    if "hy_vfd" in project["jdata"]:
        hy_vfd_dev = project["jdata"]["hy_vfd"]
        cfghal_data.append(f"loadusr -Wn vfd hy_vfd -n vfd -d {hy_vfd_dev} -p none -r 9600")
        cfghal_data.append("setp vfd.enable 1")
        cfghal_data.append("net spindle0_speed spindle.0.speed-out-abs => vfd.speed-command")
        cfghal_data.append("net spindle0_forward spindle.0.forward => vfd.spindle-forward")
        cfghal_data.append("net spindle0_reverse spindle.0.reverse => vfd.spindle-reverse")
        cfghal_data.append("net spindle0_on spindle.0.on => vfd.spindle-on")
        cfghal_data.append("")

    if project["jdata"].get("toolchange", "manual") == "manual":
        cfghal_data.append("loadusr -W hal_manualtoolchange")
        cfghal_data.append("net tool-change      hal_manualtoolchange.change   <=  iocontrol.0.tool-change")
        cfghal_data.append("net tool-changed     hal_manualtoolchange.changed  <=  iocontrol.0.tool-changed")
        cfghal_data.append("net tool-prep-number hal_manualtoolchange.number   <=  iocontrol.0.tool-prep-number")
        cfghal_data.append("net tool-prepare-loopback iocontrol.0.tool-prepare => iocontrol.0.tool-prepared")
        cfghal_data.append("")

    if num_pids > 0:
        cfghal_data.append(f"loadrt pid num_chan={num_pids}")
        for pidn in range(num_pids):
            cfghal_data.append(f"addf pid.{pidn}.do-pid-calcs        servo-thread")
            cfghal_data.append("")

    for num, vout in enumerate(project["voutnames"]):
        vname = vout['_name']
        vout_name = vout.get("name", vname)
        vout_net = vout.get("net")
        if vout_net:
            netlist.append(vout_net)
            cfghal_data.append(f"net {vout_name} <= {vout_net}")
            cfghal_data.append(f"net {vout_name} => rio.{vname}")
            cfghal_data.append("")

    for num, din in enumerate(project["dinnames"]):
        dname = project["dinnames"][num]['_name']
        invert = din.get("invert", False)
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            netlist.append(din_net)
            cfghal_data.append(f"net {din_name} <= rio.{dname}")
            cfghal_data.append(f"net {din_name} => {din_net}")
            cfghal_data.append("")
        elif din_type == "alarm" and din_joint:
            cfghal_data.append(
                f"net din{num} joint.{din_joint}.amp-fault-in <= rio.{dname}"
            )
            cfghal_data.append("")
        elif din_type == "home" and din_joint:
            netlist.append(f"joint.{din_joint}.home-sw-in")
            cfghal_data.append(
                f"net home-{axis_names[int(din_joint)].lower()} <= rio.{dname}"
            )
            cfghal_data.append(
                f"net home-{axis_names[int(din_joint)].lower()} => joint.{din_joint}.home-sw-in"
            )
            cfghal_data.append("")
        elif din_type == "probe":
            cfghal_data.append(f"net toolprobe <= rio.input.{dname}")
            cfghal_data.append(f"net toolprobe => motion.probe-input")
            cfghal_data.append("")

    for num, dout in enumerate(project["doutnames"]):
        dname = dout['_name']
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            netlist.append(dout_net)
            cfghal_data.append(f"net {dout_name} <= {dout_net}")
            cfghal_data.append(f"net {dout_name} => rio.{dname}")
            cfghal_data.append("")

    if f"iocontrol.0.emc-enable-in" not in netlist:
        cfghal_data.append("net rio-status <= rio.SPI-status => iocontrol.0.emc-enable-in")
        cfghal_data.append("")


    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        function = vin.get("function")
        if function == "spindle-index":
            scale = vin.get("scale", 1.0)
            cfghal_data.append(f"setp rio.{vname}-scale {scale}")
            cfghal_data.append(f"net spindle-position rio.{vname} => spindle.0.revs")
            cfghal_data.append(f"net spindle-index-enable rio.{vname}-index-enable <=> spindle.0.index-enable")
            cfghal_data.append("")
        elif function:
            pass

    cfghal_data.append("")

    pidn = 0
    for num, joint in enumerate(project["jointnames"]):
        # limit axis configurations
        if num >= num_joints:
            continue
        if joint.get("cl", False):
            cfghal_data.append(
                f"""# Joint {num} setup

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

net {axis_names[num]}vel-cmd 		<= pid.{pidn}.output 	=> rio.joint.{num}.vel-cmd  
net {axis_names[num]}pos-cmd 		<= joint.{num}.motor-pos-cmd 	=> pid.{pidn}.command
net j{num}pos-fb 		<= rio.joint.{num}.pos-fb 	=> joint.{num}.motor-pos-fb
net j{num}pos-fb 		=> pid.{pidn}.feedback

net j{num}enable 		<= joint.{num}.amp-enable-out 	=> rio.joint.{num}.enable
net j{num}enable 		=> pid.{pidn}.enable

"""
            )

            pidn += 1
        else:

            cfghal_data.append(
                f"""# Joint {num} setup

setp rio.joint.{num}.scale 		[JOINT_{num}]SCALE
setp rio.joint.{num}.maxaccel 	[JOINT_{num}]STEPGEN_MAXACCEL

net {axis_names[num]}pos-cmd 		<= joint.{num}.motor-pos-cmd 	=> rio.joint.{num}.pos-cmd  
net j{num}pos-fb 		<= rio.joint.{num}.pos-fb 	=> joint.{num}.motor-pos-fb
net j{num}enable 		<= joint.{num}.amp-enable-out 	=> rio.joint.{num}.enable

"""
            )
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio.hal", "w").write(
        "\n".join(cfghal_data)
    )

def generate_custom_postgui_hal_qtdragon(project):
    gui = project["jdata"].get("gui", "axis")

    netlist = []
    for num, din in enumerate(project["dinnames"]):
        din_net = din.get("net")
        if din_net:
            netlist.append(din_net)

    cfghal_data = []
    cfghal_data.append("")


    for num, din in enumerate(project["dinnames"]):
        dname = din['_name']
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            cfghal_data.append(f"net {dname} => qtdragon.{dname}")
        elif din_type == "alarm" and din_joint:
            pass
        elif din_type == "home" and din_joint:
            pass
        elif not dname.endswith("-index-enable-out"):
            cfghal_data.append(
                f"net {dname} rio.{dname} qtdragon.{dname}"
            )


    jogwheel = False
    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        vin_name = vin.get("name", f"vin{num}")
        vin_net = vin.get("net")
        function = vin.get("function")
        vtype = vin.get("type")
        if vtype:
            vin_name = f"{vin_name} ({vtype})"

        if function:
            pass
        else:
            scale = vin.get("scale")
            if scale is not None and float(scale) != float(1.0):
                cfghal_data.append(f"setp rio.{vname}-scale {scale}")
            offset = vin.get("offset")
            if offset is not None and float(offset) != float(0.0):
                cfghal_data.append(f"setp rio.{vname}-offset {offset}")
            display = vin.get("display", {})
            display_type = display.get("type")
            if display_type == "meter":
                cfghal_data.append(f"net {vname} rio.{vname} qtdragon.gauge_{vname}_value")
            elif display_type == "bar":
                pass
            elif display_type:
                cfghal_data.append(f"net {vname} rio.{vname} qtdragon.{vname}")

    """
    #postgui_list.append("net qtdragon.slider_SP.12")
    #postgui_list.append("setp rio.flow-scale 0.033")
    """
    # spindle.0
    if "hy_vfd" in project["jdata"]:
        cfghal_data.append("net pyvcp-spindle-at-speed   vfd.spindle-at-speed      => pyvcp.spindle-at-speed")
        cfghal_data.append("net pyvcp-spindle-speed_fb   vfd.spindle-speed-fb      => pyvcp.spindle-speed")
        cfghal_data.append("net pyvcp-hycomm-ok          vfd.hycomm-ok             => pyvcp.hycomm-ok")
        cfghal_data.append("#net qtdragon-spindle-voltage    vfd.rated-motor-voltage   => qtdragon.spindle-volts")
        cfghal_data.append("#net qtdragon-spindle-current    vfd.rated-motor-current   => qtdragon.spindle-amps")
        """
        qtdragon.spindle-modbus-connection
        qtdragon.spindle-modbus-errors
        qtdragon.spindle-amps
        qtdragon.spindle-fault
        qtdragon.spindle-volts
        """
        cfghal_data.append("")

    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/custom_postgui.hal", "w").write(
        "\n".join(cfghal_data)
    )

    postgui_list = []
    postgui_list.append("source custom_postgui.hal")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/postgui_call_list.hal", "w").write(
        "\n".join(postgui_list)
    )


def generate_custom_postgui_hal_axis(project):
    gui = project["jdata"].get("gui", "axis")

    netlist = []
    for num, din in enumerate(project["dinnames"]):
        din_net = din.get("net")
        if din_net:
            netlist.append(din_net)

    cfghal_data = []
    cfghal_data.append("")

    for num, dout in enumerate(project["doutnames"]):
        dname = dout['_name']
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            cfghal_data.append(f"net {dname} => pyvcp.{dname}")
        elif not dname.endswith("-index-enable"):
            cfghal_data.append(f"net {dname} pyvcp.{dname} rio.{dname}")

    for num, din in enumerate(project["dinnames"]):
        dname = din['_name']
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            cfghal_data.append(f"net {dname} => pyvcp.{dname}")
        elif din_type == "alarm" and din_joint:
            pass
        elif din_type == "home" and din_joint:
            pass
        elif not dname.endswith("-index-enable-out"):
            cfghal_data.append(
                f"net {dname} rio.{dname} pyvcp.{dname}"
            )

    for num, vout in enumerate(project["voutnames"]):
        vname = vout['_name']
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        if vout_net:
            cfghal_data.append(f"net {vname} => pyvcp.{vname}")
        else:
            cfghal_data.append(f"net {vname} pyvcp.{vname}-f rio.{vname}")

    jogwheel = False
    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        vin_name = vin.get("name", f"vin{num}")
        vin_net = vin.get("net")
        function = vin.get("function")
        if vin_net in ["halui.feed-override", "halui.rapid-override", "halui.spindle.0.override", "halui.spindle.1.override"]:
            function = vin_net.split(".")[-1]
        if function == "jogwheel" and not jogwheel:
            jogwheel = True
            cfghal_data.append("")
            cfghal_data.append("# jog-wheel")
            cfghal_data.append(f"loadrt mux8 count=1")
            cfghal_data.append(f"addf mux8.0 servo-thread")
            cfghal_data.append(f"setp mux8.0.in1 0.01")
            cfghal_data.append(f"setp mux8.0.in2 0.1")
            cfghal_data.append(f"setp mux8.0.in4 1.0")
            cfghal_data.append(f"net scale1 mux8.0.sel0 <= pyvcp.jog-scale.001")
            cfghal_data.append(f"net scale2 mux8.0.sel1 <= pyvcp.jog-scale.01")
            cfghal_data.append(f"net scale3 mux8.0.sel2 <= pyvcp.jog-scale.1")
            cfghal_data.append(f"net jog-scale <= mux8.0.out")
            cfghal_data.append(f"net jog-vel-mode <= pyvcp.jog-mode")
            for jnum in range(min(project["joints"], len(axis_names))):
                # limit axis configurations
                if jnum >= num_joints:
                    continue
                axis_str = axis_names[jnum].lower()
                cfghal_data.append(f"net jog-vel-mode => joint.{jnum}.jog-vel-mode axis.{axis_str}.jog-vel-mode")
                cfghal_data.append(f"net jog-scale => joint.{jnum}.jog-scale axis.{axis_str}.jog-scale")
                cfghal_data.append(f"net jog-counts => joint.{jnum}.jog-counts axis.{axis_str}.jog-counts")
                #cfghal_data.append(f"net jog-enable-{axis_str} axisui.jog.{axis_str} => joint.{jnum}.jog-enable axis.{axis_str}.jog-enable")
                cfghal_data.append(f"net jog-enable-{axis_str} pyvcp.jog-axis.{axis_str} => joint.{jnum}.jog-enable axis.{axis_str}.jog-enable")
            cfghal_data.append(f"net jog-counts <= rio.{vname}-s32")
            cfghal_data.append("")
        elif function in ["feed-override", "rapid-override", "spindle.0.override", "spindle.1.override"]:
            cfghal_data.append("")
            cfghal_data.append(f"# {function}")
            if vin['type'] == "ads1115":
                cfghal_data.append(f"setp rio.{vname}-scale 0.3025")
            else:
                cfghal_data.append(f"setp rio.{vname}-scale 1.0")
            cfghal_data.append(f"setp halui.{function}.direct-value 1")
            cfghal_data.append(f"setp halui.{function}.scale 0.01")
            cfghal_data.append(f"net {function} rio.{vname}-s32 => halui.{function}.counts")
            cfghal_data.append("")
        elif function:
            pass
        else:
            scale = vin.get("scale")
            if scale is not None and float(scale) != float(1.0):
                cfghal_data.append(f"setp rio.{vname}-scale {scale}")
            offset = vin.get("offset")
            if offset is not None and float(offset) != float(0.0):
                cfghal_data.append(f"setp rio.{vname}-offset {offset}")
            cfghal_data.append(f"net {vname} rio.{vname} pyvcp.{vname}")

        if vin.get("type") in {"vin_quadencoder", "vin_quadencoderz"}:
            cfghal_data.append(f"net {vname}-rpm rio.{vname}-rpm pyvcp.{vname}-rpm")

    cfghal_data.append("net zeroxy halui.mdi-command-00 <= pyvcp.zeroxy")
    cfghal_data.append("net zeroz halui.mdi-command-01 <= pyvcp.zeroz")
    if "motion.probe-input" in netlist:
        cfghal_data.append("net ztouch halui.mdi-command-02 <= pyvcp.ztouch")

    # spindle.0
    if "hy_vfd" in project["jdata"]:
        cfghal_data.append("net pyvcp-spindle-at-speed   vfd.spindle-at-speed      => pyvcp.spindle-at-speed")
        cfghal_data.append("net pyvcp-spindle-speed_fb   vfd.spindle-speed-fb      => pyvcp.spindle-speed")
        cfghal_data.append("net pyvcp-hycomm-ok          vfd.hycomm-ok             => pyvcp.hycomm-ok")
        cfghal_data.append("#net pyvcp-spindle-voltage    vfd.rated-motor-voltage   => pyvcp.spindle-voltage")
        cfghal_data.append("#net pyvcp-spindle-current    vfd.rated-motor-current   => pyvcp.spindle-current")


    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/custom_postgui.hal", "w").write(
        "\n".join(cfghal_data)
    )

    postgui_list = []
    postgui_list.append("source custom_postgui.hal")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/postgui_call_list.hal", "w").write(
        "\n".join(postgui_list)
    )


def generate_rio_axis(project):
    netlist = []
    for num, din in enumerate(project["dinnames"]):
        din_net = din.get("net")
        if din_net:
            netlist.append(din_net)

    gui_gen = axis()

    cfgxml_data = []
    cfgxml_data.append("<pyvcp>")
    cfgxml_data.append('<tabs>')
    cfgxml_data.append('    <names>["Status", "Inputs", "Outputs"]</names>')

    # Tab: Status
    cfgxml_data.append('    <vbox>')

    # jogging
    jogwheel = False
    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        vin_name = vin.get("name", f"vin{num}")
        vin_net = vin.get("net")
        function = vin.get("function")
        if vin_net in ["halui.feed-override", "halui.rapid-override", "halui.spindle.0.override", "halui.spindle.1.override"]:
            function = vin_net.split(".")[-1]
        if function == "jogwheel" and not jogwheel:
            jogwheel = True
            cfgxml_data.append("  <labelframe text=\"Jog-Options\">")
            cfgxml_data.append("    <relief>RAISED</relief>")
            cfgxml_data.append("    <font>(\"Helvetica\", 12)</font>")
            cfgxml_data.append("  <hbox>")
            cfgxml_data.append("    <relief>RAISED</relief>")
            cfgxml_data.append("    <bd>2</bd>")
            cfgxml_data.append("	<radiobutton>")
            axislist = []
            for jnum in range(min(project["joints"], len(axis_names))):
                # limit axis configurations
                if jnum >= num_joints:
                    continue
                axis_str = axis_names[jnum].lower()
                axislist.append(f"\"{axis_str}\"")
            axislist_str = ','.join(axislist)
            cfgxml_data.append(f"		<choices>[{axislist_str}]</choices> ")
            cfgxml_data.append("		<halpin>\"jog-axis\"</halpin> ")
            cfgxml_data.append("	</radiobutton>")
            cfgxml_data.append("	<radiobutton>")
            cfgxml_data.append("		<choices>[\"001\", \"01\", \"1\"]</choices> ")
            cfgxml_data.append("		<halpin>\"jog-scale\"</halpin> ")
            cfgxml_data.append("	</radiobutton>")
            cfgxml_data.append("    <checkbutton>")
            cfgxml_data.append(f'      <halpin>"jog-mode"</halpin>')
            cfgxml_data.append(f'      <text>"Velocity"</text>')
            cfgxml_data.append("    </checkbutton>")
            cfgxml_data.append("  </hbox>")
            cfgxml_data.append("  </labelframe>")
        elif vin.get("type") in {"vin_quadencoder", "vin_quadencoderz"}:
            cfgxml_data += gui_gen.draw_number(f"RPM - {vname}", f"{vname}-rpm")

        elif function:
            pass

    # spindle.0
    if "hy_vfd" in project["jdata"]:
        cfgxml_data.append("<labelframe text=\"Spindle\">")
        cfgxml_data.append("    <relief>RAISED</relief>")
        cfgxml_data.append("    <font>(\"Helvetica\", 12)</font>")
        cfgxml_data.append("  <vbox>")
        cfgxml_data.append("    <hbox>")
        cfgxml_data.append("      <label>")
        cfgxml_data.append("          <text>\"RPM\"</text>")
        cfgxml_data.append("          <font>(\"Helvetica\",10)</font>")
        cfgxml_data.append("      </label>")
        cfgxml_data.append("      <number>")
        cfgxml_data.append('        <halpin>"spindle-speed"</halpin>')
        cfgxml_data.append('        <font>("Helvetica",24)</font>')
        cfgxml_data.append('        <format>"05d"</format>')
        cfgxml_data.append("      </number>")
        cfgxml_data.append("      <vbox>")
        cfgxml_data.append("        <hbox>")
        cfgxml_data.append("          <led>")
        cfgxml_data.append("            <halpin>\"hycomm-ok\"</halpin>")
        cfgxml_data.append("            <size>\"10\"</size>")
        cfgxml_data.append("            <on_color>\"green\"</on_color>")
        cfgxml_data.append("            <off_color>\"red\"</off_color>")
        cfgxml_data.append("          </led>")
        cfgxml_data.append("          <label>")
        cfgxml_data.append("            <text>\"Modbus\"</text>")
        cfgxml_data.append("          </label>")
        cfgxml_data.append("        </hbox>")
        cfgxml_data.append("        <hbox>")
        cfgxml_data.append("          <led>")
        cfgxml_data.append("            <halpin>\"spindle-at-speed\"</halpin>")
        cfgxml_data.append("            <size>\"10\"</size>")
        cfgxml_data.append("            <on_color>\"green\"</on_color>")
        cfgxml_data.append("            <off_color>\"red\"</off_color>")
        cfgxml_data.append("          </led>")
        cfgxml_data.append("          <label>")
        cfgxml_data.append("            <text>\"at speed\"</text>")
        cfgxml_data.append("          </label>")
        cfgxml_data.append("        </hbox>")
        cfgxml_data.append("      </vbox>")
        cfgxml_data.append("    </hbox>")
        cfgxml_data.append("  </vbox>")
        cfgxml_data.append("</labelframe>")

    for num, din in enumerate(project["dinnames"]):
        dname = din['_name']
        if dname.endswith("-index-enable-out"):
            continue
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            cfgxml_data += gui_gen.draw_led(din_name, dname)

    for num, vout in enumerate(project["voutnames"]):
        vname = vout['_name']
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        if vout_net:
            if "dir" in vout:
                vmin = int(vout.get('min', vout.get('max', 100)) * -1)
                vmax = vout.get('max', 100)
            else:
                vmin = int(vout.get('min', 0))
                vmax = vout.get('max', 100)
            if vout.get("type") == "pwm":
                cfgxml_data += gui_gen.draw_bar(vout_name, vname, vmin=vmin, vmax=vmax)
            else:
                cfgxml_data += gui_gen.draw_number(vout_name, vname)

    jogwheel = False
    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        vin_name = vin.get("name", f"vin{num}")
        vin_net = vin.get("net")
        function = vin.get("function")
        vtype = vin.get("type")
        if vtype:
            vin_name = f"{vin_name} ({vtype})"
        if function == "jogwheel" and not jogwheel:
            jogwheel = True
        elif function:
            pass
        else:
            display = vin.get("display", {})
            display_type = display.get("type")
            if display_type == "meter":
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_meter(display_text, vname, display)
            elif display_type == "bar":
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_bar(display_text, vname, display)
            elif display_type:
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_number(display_text, vname, display)


    cfgxml_data.append('  </vbox>')

    # Tab: Inputs
    cfgxml_data.append('  <vbox>')
    for num, din in enumerate(project["dinnames"]):
        dname = din['_name']
        if dname.endswith("-index-enable-out"):
            continue
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if not din_net:
            cfgxml_data += gui_gen.draw_led(din_name, dname)

    jogwheel = False
    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        vin_name = vin.get("name", f"vin{num}")
        vin_net = vin.get("net")
        function = vin.get("function")
        vtype = vin.get("type")
        if vtype:
            vin_name = f"{vin_name} ({vtype})"
        if function == "jogwheel" and not jogwheel:
            jogwheel = True
        elif function:
            pass
        else:
            display = vin.get("display", {})
            display_type = display.get("type")
            if not display_type:
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_number(display_text, vname, display)
    cfgxml_data.append('  </vbox>')

    # Tab: Outputs
    cfgxml_data.append('  <vbox>')
    for num, dout in enumerate(project["doutnames"]):
        dname = dout['_name']
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            cfgxml_data += gui_gen.draw_led(dout_name, dname)
        else:
            cfgxml_data += gui_gen.draw_checkbutton(dout_name, dname)

    for num, vout in enumerate(project["voutnames"]):
        vname = vout['_name']
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        vmin = vout.get('min', 0)
        vmax = vout.get('max', 100)
        if vout_net:
            continue
        vtype = vout.get("type")
        if vtype:
            vout_name = f"{vout_name} ({vtype})"
        if vout.get("type") == "vout_sine":
            vmin = vout.get('min', -100)
            vmax = vout.get('max', 100)
        elif vout.get("type") == "vout_pwm":
            if "dir" in vout:
                vmin = int(vout.get('max', 100)) * -1
            else:
                vmin = vout.get('min', 0)
            vmax = vout.get('max', 100)
        elif vout.get("type") == "vout_rcservo":
            vmin = vout.get('min', -100)
            vmax = vout.get('max', 100)
        else:
            vmin = vout.get('min', 0)
            vmax = vout.get('max', 10)

        cfgxml_data += gui_gen.draw_scale(vout_name, vname, vmin, vmax)

    cfgxml_data.append('  </vbox>')
    cfgxml_data.append('</tabs>')

    # mdi-command buttons
    cfgxml_data.append("  <labelframe text=\"MDI-Commands\">")
    cfgxml_data.append("    <relief>RAISED</relief>")
    cfgxml_data.append("    <font>(\"Helvetica\", 12)</font>")
    cfgxml_data.append("    <hbox>")
    cfgxml_data.append("      <relief>RIDGE</relief>")
    cfgxml_data.append("      <bd>2</bd>")
    cfgxml_data.append("      <button>")
    cfgxml_data.append("        <relief>RAISED</relief>")
    cfgxml_data.append("        <bd>3</bd>")
    cfgxml_data.append("        <halpin>\"zeroxy\"</halpin><text>\"Zero XY\"</text>")
    cfgxml_data.append("        <font>(\"Helvetica\", 12)</font>")
    cfgxml_data.append("      </button>")
    cfgxml_data.append("      <button>")
    cfgxml_data.append("        <relief>RAISED</relief>")
    cfgxml_data.append("        <bd>3</bd>")
    cfgxml_data.append("        <halpin>\"zeroz\"</halpin><text>\"Zero Z\"</text>")
    cfgxml_data.append("        <font>(\"Helvetica\", 12)</font>")
    cfgxml_data.append("      </button>")
    if "motion.probe-input" in netlist:
        cfgxml_data.append("      <button>")
        cfgxml_data.append("        <relief>RAISED</relief>")
        cfgxml_data.append("        <bd>3</bd>")
        cfgxml_data.append("        <halpin>\"ztouch\"</halpin><text>\"Touch Off\"</text>")
        cfgxml_data.append("        <font>(\"Helvetica\", 12)</font>")
        cfgxml_data.append("      </button>")
    cfgxml_data.append("    </hbox>")
    cfgxml_data.append("  </labelframe>")

    cfgxml_data.append("</pyvcp>")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio-gui.xml", "w").write(
        "\n".join(cfgxml_data)
    )





def generate_rio_qtdragon(project):
    netlist = []
    for num, din in enumerate(project["dinnames"]):
        din_net = din.get("net")
        if din_net:
            netlist.append(din_net)

    gui = project["jdata"].get("gui", "axis")
    
    gui_gen = qtdragon()

    cfgxml_data = []
    cfgxml_data.append("")
    cfgxml_data.append("")


    cfgxml_data.append("           <item>")
    cfgxml_data.append("            <widget class=\"QGroupBox\" name=\"groupBox_rio\">")
    cfgxml_data.append("             <property name=\"title\">")
    cfgxml_data.append("              <string>RIO</string>")
    cfgxml_data.append("             </property>")


    cfgxml_data.append("           <property name=\"sizePolicy\">")
    cfgxml_data.append("            <sizepolicy hsizetype=\"Minimum\" vsizetype=\"Preferred\">")
    cfgxml_data.append("             <horstretch>0</horstretch>")
    cfgxml_data.append("             <verstretch>0</verstretch>")
    cfgxml_data.append("            </sizepolicy>")
    cfgxml_data.append("           </property>")
    cfgxml_data.append("           <property name=\"minimumSize\">")
    cfgxml_data.append("            <size>")
    cfgxml_data.append("             <width>200</width>")
    cfgxml_data.append("             <height>0</height>")
    cfgxml_data.append("            </size>")
    cfgxml_data.append("           </property>")

    cfgxml_data.append("             <property name=\"alignment\">")
    cfgxml_data.append("              <set>Qt::AlignCenter</set>")
    cfgxml_data.append("             </property>")
    cfgxml_data.append("             <layout class=\"QVBoxLayout\" name=\"verticalLayout_30\">")
    cfgxml_data.append("              <property name=\"spacing\">")
    cfgxml_data.append("               <number>6</number>")
    cfgxml_data.append("              </property>")
    cfgxml_data.append("              <property name=\"leftMargin\">")
    cfgxml_data.append("               <number>2</number>")
    cfgxml_data.append("              </property>")
    cfgxml_data.append("              <property name=\"topMargin\">")
    cfgxml_data.append("               <number>2</number>")
    cfgxml_data.append("              </property>")
    cfgxml_data.append("              <property name=\"rightMargin\">")
    cfgxml_data.append("               <number>2</number>")
    cfgxml_data.append("              </property>")
    cfgxml_data.append("              <property name=\"bottomMargin\">")
    cfgxml_data.append("               <number>2</number>")
    cfgxml_data.append("              </property>")



    cfgxml_data.append("                    <item>")
    cfgxml_data.append("                     <widget class=\"QTabWidget\" name=\"tabWidget_setup\">")

    cfgxml_data.append("  <property name=\"geometry\">")
    cfgxml_data.append("   <rect>")
    cfgxml_data.append("    <x>0</x>")
    cfgxml_data.append("    <y>0</y>")
    cfgxml_data.append("    <width>400</width>")
    cfgxml_data.append("    <height>300</height>")
    cfgxml_data.append("   </rect>")
    cfgxml_data.append("  </property>")

    cfgxml_data.append("                      <property name=\"sizePolicy\">")
    cfgxml_data.append("                       <sizepolicy hsizetype=\"Expanding\" vsizetype=\"Preferred\">")
    cfgxml_data.append("                        <horstretch>1</horstretch>")
    cfgxml_data.append("                        <verstretch>0</verstretch>")
    cfgxml_data.append("                       </sizepolicy>")
    cfgxml_data.append("                      </property>")
    cfgxml_data.append("                      <property name=\"currentIndex\">")
    cfgxml_data.append("                       <number>0</number>")
    cfgxml_data.append("                      </property>")



    cfgxml_data.append("                      <widget class=\"QWidget\" name=\"tab_stat\">")
    cfgxml_data.append("                       <attribute name=\"title\">")
    cfgxml_data.append("                        <string>Stat</string>")
    cfgxml_data.append("                       </attribute>")
    cfgxml_data.append("                       <layout class=\"QVBoxLayout\" name=\"layout_stat\">")
    cfgxml_data.append("                        <property name=\"spacing\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"leftMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"topMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"rightMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"bottomMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")

    cfgxml_data.append("                         <item>")
    cfgxml_data.append("                          <layout class=\"QVBoxLayout\" name=\"verticalLayout_58\">")


    for num, dout in enumerate(project["doutnames"]):
        dname = dout['_name']
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            cfgxml_data += gui_gen.draw_led(dout_name, dname)
        else:
            cfgxml_data += gui_gen.draw_checkbutton(dout_name, dname)

    for num, din in enumerate(project["dinnames"]):
        dname = din['_name']
        if dname.endswith("-index-enable-out"):
            continue
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            cfgxml_data += gui_gen.draw_led(din_name, dname)

    for num, vout in enumerate(project["voutnames"]):
        vname = vout['_name']
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        if vout_net:
            if "dir" in vout:
                vmin = int(vout.get('min', vout.get('max', 100)) * -1)
                vmax = vout.get('max', 100)
            else:
                vmin = int(vout.get('min', 0))
                vmax = vout.get('max', 100)
            if vout.get("type") == "pwm":
                cfgxml_data += gui_gen.draw_bar(vout_name, vname, vmin=vmin, vmax=vmax)
            else:
                cfgxml_data += gui_gen.draw_number(vout_name, vname)

    jogwheel = False
    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        vin_name = vin.get("name", f"vin{num}")
        vin_net = vin.get("net")
        function = vin.get("function")
        vtype = vin.get("type")
        if vtype:
            vin_name = f"{vin_name} ({vtype})"
        if function == "jogwheel" and not jogwheel:
            jogwheel = True
        elif function:
            pass
        else:
            display = vin.get("display", {})
            display_type = display.get("type")
            if display_type == "meter":
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_meter(display_text, vname, display)
            elif display_type == "bar":
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_bar(display_text, vname, display)
            elif display_type:
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_number(display_text, vname, display)


    cfgxml_data.append("                          </layout>")
    cfgxml_data.append("                         </item>")
    cfgxml_data.append("                        </layout>")
    cfgxml_data.append("                      </widget>")

    cfgxml_data.append("                      <widget class=\"QWidget\" name=\"tab_inputs\">")
    cfgxml_data.append("                       <attribute name=\"title\">")
    cfgxml_data.append("                        <string>In/Out</string>")
    cfgxml_data.append("                       </attribute>")
    cfgxml_data.append("                       <layout class=\"QVBoxLayout\" name=\"layout_properties\">")
    cfgxml_data.append("                        <property name=\"spacing\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"leftMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"topMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"rightMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"bottomMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")

    cfgxml_data.append("                         <item>")
    cfgxml_data.append("                          <layout class=\"QVBoxLayout\" name=\"verticalLayout_58\">")

    # Tab: Inputs
    for num, din in enumerate(project["dinnames"]):
        dname = din['_name']
        if dname.endswith("-index-enable-out"):
            continue
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if not din_net:
            cfgxml_data += gui_gen.draw_led(din_name, dname)

    jogwheel = False
    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        vin_name = vin.get("name", f"vin{num}")
        vin_net = vin.get("net")
        function = vin.get("function")
        vtype = vin.get("type")
        #if vtype:
        #    vin_name = f"{vin_name} ({vtype})"
        if function == "jogwheel" and not jogwheel:
            jogwheel = True
        elif function:
            pass
        else:
            display = vin.get("display", {})
            display_type = display.get("type")
            if display_type == "meter":
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_number(display_text, vname, display)
            else:
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_number(display_text, vname, display)


    """
    cfgxml_data.append("                          </layout>")
    cfgxml_data.append("                         </item>")
    cfgxml_data.append("                        </layout>")
    cfgxml_data.append("                      </widget>")

    cfgxml_data.append("                      <widget class=\"QWidget\" name=\"tab_outputs\">")
    cfgxml_data.append("                       <attribute name=\"title\">")
    cfgxml_data.append("                        <string>Out</string>")
    cfgxml_data.append("                       </attribute>")
    cfgxml_data.append("                       <layout class=\"QVBoxLayout\" name=\"layout_properties\">")
    cfgxml_data.append("                        <property name=\"spacing\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"leftMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"topMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"rightMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")
    cfgxml_data.append("                        <property name=\"bottomMargin\">")
    cfgxml_data.append("                         <number>0</number>")
    cfgxml_data.append("                        </property>")

    cfgxml_data.append("                         <item>")
    cfgxml_data.append("                          <layout class=\"QVBoxLayout\" name=\"verticalLayout_58\">")
    """


    # Tab: Outputs
    for num, dout in enumerate(project["doutnames"]):
        dname = dout['_name']
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            cfgxml_data += gui_gen.draw_led(dout_name, dname)
        else:
            cfgxml_data += gui_gen.draw_checkbutton(dout_name, dname)

    for num, vout in enumerate(project["voutnames"]):
        vname = vout['_name']
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        vmin = vout.get('min', 0)
        vmax = vout.get('max', 100)
        if vout_net:
            continue
        vtype = vout.get("type")
        if vtype:
            vout_name = f"{vout_name} ({vtype})"
        if vout.get("type") == "vout_sine":
            vmin = vout.get('min', -100)
            vmax = vout.get('max', 100)
        elif vout.get("type") == "vout_pwm":
            if "dir" in vout:
                vmin = int(vout.get('max', 100)) * -1
            else:
                vmin = vout.get('min', 0)
            vmax = vout.get('max', 100)
        elif vout.get("type") == "vout_rcservo":
            vmin = vout.get('min', -100)
            vmax = vout.get('max', 100)
        else:
            vmin = vout.get('min', 0)
            vmax = vout.get('max', 10)

        cfgxml_data += gui_gen.draw_scale(vout_name, vname, vmin, vmax)


    cfgxml_data.append("                          </layout>")
    cfgxml_data.append("                         </item>")
    cfgxml_data.append("                        </layout>")
    cfgxml_data.append("                      </widget>")


    cfgxml_data.append("                     </widget>")
    cfgxml_data.append("                    </item>")

    cfgxml_data.append("             </layout>")
    cfgxml_data.append("            </widget>")
    cfgxml_data.append("           </item>")

    cfgxml_data.append("")
    cfgxml_data.append("")

    os.system(
        f"mkdir -p {project['LINUXCNC_PATH']}/ConfigSamples/rio/rio_hd"
    )
    os.system(
        f"cp -a generators/linuxcnc_config/rio_hd/* {project['LINUXCNC_PATH']}/ConfigSamples/rio/rio_hd/"
    )
    os.system(
        f"cat generators/linuxcnc_config/rio_hd/rio_hd.ui.pre > {project['LINUXCNC_PATH']}/ConfigSamples/rio/rio_hd/rio_hd.ui"
    )
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio_hd/rio_hd.ui", "a").write(
        "\n".join(cfgxml_data)
    )
    os.system(
        f"cat generators/linuxcnc_config/rio_hd/rio_hd.ui.post >> {project['LINUXCNC_PATH']}/ConfigSamples/rio/rio_hd/rio_hd.ui"
    )




def generate_tool_tbl(project):
    tool_tbl = []
    tool_tbl.append("T1 P1 D0.125000 Z+0.511000 ;1/8 end mill")
    tool_tbl.append("T2 P2 D0.062500 Z+0.100000 ;1/16 end mill")
    tool_tbl.append("T3 P3 D0.201000 Z+1.273000 ;#7 tap drill")
    tool_tbl.append("T99999 P99999 Z+0.100000 ;big tool number")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/tool.tbl", "w").write(
        "\n".join(tool_tbl)
    )



def generate(project):
    gui = project["jdata"].get("gui", "axis")
    print(f"generating linux-cnc config: {gui}")
    generate_rio_ini(project)
    generate_rio_hal(project)
    if gui == "qtdragon":
        generate_custom_postgui_hal_qtdragon(project)
        generate_rio_qtdragon(project)
    else:
        generate_custom_postgui_hal_axis(project)
        generate_rio_axis(project)
    generate_tool_tbl(project)

    os.system(
        f"cp -a generators/linuxcnc_config/linuxcnc.var {project['LINUXCNC_PATH']}/ConfigSamples/rio"
    )
