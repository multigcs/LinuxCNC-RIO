# Plugin: interface_w5500

UDP communication interface based on Wiznet W5500 ( HOST <-> UDP <-> W5500 <-> SPI <-> FPGA )

!!! experimental !!!

still has an error rate of 0.02%,

but only the 0.2ms duration, thus much faster than the UDP2SPI bridges


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
### LINUXCNC-RIO with W5500 on Max10 via UDP
[![LINUXCNC-RIO with W5500 on Max10 via UDP](https://img.youtube.com/vi/xcC7Dun8vxE/0.jpg)](https://www.youtube.com/shorts/xcC7Dun8vxE "LINUXCNC-RIO with W5500 on Max10 via UDP")

based on: https://github.com/harout/concurrent-data-capture
