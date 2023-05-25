# Plugin: vout_udpoti

Variable-Output using digital poti with SPI Interface (like MCP413X/415X/423X/425X)

```
{
    "type": "spipoti",
    "bits": "8",
    "speed": "1000000",
    "pins": {
        "MOSI": "A1",
        "SCLK": "A3",
        "CS": "A4"
    }
},
```

but have a problem with my X9C104, it need only 31 steps for the full range,
don't know why :(
