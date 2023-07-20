# Plugin: din_bit

## Digital Input Pin (1bit)

```
"din": [
    {
        "comment": "J1.1",
        "pin": "C4"
    }
]
```

##  extended setup:

for better generated sample config's

you can also connect the pin to a hal-net

```
{
    "name": "home-x",
    "net": "joint.0.home-sw-in",
    "invert": true,
    "pullup": true,
    "pin": "26"
},
```

this will add the pin in the generated .hal to joint.0.home-sw-in (Homing-Switch for X-Axis):

```
net home-x <= rio.din0
net home-x => joint.0.home-sw-in
```

