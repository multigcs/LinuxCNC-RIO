# Plugin: interface_w5500

UDP communication interface based on Wiznet W5500 ( HOST <-> UDP <-> W5500 <-> SPI <-> FPGA )

!!! experimental !!!

```
"interface": [
    {
        "type": "w5500",
        "ip": "192.168.10.194",
        "port": "2390",
        "pins": {
            "MOSI": "18",
            "MISO": "20",
            "SCK": "23",
            "SEL": "26"
        }
    }
],
```
