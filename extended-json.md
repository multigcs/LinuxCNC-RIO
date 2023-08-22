# extended json config examples

## stepper joint with defined scale and acceleration

<table border=1>
<tr>
<th>source</th>
<th colspan=4>generated</th>
</tr><tr>
<th>config.json</th>
<th>rio.hal</th>
<th>rio.ini</th>
<th>custom_postgui.hal</th>
<th>rio-gui.xml</th>
</tr>
<tr>
<td>

```json
{
    "type": "joint_stepper",
    "scale": -200,
    "max_acceleration": 100,
    "cl": false,
    "pins": {
        "step": "79",
        "dir": "77"
    }
},
```

</td>
<td>

```text
# Joint 0 setup

setp rio.joint.0.scale 		[JOINT_0]SCALE
setp rio.joint.0.maxaccel 	[JOINT_0]STEPGEN_MAXACCEL

net Xpos-cmd 		<= joint.0.motor-pos-cmd 	=> rio.joint.0.pos-cmd  
net j0pos-fb 		<= rio.joint.0.pos-fb 	=> joint.0.motor-pos-fb
net j0enable 		<= joint.0.amp-enable-out 	=> rio.joint.0.enable
```

</td>
<td>

```ini
[JOINT_0]
TYPE = LINEAR
MIN_LIMIT = -1300
MAX_LIMIT = 1300
MAX_VELOCITY = 40
MAX_ACCELERATION = 100
STEPGEN_MAXACCEL = 4000.0
SCALE = -200
FERROR = 1.0
MIN_FERROR = 0.5

#HOME_SEARCH_VEL = -10.0
#HOME_LATCH_VEL = -3.0
#HOME_FINAL_VEL = 5.0
#HOME_IGNORE_LIMITS = YES
#HOME_USE_INDEX = NO
#HOME_OFFSET = 0.0
#HOME = 0.0
#HOME_SEQUENCE = 1
```

</td>
<td>
</td>
<td>
</td>

</tr>
</table>


## digital input pin used as home-switch

<table border=1>
<tr>
<th>source</th>
<th colspan=4>generated</th>
</tr><tr>
<th>config.json</th>
<th>rio.hal</th>
<th>rio.ini</th>
<th>custom_postgui.hal</th>
<th>rio-gui.xml</th>
</tr>
<tr>

<td>

```json
{
    "type": "din_bit",
    "name": "home-x",
    "net": "joint.0.home-sw-in",
    "invert": false,
    "pullup": true,
    "pin": "26"
},
```

</td>
<td>

```text
net home-x <= rio.home-x
net home-x => joint.0.home-sw-in
```

</td>
<td>
this also activates the homing setup in the ini file for this axis

```ini
HOME_SEARCH_VEL = -10.0
HOME_LATCH_VEL = -3.0
HOME_FINAL_VEL = 5.0
HOME_IGNORE_LIMITS = YES
HOME_USE_INDEX = NO
HOME_OFFSET = 0.0
HOME = 0.0
HOME_SEQUENCE = 1
```

</td>
<td>

```text
net home-x => pyvcp.home-x
```

</td>
<td>

```xml
<hbox>
  <relief>RAISED</relief>
  <bd>2</bd>
  <led>
    <halpin>"home-x"</halpin>
    <size>16</size>
    <on_color>"green"</on_color>
    <off_color>"black"</off_color>
  </led>
  <label>
    <text>"home-x"</text>
  </label>
</hbox>
```

</td>

</tr>
</table>

## digital output pin configured as spindle enable signal

<table border=1>
<tr>
<th>source</th>
<th colspan=4>generated</th>
</tr><tr>
<th>config.json</th>
<th>rio.hal</th>
<th>rio.ini</th>
<th>custom_postgui.hal</th>
<th>rio-gui.xml</th>
</tr>
<tr>

<td>

```json
{
    "name": "spindle-enable",
    "net": "spindle.0.on",
    "invert": true,
    "pin": "56",
    "type": "dout_bit"
},
```

</td>
<td>

```text
net spindle-enable <= spindle.0.on
net spindle-enable => rio.spindle-enable
```

</td>
<td>


</td>
<td>

```text
net spindle-enable => pyvcp.spindle-enable
```

</td>
<td>

```xml
  <hbox>
    <relief>RAISED</relief>
    <bd>2</bd>
    <label>
      <text>"spindle-speed"</text>
    </label>
    <number>
        <halpin>"spindle-speed"</halpin>
        <font>("Helvetica",18)</font>
        <format>"05.2f"</format>
    </number>
  </hbox>
```

</td>
</tr>
</table>


## two digital input pins used as tool-probe and touch-probe

normaly you can only link one pin to one signal,
but you can add a hal-component like the OR2 (logical OR)

<table border=1>
<tr>
<th>source</th>
<th colspan=4>generated</th>
</tr><tr>
<th>config.json</th>
<th>rio.hal</th>
<th>rio.ini</th>
<th>custom_postgui.hal</th>
<th>rio-gui.xml</th>
</tr>
<tr>
<td>

```json
{
    "type": "din_bit",
    "name": "tool-probe",
    "net": "OR2:motion.probe-input",
    "invert": true,
    "pullup": true,
    "pin": "29"
},
{
    "type": "din_bit",
    "name": "touch-probe",
    "net": "OR2:motion.probe-input",
    "debounce": true,
    "invert": true,
    "pullup": true,
    "pin": "53"
},
```

</td>
<td>

```text
loadrt or2 names=or2-motion-probe-input
addf or2-motion-probe-input servo-thread
net tool-probe rio.tool-probe => or2-motion-probe-input.in0
net touch-probe rio.touch-probe => or2-motion-probe-input.in1
net motion-probe-input <= or2-motion-probe-input.out
net motion-probe-input => motion.probe-input
```

</td>
<td>


</td>
<td>

```text
net tool-probe => pyvcp.tool-probe
net touch-probe => pyvcp.touch-probe
```

</td>
<td>

```xml
  <hbox>
    <relief>RAISED</relief>
    <bd>2</bd>
    <led>
      <halpin>"tool-probe"</halpin>
      <size>16</size>
      <on_color>"green"</on_color>
      <off_color>"black"</off_color>
    </led>
    <label>
      <text>"tool-probe"</text>
    </label>
  </hbox>
  <hbox>
    <relief>RAISED</relief>
    <bd>2</bd>
    <led>
      <halpin>"touch-probe"</halpin>
      <size>16</size>
      <on_color>"green"</on_color>
      <off_color>"black"</off_color>
    </led>
    <label>
      <text>"touch-probe"</text>
    </label>
  </hbox>
```

</td>
</tr>
</table>


## pin used as pwm output

if only a 'name' is configured and no 'net',
the pin will linked in the custom_postgui.hal to a gui widget

<table border=1>
<tr>
<th>source</th>
<th colspan=4>generated</th>
</tr><tr>
<th>config.json</th>
<th>rio.hal</th>
<th>rio.ini</th>
<th>custom_postgui.hal</th>
<th>rio-gui.xml</th>
</tr>
<tr>
<td>

```json
 {
    "type": "vout_pwm",
    "name": "pwm1",
    "min": "0",
    "max": "10000",
    "invert": true,
    "pins": {
        "pwm": "76"
    }
},
```

</td>
<td>


</td>
<td>


</td>
<td>

```text
net pwm1 rio.pwm1 => pyvcp.pwm1-f
```

</td>
<td>

```xml
  <hbox>
    <relief>RAISED</relief>
    <bd>2</bd>
    <scale>
      <halpin>"pwm1"</halpin>
      <resolution>0.1</resolution>
      <orient>HORIZONTAL</orient>
      <initval>0</initval>
      <min_>0</min_>
      <max_>100</max_>
      <param_pin>1</param_pin>
    </scale>
    <label>
      <text>"pwm1 (vout_pwm)"</text>
    </label>
  </hbox>
```

</td>
</tr>
</table>


## pin used as frequency measurement input for a water-flow sensor

you can add display option to configure the generated widget

<table border=1>
<tr>
<th>source</th>
<th colspan=4>generated</th>
</tr><tr>
<th>config.json</th>
<th>rio.hal</th>
<th>rio.ini</th>
<th>custom_postgui.hal</th>
<th>rio-gui.xml</th>
</tr>
<tr>
<td>

```json
{
    "name": "flow",
    "type": "vin_frequency",
    "scale": 33.0,
    "display": {
        "type": "meter",
        "text": "Water",
        "subtext": "ml/h",
        "min": 0,
        "max": 200,
        "threshold": 90,
        "region": [
            [90, 200, "green"],
            [70, 90, "yellow"],
            [0, 70, "red"]
        ]
    },
    "debounce": true,
    "pin": "30",
    "pullup": true,
    "freq_min": 2
},
```

</td>
<td>


</td>
<td>


</td>
<td>

```xml
setp rio.flow-scale 33.0
net flow rio.flow pyvcp.flow
```

</td>
<td>

```xml
<hbox>
    <relief>RAISED</relief>
    <bd>2</bd>
    <meter>
      <halpin>"flow"</halpin>
      <text>"Water"</text>
      <subtext>"ml/h"</subtext>
      <size>150</size>
      <min_>0</min_>
      <max_>200</max_>
      <region1>(90,200,"green")</region1>
      <region2>(70,90,"yellow")</region2>
      <region3>(0,70,"red")</region3>
    </meter>
</hbox>
```

</td>
</tr>
</table>
