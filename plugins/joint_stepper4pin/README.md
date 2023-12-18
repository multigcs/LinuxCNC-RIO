# Plugin: joint_stepper4pin

## Stepper Joint with 4 output pins for unipolar-stepper or bipolar-stepper with dual full-bridge (like l298)

supports wave(0), full(1) and half(2) step's

```
{
    "type": "joint_stepper4pin",
    "steptype": 1,
    "pins": {
        "1a": "B15",
        "1b": "B16",
        "2a": "C14",
        "2b": "T15"
    }
},
```

