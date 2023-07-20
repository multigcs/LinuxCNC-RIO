# Plugin: joint_stepper

## Stepper Joint Output with STEP/DIR/ENABLE(optional) pins

```
{
    "type": "stepper",
    "cl": false,
    "pins": {
        "step": "B15",
        "dir": "C14",
        "en": "T15"
    }
},
```

## optional Encoder-inputs:

```
{
    "type": "stepper",
    "cl": true,
    "pins": {
        "step": "B15",
        "dir": "C14",
        "en": "T15"
        "enc_a": "T16"
        "enc_b": "T17"
    }
},
```

##  extended setup:

you can also add a scale parameter to get a better sample config

```
{
    "type": "stepper",
    "cl": false,
    "scale": -800,
    "pins": {
        "step": "63",
        "dir": "86"
    }
},
```

this will set the right SCALE parameter in you .ini

use negative values to reverse the direction

```
[AXIS_X]
MAX_VELOCITY = 40
MAX_ACCELERATION = 70
MIN_LIMIT = -1300
MAX_LIMIT = 1300


[JOINT_0]

TYPE = LINEAR
MIN_LIMIT = -1300
MAX_LIMIT = 1300
MAX_VELOCITY = 40
MAX_ACCELERATION = 70
STEPGEN_MAXACCEL = 4000.0
SCALE = -800
FERROR = 1.0
MIN_FERROR = 0.5
```

