# Plugin: modbus

only for HY-VFD's at the moment

## HY-VFD
```
{
    "type": "modbus",
    "protocols": [
        {
            "type": "hyvfd",
            "addr": 1,
            "spindle": 0
        }
    ],
    "baud": 9600,
    "pins": {
        "rx": "P10",
        "tx": "P9",
        "tx_enable": "P8"
    },
    "name": "MODBUS"
}
```

## TODO

* support for more modbus devices
* better plugin structure
* splitting hal code into multiple files
