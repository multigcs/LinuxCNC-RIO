# Plugin: expansion_shiftreg

Expansion to add I/O's via shiftregister's


```
"expansion": [
    {
        "type": "shiftreg",
        "speed": "1000000",
        "bits": "8",
        "pins": {
            "clock": "G2",
            "load": "G1",
            "in": "C4",
            "out": "H2"
        }
    }
],
```

you can use this extra IO's like this:
```
        {
            "type": "dout_bit",
            "name": "LED0",
            "invert": "true",
            "pin": "EXPANSION0_OUTPUT[0]"
        },
        {
            "type": "dout_bit",
            "name": "LED1",
            "invert": "true",
            "pin": "EXPANSION0_OUTPUT[0]"
        },
```


### LinuxCNC-RIO mit Unipolar Steppern über Schieberegister am FPGA 
[![LinuxCNC-RIO mit Unipolar Steppern über Schieberegister am FPGA ](https://img.youtube.com/vi/NlLd5CRCOac/0.jpg)](https://www.youtube.com/shorts/NlLd5CRCOac "LinuxCNC-RIO mit Unipolar Steppern über Schieberegister am FPGA ")


## Output-Expansion with 74HC595:

| EXP | 74HC595 | FUNC |
| --- | --- | --- |
| out | 14 | DS |
| in |  | |
| clock | 11 | SH_CP / SRCLK |
| load | 12 | ST_CP / RCLK |


## Input-Expansion with 74HC165:

| EXP | 74HC165 | FUNC |
| --- | --- | --- |
| out |  | |
| in |  | SER |
| clock | 2 | CLK |
| load |  | SH/LD |


# expansion_shiftreg.v
![graphviz](./expansion_shiftreg.svg)

