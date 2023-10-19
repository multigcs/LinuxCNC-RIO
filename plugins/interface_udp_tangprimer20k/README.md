# Plugin: interface_udp_tangprimer20k

UDP - Ethernet Interface

* only for TangPrimer20K - ext-board with Ethernet (RTL8201)
* very experimental !
* never tested with LinuxCNC, only with the python test-tool
* works only with the gowin toolchain


```
"interface": [
    {
        "type": "udp_tangprimer20k",
        "mac": "06:00:AA:BB:0C:DE",
        "ip": "192.168.10.15",
        "pins": {
            "phyrst": "F10",
            "netrmii_txd_1": "E14",
            "netrmii_txd_0": "D16",
            "netrmii_txen": "E16",
            "netrmii_mdc": "F14",
            "netrmii_rxd_1": "C9",
            "netrmii_rxd_0": "F15",
            "netrmii_rx_crs": "M6",
            "netrmii_clk50m": "A9",
            "netrmii_mdio": "F16"
        }
    }
]
```

## original source

https://github.com/ZiyangYE/verilog_UDP
