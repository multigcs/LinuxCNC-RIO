# Plugin: expansion_pcf8574

Expansion to add I/O's via I2C

very slow, do not use for realtime stuff !

```
"expansion": [
    {
        "type": "pcf8574",
        "address": "8'h40",
        "devices": 2,
        "pins": {
            "scl": "PIN_46",
            "sda": "PIN_47"
        }
    }
],
```
