# Plugin: wled

## LED Output via ws2812 (wled) protocol,

each color is one output (Green/Blue/Red)

you can also using strips with many LED's

[![LinuxCNC-RIO mit ws2812 stripe an einem Max10 FPGA](https://img.youtube.com/vi/wu29vGSSK_0/0.jpg)](https://www.youtube.com/shorts/wu29vGSSK_0 "LinuxCNC-RIO mit ws2812 stripe an einem Max10 FPGA")


```
{
    "type": "dout_wled",
    "leds": 3,
    "pin": "PIN_41"
},
```

##  extended setup:

you can add a list of net names,
    1. is LED0-Green
    2. is LED0-Blue
    3. is LED0-Red
    3. is LED1-Green
    ...

```
{
    "type": "dout_wled",
    "leds": 3,
    "net": ["motion.digital-out-00", "motion.digital-out-01", "motion.digital-out-02", "motion.digital-out-03", "motion.digital-out-04", "motion.digital-out-05"],
    "pin": "PIN_41"
},
```
