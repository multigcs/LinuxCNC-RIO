# Plugin: joint_stepper

Stepper Joint Output with STEP/DIR/ENABLE(optional) pins

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

optional Encoder-inputs:

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

