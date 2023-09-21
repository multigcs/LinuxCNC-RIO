
import os
import sys

axis_names = ["X", "Y", "Z", "A", "C", "B", "U", "V", "W"]
netlist = []

class qtdragon():
    #
    # wget "https://raw.githubusercontent.com/LinuxCNC/linuxcnc/master/lib/python/qtvcp/designer/install_script"
    #

    def draw_begin(self):
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
        return cfgxml_data

    def draw_end(self):
        cfgxml_data = []
        cfgxml_data.append("             </layout>")
        cfgxml_data.append("            </widget>")
        cfgxml_data.append("           </item>")
        cfgxml_data.append("")
        cfgxml_data.append("")
        return cfgxml_data

    def draw_tabs_begin(self, names):
        cfgxml_data = []
        cfgxml_data.append("                    <item>")
        cfgxml_data.append("                     <widget class=\"QTabWidget\" name=\"tabWidget_setup\">")
        cfgxml_data.append("                      <property name=\"geometry\">")
        cfgxml_data.append("                       <rect>")
        cfgxml_data.append("                        <x>0</x>")
        cfgxml_data.append("                        <y>0</y>")
        cfgxml_data.append("                        <width>400</width>")
        cfgxml_data.append("                        <height>300</height>")
        cfgxml_data.append("                       </rect>")
        cfgxml_data.append("                      </property>")
        cfgxml_data.append("                      <property name=\"sizePolicy\">")
        cfgxml_data.append("                       <sizepolicy hsizetype=\"Expanding\" vsizetype=\"Preferred\">")
        cfgxml_data.append("                        <horstretch>1</horstretch>")
        cfgxml_data.append("                        <verstretch>0</verstretch>")
        cfgxml_data.append("                       </sizepolicy>")
        cfgxml_data.append("                      </property>")
        cfgxml_data.append("                      <property name=\"currentIndex\">")
        cfgxml_data.append("                       <number>0</number>")
        cfgxml_data.append("                      </property>")
        return cfgxml_data

    def draw_tabs_end(self):
        cfgxml_data = []
        cfgxml_data.append("                     </widget>")
        cfgxml_data.append("                    </item>")
        return cfgxml_data

    def draw_tab_begin(self, name):
        cfgxml_data = []
        cfgxml_data.append(f"                      <widget class=\"QWidget\" name=\"tab_{name}\">")
        cfgxml_data.append("                       <attribute name=\"title\">")
        cfgxml_data.append(f"                        <string>{name}</string>")
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
        return cfgxml_data

    def draw_tab_end(self):
        cfgxml_data = []
        cfgxml_data.append("                          </layout>")
        cfgxml_data.append("                         </item>")
        cfgxml_data.append("                        </layout>")
        cfgxml_data.append("                      </widget>")
        return cfgxml_data

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
        display_text = setup.get("text", name)
        display_subtext = setup.get("subtext", '')
        display_region = setup.get("region", [])
        display_size = setup.get("size", 150)
        display_threshold = setup.get("threshold")
        cfgxml_data = []
        cfgxml_data.append('   <item>')
        cfgxml_data.append(f'       <widget class="Gauge" name="{halpin}">')
        cfgxml_data.append('        <property name="minimumSize">')
        cfgxml_data.append('         <size>')
        cfgxml_data.append('          <width>150</width>')
        cfgxml_data.append('          <height>150</height>')
        cfgxml_data.append('         </size>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="max_value" stdset="0">')
        cfgxml_data.append(f'         <number>{display_max}</number>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="max_reading" stdset="0">')
        cfgxml_data.append(f'         <number>{display_max}</number>')
        cfgxml_data.append('        </property>')
        if display_threshold:
            cfgxml_data.append('        <property name="threshold" stdset="0">')
            cfgxml_data.append(f'         <number>{display_threshold}</number>')
            cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="num_ticks" stdset="0">')
        cfgxml_data.append('         <number>9</number>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="gauge_label" stdset="0">')
        cfgxml_data.append(f'         <string>{display_text}</string>')
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
        return self.draw_number(name, halpin, setup)
        
        display_min = setup.get("min", vmin)
        display_max = setup.get("max", vmax)
        display_range = setup.get("range", [])
        display_format = setup.get("format", "05d")
        display_fillcolor = setup.get("fillcolor", "red")
        display_bgcolor = setup.get("fillcolor", "grey")
        cfgxml_data = []
        return cfgxml_data

    def draw_number(self, name, halpin, setup={}):
        display_format = setup.get("format", "%0.2f")
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
        cfgxml_data.append('      <property name="textTemplate" stdset="0">')
        cfgxml_data.append(f'       <string>{display_format}</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="styleSheet">')
        cfgxml_data.append('       <string notr="true">font: 20pt &quot;Lato Heavy&quot;;</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="bit_pin_type" stdset="0">')
        cfgxml_data.append('       <bool>false</bool>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="float_pin_type" stdset="0">')
        cfgxml_data.append('       <bool>true</bool>')
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
        cfgxml_data.append(f'     <widget class="PushButton" name="{halpin}">')
        cfgxml_data.append('      <property name="text">')
        cfgxml_data.append(f'       <string>{name}</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="checkable">')
        cfgxml_data.append('        <bool>true</bool>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="styleSheet">')
        cfgxml_data.append('        <string notr="true">font: 18pt &quot;Lato Heavy&quot;;</string>')
        cfgxml_data.append('      </property>')
        cfgxml_data.append('      <property name="minimumSize">')
        cfgxml_data.append('        <size>')
        cfgxml_data.append('         <width>32</width>')
        cfgxml_data.append('         <height>32</height>')
        cfgxml_data.append('        </size>')
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
        cfgxml_data.append('    <item>')
        cfgxml_data.append(f'     <widget class="LED" name="{halpin}">')
        cfgxml_data.append('        <property name="sizePolicy">')
        cfgxml_data.append('         <sizepolicy hsizetype="Fixed" vsizetype="Fixed">')
        cfgxml_data.append('          <horstretch>0</horstretch>')
        cfgxml_data.append('          <verstretch>0</verstretch>')
        cfgxml_data.append('         </sizepolicy>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="minimumSize">')
        cfgxml_data.append('         <size>')
        cfgxml_data.append('          <width>32</width>')
        cfgxml_data.append('          <height>32</height>')
        cfgxml_data.append('         </size>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="color">')
        cfgxml_data.append('          <color>')
        cfgxml_data.append('           <red>85</red>')
        cfgxml_data.append('           <green>255</green>')
        cfgxml_data.append('           <blue>0</blue>')
        cfgxml_data.append('          </color>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('        <property name="maximumSize">')
        cfgxml_data.append('         <size>')
        cfgxml_data.append('          <width>32</width>')
        cfgxml_data.append('          <height>32</height>')
        cfgxml_data.append('         </size>')
        cfgxml_data.append('        </property>')
        cfgxml_data.append('     </widget>')
        cfgxml_data.append('    </item>')
        cfgxml_data.append('   </layout>')
        cfgxml_data.append('  </item>')
        return cfgxml_data

class axis():

    def draw_begin(self):
        cfgxml_data = []
        cfgxml_data.append("<pyvcp>")
        return cfgxml_data

    def draw_end(self):
        cfgxml_data = []
        cfgxml_data.append("</pyvcp>")
        return cfgxml_data

    def draw_tabs_begin(self, names):
        cfgxml_data = []
        cfgxml_data.append('<tabs>')
        cfgxml_data.append(f'    <names>{names}</names>')
        return cfgxml_data

    def draw_tabs_end(self):
        cfgxml_data = []
        cfgxml_data.append('</tabs>')
        return cfgxml_data

    def draw_tab_begin(self, name):
        cfgxml_data = []
        cfgxml_data.append('    <vbox>')
        return cfgxml_data

    def draw_tab_end(self):
        cfgxml_data = []
        cfgxml_data.append('    </vbox>')
        return cfgxml_data


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
        cfgxml_data.append("      <size>16</size>")
        cfgxml_data.append('      <on_color>"green"</on_color>')
        cfgxml_data.append('      <off_color>"black"</off_color>')
        cfgxml_data.append("    </led>")
        cfgxml_data.append("    <label>")
        cfgxml_data.append(f'      <text>"{name}"</text>')
        cfgxml_data.append("    </label>")
        cfgxml_data.append("  </hbox>")
        return cfgxml_data



def generate_rio_ini(project):
    global netlist
    gui = project["jdata"].get("gui", "axis")
    limit_axis = int(project["jdata"].get("axis", 9))
    num_axis = min(project['joints'], limit_axis)
    num_joints = min(project['joints'], 9)

    axis_str = ""
    traj_axis_list = []
    for num in range(min(project["joints"], len(axis_names))):
        # limit axis configurations
        if num >= num_axis:
            continue
        axis_str += axis_names[num]
        traj_axis_list.append(axis_names[num])


    for num, joint in enumerate(project["jointnames"]):
        # limit axis configurations
        if num >= num_joints:
            continue
        AXIS_NAME = joint.get("axis", axis_names[num])
        if AXIS_NAME not in axis_str:
            continue
        if num >= len(traj_axis_list):
            print("append")
            traj_axis_list.append(AXIS_NAME)
        else:
            traj_axis_list[num] = AXIS_NAME

    num_joints = len(traj_axis_list)

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
            "POSITION_OFFSET": "RELATIVE",
            "POSITION_FEEDBACK": "ACTUAL",
            "PYVCP": "rio-gui.xml",
            "PREFERENCE_FILE_PATH": None,
            "ARCDIVISION": 64,
            "GRIDS": "10mm 20mm 50mm 100mm",
            "INTRO_GRAPHIC": "linuxcnc.gif",
            "INTRO_TIME": 2,
            "PROGRAM_PREFIX": "~/linuxcnc/nc_files",
            "INCREMENTS": "50mm 10mm 5mm 1mm .5mm .1mm .05mm .01mm",
            "SPINDLES": 1,
            "MAX_FEED_OVERRIDE": 5.0,
            "MIN_SPINDLE_0_OVERRIDE": 0.5,
            "MAX_SPINDLE_0_OVERRIDE": 1.2,
            "MIN_SPINDLE_0_SPEED": 1000,
            "DEFAULT_SPINDLE_0_SPEED": 6000,
            "MAX_SPINDLE_0_SPEED": 20000,
            "MIN_LINEAR_VELOCITY": 0.0,
            "DEFAULT_LINEAR_VELOCITY": 10.0,
            "MAX_LINEAR_VELOCITY": 40.0,
            "MIN_ANGULAR_VELOCITY": 0.0,
            "DEFAULT_ANGULAR_VELOCITY": 2.5,
            "MAX_ANGULAR_VELOCITY": 5.0,
            "SPINDLE_INCREMENT": 200,
            "MAX_SPINDLE_POWER": 2000,
        },
        "KINS": {
            "JOINTS": num_joints,
            "KINEMATICS": f"trivkins coordinates={''.join(traj_axis_list)}",
        },
        "FILTER": {
            "PROGRAM_EXTENSION": [".ngc,.nc,.tap G-Code File (*.ngc,*.nc,*.tap)", ".py Python Script"],
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
            "COORDINATES": " ".join(traj_axis_list),
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

    if gui == "qtdragon":
        qtdragon_setup = {
            "DISPLAY": {
                "DISPLAY": "qtvcp -d rio_hd",
                "ICON": "silver_dragon.png",
                "EDITOR": None,
                "PYVCP": None,
                "PREFERENCE_FILE_PATH": "WORKINGFOLDER/qtdragon_hd.pref",
                "INTRO_GRAPHIC": "silver_dragon.png",
                "CYCLE_TIME": 100,
                "NGCGUI_SUBFILE_PATH": "../../../nc_files/ngcgui_lib/",
                "NGCGUI_SUBFILE": "qpocket.ngc",
                "MDI_HISTORY_FILE": "mdi_history.dat",
                "LOG_FILE": "qtdragon_hd.log",
            },
            "MDI_COMMAND_LIST": {
                "MDI_COMMAND": ["G0 Z25 X0 Y0;Z0,Goto\\nZero", "G53 G0 Z0;G53 G0 X0 Y0,Goto\\nMach\\nZero"],
            },
            "FILTER": {
                "PROGRAM_EXTENSION": [".ngc,.nc,.tap G-Code File (*.ngc,*.nc,*.tap)", ".png,.gif,.jpg Greyscale Depth Image", ".py Python Script"],
                "png": "image-to-gcode",
                "gif": "image-to-gcode",
                "jpg": "image-to-gcode",
                "py": "python3",
            },
            "RS274NGC": {
                "PARAMETER_FILE": "linuxcnc.var",
                "RS274NGC_STARTUP_CODE": "G17 G21 G40 G43H0 G54 G64P0.0127 G80 G90 G94 G97 M5 M9",
                "SUBROUTINE_PATH": "./subroutines/",
                "USER_M_PATH": "./mcodes/",
                "ON_ABORT_COMMAND": "O <on_abort> call",
            },
            "HALUI": {
            },
            "PROBE": {
                "USE_PROBE": "basicprobe",
            },
        }
        for section, sdata in qtdragon_setup.items():
            if section not in basic_setup:
                basic_setup[section] = {}
            for key, value in sdata.items():
                basic_setup[section][key] = value



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

    for num, axis in enumerate(axis_str):
        for joint in project["jointnames"]:
            AXIS_NAME = joint.get("axis", axis_names[num])

            if AXIS_NAME == axis:
                if joint.get("type") == "rcservo":
                    SCALE = 80.0
                    MIN_LIMIT = -110
                    MAX_LIMIT = 110
                else:
                    if AXIS_NAME in "ACBUVW":
                        SCALE = 223.0
                        MIN_LIMIT = -360
                        MAX_LIMIT = 360
                    else:
                        SCALE = 800.0
                        MIN_LIMIT = -1300
                        MAX_LIMIT = 1300

                MIN_LIMIT = joint.get("min_limit", MIN_LIMIT)
                MAX_LIMIT = joint.get("max_limit", MAX_LIMIT)
                MAX_VELOCITY = joint.get("max_velocity", 40)
                MAX_ACCELERATION = joint.get("max_acceleration", 70)

                cfgini_data.append(f"[AXIS_{AXIS_NAME}]")
                cfgini_data.append(f"MAX_VELOCITY = {MAX_VELOCITY}")
                cfgini_data.append(f"MAX_ACCELERATION = {MAX_ACCELERATION}")
                cfgini_data.append(f"MIN_LIMIT = {MIN_LIMIT}")
                cfgini_data.append(f"MAX_LIMIT = {MAX_LIMIT}")
                cfgini_data.append("")
                break


    for num, joint in enumerate(project["jointnames"]):
        # limit axis configurations
        if num >= num_joints:
            continue

        if joint.get("type") == "rcservo":
            SCALE = 80.0
            MIN_LIMIT = -110
            MAX_LIMIT = 110
            MAX_VELOCITY = 40
            MAX_ACCELERATION = 70
        else:
            MAX_VELOCITY = 40
            MAX_ACCELERATION = 70
            if AXIS_NAME in "ACBUVW":
                SCALE = 223.0
                MIN_LIMIT = -360
                MAX_LIMIT = 360
            else:
                SCALE = 800.0
                MIN_LIMIT = -1300
                MAX_LIMIT = 1300

        AXIS_NAME = joint.get("axis", axis_names[num])
        OUTPUT_SCALE = float(joint.get("scale", SCALE))
        INPUT_SCALE = float(joint.get("enc_scale", OUTPUT_SCALE))
        scales = f"SCALE = {OUTPUT_SCALE}"

        cfgini_data.append(f"[JOINT_{num}]")
        if joint.get("cl", False):
            for key, default in {
                "P": "1.0",
                "I": "0.0",
                "D": "0.0",
                "FF0": "0.0",
                "FF1": "1.0",
                "FF2": "0.01",
                "BIAS": "0.0",
                "DEADBAND": 2.0,
            }.items():
                value = joint.get("pid", {}).get(key, default)
                cfgini_data.append(f"{key} = {value}")

            scales = f"OUTPUT_SCALE = {OUTPUT_SCALE}\nINPUT_SCALE = {INPUT_SCALE}"

        joint_options = {
            "TYPE": joint.get("axis_type", "LINEAR"),
            "MIN_LIMIT": joint.get("min_limit", MIN_LIMIT),
            "MAX_LIMIT": joint.get("max_limit", MAX_LIMIT),
            "MAX_VELOCITY": joint.get("max_velocity", MAX_VELOCITY),
            "MAX_ACCELERATION": joint.get("max_acceleration", MAX_ACCELERATION),
            "STEPGEN_MAXACCEL": joint.get("stepgen_maxaccel", 4000.0),
            "STEPGEN_DEADBAND": joint.get("stepgen_deadband", 1.0 / abs(OUTPUT_SCALE) * 10.0),
            "FERROR": joint.get("ferror", 1.0),
            "MIN_FERROR": joint.get("min_ferror", 0.5),
        }

        if AXIS_NAME in "ACBUVW":
            # rotary axis
            joint_options["TYPE"] = joint.get("axis_type", "ANGULAR")

        for key, value in joint_options.items():
            cfgini_data.append(f"{key} = {value}")
        cfgini_data.append(scales)
        cfgini_data.append("")


        HOME_SEQUENCE = 1
        if AXIS_NAME == "Z":
            HOME_SEQUENCE = 0

        REV = 1.0
        if int(OUTPUT_SCALE) < 0:
            REV = -1.0

        home_options = {
            "HOME_SEQUENCE": joint.get("home_sequence", 10),
            "HOME_SEARCH_VEL": joint.get("home_search_vel", 10.0 * REV),
            "HOME_LATCH_VEL": joint.get("home_latch_vel", 3.0 * REV),
            "HOME_FINAL_VEL": joint.get("home_final_vel", -5.0 * REV),
            "HOME_IGNORE_LIMITS": "YES",
            "HOME_USE_INDEX": "NO",
            "HOME_OFFSET": joint.get("home_offset", 0.0),
            "HOME": 0.0,
        }
        if f"joint.{num}.home-sw-in" in netlist:
            home_options["HOME_SEQUENCE"] = joint.get("home_sequence", HOME_SEQUENCE)

        for key, value in home_options.items():
            cfgini_data.append(f"{key} = {value}")
        cfgini_data.append("")

    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio.ini", "w").write(
        "\n".join(cfgini_data)
    )

def generate_rio_hal(project):
    global netlist
    netlist = []
    for num, din in enumerate(project["dinnames"]):
        din_net = din.get("net")
        if din_net:
            netlist.append(din_net)

    gui = project["jdata"].get("gui", "axis")
    limit_axis = int(project["jdata"].get("axis", 9))
    num_axis = min(project['joints'], limit_axis)
    num_joints = min(project['joints'], 9)

    axis_str = ""
    traj_axis_list = []
    for num in range(min(project["joints"], len(axis_names))):
        # limit axis configurations
        if num >= num_axis:
            continue
        axis_str += axis_names[num]
        traj_axis_list.append(axis_names[num])


    for num, joint in enumerate(project["jointnames"]):
        # limit axis configurations
        if num >= num_joints:
            continue
        AXIS_NAME = joint.get("axis", axis_names[num])
        if AXIS_NAME not in axis_str:
            continue
        if num >= len(traj_axis_list):
            print("append")
            traj_axis_list.append(AXIS_NAME)
        else:
            traj_axis_list[num] = AXIS_NAME

    num_joints = len(traj_axis_list)

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

    ## wcomp test ##
    # loadrt wcomp count=1
    # addf wcomp.0 servo-thread
    # setp wcomp.0.min 2.0
    # setp wcomp.0.max 2.5
    # net pressure wcomp.0.in <= rio.pressure
    # net compressor wcomp.0.out => rio.compressor

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

    mixedInputs = {
        "setup": {
            # component: [inputs:type], [outputs:type], [parameters:type]
            "or2": ({"in0": "bit", "in1": "bit"}, {"out": "bit"}, {}),
            "xor2": ({"in0": "bit", "in1": "bit"}, {"out": "bit"}, {}),
            "and2": ({"in0": "bit", "in1": "bit"}, {"out": "bit"}, {}),
            "maj3": ({"in1": "bit", "in2": "bit", "in3": "bit"}, {"out": "bit"}),
            "mult2": ({"in0": "float", "in1": "float"}, {"out": "float"}),
            "sum2": ({"in0": "float", "in1": "float"}, {"out": "float"}, {"gain0": "float", "gain1": "float", "offset": "float"}),
            "hypot": ({"in0": "float", "in1": "float", "in2": "float"}, {"out": "float"}),
            "comp": ({"in0": "float", "in1": "float"}, {"out": "bit", "equal": "bit"}, {"hyst": "float"}),
            "blend": ({"in1": "float", "in2": "float", "select": "float"}, {"out": "float"}, {"open": "bit"}),
            "bitwise": ({"in0": "u32", "in1": "u32", "select": "u32"}, {"out-and": "u32", "out-or": "u32", "out-xor": "u32", "out-nand": "u32", "out-nor": "u32", "out-xnor": "u32"}),
            "clarke2": ({"a": "float", "b": "float"}, {"x": "float", "y": "float"}),
            "clarke3": ({"a": "float", "b": "float", "c": "float"}, {"x": "float", "y": "float", "h": "float"}),
            "deadzone": ({"in": "float"}, {"out": "float"}, {"center": "float", "threshhold": "float"}),
            "minmax": ({"in": "float", "reset": "bit"}, {"max": "float", "min": "float"}, {}),
        },
        "data": {},
    }
    ignoreList = tuple([f"{mtype}:" for mtype in mixedInputs["setup"]])

    for mtypeBase, msetup in mixedInputs["setup"].items():
        mtypeList = [mtypeBase]
        for oname in msetup[1]:
            mtypeList.append(f"{mtypeBase}.{oname}")
        for mtype in mtypeList:
            for key, inType in {"dinnames": ["bit"], "vinnames": ["float", "u32"]}.items():
                for num, pin in enumerate(project[key]):
                    pname = pin['_name']
                    pin_name = pin.get("name", pname)
                    pin_net = pin.get("net")
                    if pin_net and pin_net.lower().startswith(f"{mtype}:"):
                        if "." in mtype:
                            output = mtype.split(".", 1)[1]
                            mtypeReal = mtype.split(".", 1)[0]
                        else:
                            output = [msetup[1]][0]
                            mtypeReal = mtype

                        if mtypeReal not in mixedInputs['data']:
                            mixedInputs['data'][mtypeReal] = {}
                        options = pin_net.split(":")
                        target_net = options[-1]
                        target_name = target_net.replace(".", "-")
                        if target_name not in mixedInputs['data'][mtypeReal]:
                            mixedInputs['data'][mtypeReal][target_name] = {
                                "output": target_net,
                                "inputs": {},
                                "parameters": {},
                            }
                        inNames = list(msetup[0].keys())
                        paraNames = list(msetup[2].keys())
                        inNum = len(mixedInputs['data'][mtypeReal][target_name]["inputs"])
                        inName = inNames[inNum]
                        if len(options) > 2:
                            inName = options[1]
                        pinSource = f"rio.{pname}"
                        if inName in inNames:
                            if msetup[0][inName] not in inType:
                                print(f"ERROR: input pin has wrong type, must be: {msetup[0][inName]} for {target_name} ({mtypeReal})")
                            if inName in mixedInputs['data'][mtypeReal][target_name]["inputs"]:
                                print(f"ERROR: input pin allready set: {inName} for {target_name} ({mtypeReal})")
                                exit(1)
                            if msetup[0][inName] in {"u32", "s32"}:
                                pinSource = f"{pinSource}-s32"
                            mixedInputs['data'][mtypeReal][target_name]["inputs"][inName] = {
                                "name": pin_name,
                                "pin": pinSource,
                            }
                        elif inName in paraNames:
                            if msetup[2][inName] not in inType:
                                print(f"ERROR: input pin has wrong type, must be: {msetup[2][inName]} for {target_name} ({mtypeReal})")
                            if inName in mixedInputs['data'][mtypeReal][target_name]["parameters"]:
                                print(f"ERROR: parameter pin allready set: {inName} for {target_name} ({mtypeReal})")
                                exit(1)
                            mixedInputs['data'][mtypeReal][target_name]["parameters"][inName] = {
                                "name": pin_name,
                                "pin": pinSource,
                            }
                        else:
                            print(f"ERROR: input pin not exist: {inName} for {target_name} ({mtypeReal})")
                            exit(1)


    for mtype, mdata in mixedInputs['data'].items():
        if mdata:
            cfghal_data.append(f"loadrt {mtype} names={','.join([f'{mtype}-{name}' for name in mdata])}")
            for name, setup in mdata.items():
                cfghal_data.append(f"addf {mtype}-{name} servo-thread")
                inNames = list(mixedInputs["setup"][mtype][0].keys())
                if len(setup["inputs"]) != len(inNames):
                    print(f"ERROR: each {mtype} component needs #{len(inNames)} inputs: {setup['inputs']}")
                    exit(1)
                for inputName, inputPin in setup["inputs"].items():
                    cfghal_data.append(f"net {inputPin['name']} {inputPin['pin']} => {mtype}-{name}.{inputName}")
                for inputName, inputPin in setup["parameters"].items():
                    cfghal_data.append(f"net {inputPin['name']} {inputPin['pin']} => {mtype}-{name}.{inputName}")
                outNames = list(mixedInputs["setup"][mtype][1].keys())
                cfghal_data.append(f"net {name} <= {mtype}-{name}.{outNames[0]}")
                cfghal_data.append(f"net {name} => {setup['output']}")
                netlist.append(setup['output'])
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
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")

        if din_net and din_net.lower().startswith(ignoreList):
            continue

        if din_net and din_net != "spindle.0.speed-out":
            netlist.append(din_net)
            cfghal_data.append(f"net {din_name} <= rio.{dname}")
            cfghal_data.append(f"net {din_name} => {din_net}")
            cfghal_data.append("")

        elif din_net == "spindle.0.speed-out":
            cfghal_data.append(f"net {din_name}-at-speed spindle.0.at-speed <= rio.{dname}")
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
        if dout_net and dout_net != "spindle.0.speed-out":
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
        vin_name = vin.get("name", vname)
        vin_net = vin.get("net")

        if vin_net and din_net.lower().startswith(ignoreList):
            continue

        if function == "spindle-index":
            scale = vin.get("scale", 1.0)
            cfghal_data.append(f"setp rio.{vname}-scale {scale}")
            cfghal_data.append(f"net spindle-position rio.{vname} => spindle.0.revs")
            cfghal_data.append(f"net spindle-index-enable rio.{vname}-index-enable <=> spindle.0.index-enable")
            cfghal_data.append("")
        if vin_net and vin_net != "spindle.0.speed-out":
            netlist.append(vin_net)
            cfghal_data.append(f"net {vin_name} <= {vin_net}")
            cfghal_data.append(f"net {vin_name} => rio.{vname}")
            cfghal_data.append("")

        elif vin_net == "spindle.0.speed-out":
            cfghal_data.append(f"net {vin_name}-get-speed spindle.0.speed-in <= rio.{vname}")
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
setp rio.joint.{num}.deadband 	[JOINT_{num}]STEPGEN_DEADBAND

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
setp rio.joint.{num}.deadband 	[JOINT_{num}]STEPGEN_DEADBAND

net {axis_names[num]}pos-cmd 		<= joint.{num}.motor-pos-cmd 	=> rio.joint.{num}.pos-cmd  
net j{num}pos-fb 		<= rio.joint.{num}.pos-fb 	=> joint.{num}.motor-pos-fb
net j{num}enable 		<= joint.{num}.amp-enable-out 	=> rio.joint.{num}.enable

"""
            )
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio.hal", "w").write(
        "\n".join(cfghal_data)
    )





def generate_custom_postgui_hal(project):
    gui = project["jdata"].get("gui", "axis")

    if gui == "qtdragon":
        prefix = "qtdragon"
    else:
        prefix = "pyvcp"


    customhal_data = []
    customhal_data.append("")

    customhal_data.append(f"# doutnames")
    for num, dout in enumerate(project["doutnames"]):
        dname = dout['_name']
        dout_name = dout.get("name", dname)
        dout_net = dout.get("net")
        if dout_net:
            customhal_data.append(f"net {dname} => {prefix}.{dname}")
        elif not dname.endswith("-index-enable"):
            customhal_data.append(f"net {dname} {prefix}.{dname} rio.{dname}")

    customhal_data.append(f"# dinnames")
    for num, din in enumerate(project["dinnames"]):
        dname = din['_name']
        din_type = din.get("type")
        din_joint = din.get("joint", str(num))
        din_name = din.get("name", dname)
        din_net = din.get("net")
        if din_net:
            customhal_data.append(f"net {dname} => {prefix}.{dname}")
        elif din_type == "alarm" and din_joint:
            pass
        elif din_type == "home" and din_joint:
            pass
        elif not dname.endswith("-index-enable-out"):
            customhal_data.append(
                f"net {dname} rio.{dname} {prefix}.{dname}"
            )

    customhal_data.append(f"# voutnames")
    for num, vout in enumerate(project["voutnames"]):
        vname = vout['_name']
        vout_name = vout.get("name", f"vout{num}")
        vout_net = vout.get("net")
        if vout_net:
            if vout_net == "spindle.0.speed-out" and gui == "qtdragon" and vout['type'] == "vfdbridge":
                customhal_data.append(f"# scale rpm display for qtdragon: rpm -> hz")
                customhal_data.append(f"setp qtdragon.spindle-rpm-scale 0.016666666666")
            else:
                customhal_data.append(f"net {vname} => {prefix}.{vname}")

        elif vout_net != "spindle.0.speed-out":
            customhal_data.append(f"net {vname} rio.{vname} => {prefix}.{vname}-f")

    customhal_data.append(f"# vinnames")
    jogwheel = False
    for num, vin in enumerate(project["vinnames"]):
        vname = vin['_name']
        vin_name = vin.get("name", f"vin{num}")
        vin_net = vin.get("net")
        function = vin.get("function")
        display = vin.get("display", {})
        display_type = display.get("type")
        if vin_net in ["halui.feed-override", "halui.rapid-override", "halui.spindle.0.override", "halui.spindle.1.override"]:
            function = vin_net.split(".")[-1]
        if function == "jogwheel" and not jogwheel:
            jogwheel = True
            if gui != "qtdragon":
                customhal_data.append("")
                customhal_data.append("# jog-wheel")
                customhal_data.append(f"loadrt mux8 count=1")
                customhal_data.append(f"addf mux8.0 servo-thread")
                customhal_data.append(f"setp mux8.0.in1 0.01")
                customhal_data.append(f"setp mux8.0.in2 0.1")
                customhal_data.append(f"setp mux8.0.in4 1.0")
                customhal_data.append(f"net scale1 mux8.0.sel0 <= {prefix}.jog-scale.001")
                customhal_data.append(f"net scale2 mux8.0.sel1 <= {prefix}.jog-scale.01")
                customhal_data.append(f"net scale3 mux8.0.sel2 <= {prefix}.jog-scale.1")
                customhal_data.append(f"net jog-scale <= mux8.0.out")
                customhal_data.append(f"net jog-vel-mode <= {prefix}.jog-mode")
                for jnum in range(min(project["joints"], len(axis_names))):
                    # limit axis configurations
                    if jnum >= num_joints:
                        continue
                    axis_str = axis_names[jnum].lower()
                    customhal_data.append(f"net jog-vel-mode => joint.{jnum}.jog-vel-mode axis.{axis_str}.jog-vel-mode")
                    customhal_data.append(f"net jog-scale => joint.{jnum}.jog-scale axis.{axis_str}.jog-scale")
                    customhal_data.append(f"net jog-counts => joint.{jnum}.jog-counts axis.{axis_str}.jog-counts")
                    #customhal_data.append(f"net jog-enable-{axis_str} axisui.jog.{axis_str} => joint.{jnum}.jog-enable axis.{axis_str}.jog-enable")
                    customhal_data.append(f"net jog-enable-{axis_str} {prefix}.jog-axis.{axis_str} => joint.{jnum}.jog-enable axis.{axis_str}.jog-enable")
                customhal_data.append(f"net jog-counts <= rio.{vname}-s32")
            customhal_data.append("")
        elif function in ["feed-override", "rapid-override", "spindle.0.override", "spindle.1.override"]:
            if gui != "qtdragon":
                customhal_data.append("")
                customhal_data.append(f"# {function}")
                if vin['type'] == "ads1115":
                    customhal_data.append(f"setp rio.{vname}-scale 0.3025")
                else:
                    customhal_data.append(f"setp rio.{vname}-scale 1.0")
                customhal_data.append(f"setp halui.{function}.direct-value 1")
                customhal_data.append(f"setp halui.{function}.scale 0.01")
                customhal_data.append(f"net {function} rio.{vname}-s32 => halui.{function}.counts")
            customhal_data.append("")
        elif function:
            pass
        else:
            scale = vin.get("scale")
            if scale is not None and float(scale) != float(1.0):
                customhal_data.append(f"setp rio.{vname}-scale {scale}")
            offset = vin.get("offset")
            if offset is not None and float(offset) != float(0.0):
                customhal_data.append(f"setp rio.{vname}-offset {offset}")

            if vin_net == "spindle.0.speed-out" and gui == "qtdragon":
                pass
            elif display_type == "meter" and gui == "qtdragon":
                customhal_data.append(f"net {vname} rio.{vname} {prefix}.{vname}_value")
            else:
                if vin_net:
                    customhal_data.append(f"net {vname} {prefix}.{vname}")
                else:
                    customhal_data.append(f"net {vname} rio.{vname} {prefix}.{vname}")


        if vin.get("type") in {"vin_quadencoder", "vin_quadencoderz"}:
            customhal_data.append(f"net {vname}-rpm rio.{vname}-rpm {prefix}.{vname}-rpm")

    if gui != "qtdragon":
        customhal_data.append(f"net zeroxy halui.mdi-command-00 <= {prefix}.zeroxy")
        customhal_data.append(f"net zeroz halui.mdi-command-01 <= {prefix}.zeroz")
        if "motion.probe-input" in netlist:
            customhal_data.append(f"net ztouch halui.mdi-command-02 <= {prefix}.ztouch")

        # spindle.0
        if "hy_vfd" in project["jdata"]:
            customhal_data.append(f"net {prefix}-spindle-at-speed   vfd.spindle-at-speed      => {prefix}.spindle-at-speed")
            customhal_data.append(f"net {prefix}-spindle-speed_fb   vfd.spindle-speed-fb      => {prefix}.spindle-speed")
            customhal_data.append(f"net {prefix}-hycomm-ok          vfd.hycomm-ok             => {prefix}.hycomm-ok")
            customhal_data.append(f"#net {prefix}-spindle-voltage    vfd.rated-motor-voltage   => {prefix}.spindle-voltage")
            customhal_data.append(f"#net {prefix}-spindle-current    vfd.rated-motor-current   => {prefix}.spindle-current")


    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/custom_postgui.hal", "w").write(
        "\n".join(customhal_data)
    )

    postgui_list = []
    postgui_list.append("source custom_postgui.hal")
    open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/postgui_call_list.hal", "w").write(
        "\n".join(postgui_list)
    )


def generate_rio_gui(project):

    gui = project["jdata"].get("gui", "axis")

    if gui == "qtdragon":
        gui_gen = qtdragon()
    else:
        gui_gen = axis()

    cfgxml_data = []
    cfgxml_data += gui_gen.draw_begin()
    cfgxml_data += gui_gen.draw_tabs_begin(["Status", "Inputs", "Outputs"])


    cfgxml_data += gui_gen.draw_tab_begin("Status")

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
            if gui != "qtdragon":
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

        elif vin_net == "spindle.0.speed-out":
            if gui != "qtdragon":
                cfgxml_data += gui_gen.draw_number(f"{vname}", f"{vname}")
    
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
        if din_net == "spindle.0.speed-out":
            cfgxml_data += gui_gen.draw_led(dname, dname)
        elif din_net:
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
            elif vout_net == "spindle.0.speed-out" and gui == "qtdragon":
                pass
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
        elif not vin_net or vin_net != "spindle.0.speed-out":
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
    cfgxml_data += gui_gen.draw_tab_end()


    cfgxml_data += gui_gen.draw_tab_begin("Inputs")
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
        elif not vin_net:
            display = vin.get("display", {})
            display_type = display.get("type")
            if not display_type:
                display_text = display.get("text", vin_name)
                cfgxml_data += gui_gen.draw_number(display_text, vname, display)

    cfgxml_data += gui_gen.draw_tab_end()


    cfgxml_data += gui_gen.draw_tab_begin("Outputs")
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

    cfgxml_data += gui_gen.draw_tab_end()

    cfgxml_data += gui_gen.draw_tabs_end()

    if gui != "qtdragon":
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


    cfgxml_data += gui_gen.draw_end()

    if gui == "qtdragon":
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

    else:
        open(f"{project['LINUXCNC_PATH']}/ConfigSamples/rio/rio-gui.xml", "w").write(
            "\n".join(cfgxml_data)
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
    generate_rio_hal(project)
    generate_rio_ini(project)
    generate_custom_postgui_hal(project)
    generate_rio_gui(project)
    generate_tool_tbl(project)

    os.system(
        f"cp -a generators/linuxcnc_config/linuxcnc.var {project['LINUXCNC_PATH']}/ConfigSamples/rio"
    )
