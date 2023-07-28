# Plugin: expansion_shiftreg

Expansion to add I/O's via shiftregister's


```
"expansion": [
    {
        "type": "shiftreg",
        "speed": "1000000",
        "pins": {
            "clock": "G2",
            "load": "G1",
            "in": "C4",
            "out": "H2"
        }
    }
],
```


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



# Verilog-Flowchart
![graphviz](./expansion_shiftreg.svg)

