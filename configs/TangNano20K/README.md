# Tang Nano 20K minimal config

https://wiki.sipeed.com/hardware/en/tang/tang-nano-20k/nano-20k.html

## Known-Issues:
* openFPGAloader will not work on Raspberry Pi, you have to use another host to flash the FPGA !
* you have to use the gowin toolchain, the opensource one will not work, all required files are generated

```
export PATH=$PATH:/opt/gowin/IDE/bin/
```
