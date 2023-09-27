# Tang Primer 20K minimal config

https://wiki.sipeed.com/hardware/en/tang/tang-primer-20k/primer-20k.html

## Known-Issues:
* openFPGAloader will not work on Raspberry Pi, you have to use another host to flash the FPGA !
* you have to use the gowin toolchain, the opensource one will not work, all required files are generated

```
export PATH=$PATH:/opt/gowin/IDE/bin/
```

The Primer20K is now supported by yosys/nextpnr but it's buggy, plese use the gowin toolchain
```
make gowin_build
```


