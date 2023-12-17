# Plugin: dout_bit

## Digital Output Pin (1bit)

```
{
    "type": "dout_bit",
    "name": "LED3",
    "invert": "true",
    "pin": "PIN_135"
},
```

##  extended setup:

for better generated sample config's

you can also connect the pin to a hal-net

```
{
    "type": "dout_bit",
    "name": "spindle-enable",
    "net": "spindle.0.on",
    "invert": true,
    "pin": "38"
},
```
this will add the pin in the sample .hal to spindle.0.on (Spindle-On/Off):

```
net spindle-enable <= spindle.0.on
net spindle-enable => rio.dout0
```
