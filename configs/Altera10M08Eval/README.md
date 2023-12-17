# Altera10M08Eval

https://www.intel.de/content/www/de/de/products/details/fpga/development-kits/max/10m08-evaluation-kit.html

![hw-setup](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/Altera10M08Eval/hw-setup.jpg)

# SPI connection to the Raspberry
![fpga-spi](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/Altera10M08Eval/fpga-spi.jpg)
![rpi-spi](https://raw.githubusercontent.com/multigcs/LinuxCNC-RIO/main/configs/Altera10M08Eval/rpi-spi.jpg)


| FUNC | FPGA-Pin |Raspberry-GPIO | Raspberry-Pin |
| --- | --- | --- | --- |
| MOSI | 55 | GPIO10 (MOSI) | 19 |
| MISO |  56 |GPIO9 (MISO) | 21 |
| SCK |  59 |GPIO11 (SCLK) | 23 |
| CS |  60 |GPIO7 (CE1) | 26 |
| GND | | | 6 |


### LinuxCNC-Rio on MAX10 with CNC-Shield v3
[![LinuxCNC-Rio on MAX10 with CNC-Shield v3](https://img.youtube.com/vi/DnB64Y6h2Go/0.jpg)](https://www.youtube.com/watch?v=DnB64Y6h2Go&t=1s "LinuxCNC-Rio on MAX10 with CNC-Shield v3")

# Quickstart

## get the source
```
cd /usr/src/
git clone https://github.com/multigcs/LinuxCNC-RIO
cd LinuxCNC-RIO
```

## build the files
```
make CONFIG=configs/Altera10M08Eval/config.json build
```

## generate the gateware

the Quartus have to be installed and in the PATH

```
(
cd Output/Altera10M08Eval/Gateware
make clean all load
)
```

# linuxcnc setup
copy the sample config and components to your cnc host

i using rsync:
```
rsync -avr Output/Altera10M08Eval/LinuxCNC/ 192.168.10.247:/home/cnc/LinuxCNC/
```

## compile and install the linuxcnc component

run on the cnc host
```
sudo halcompile --install /home/cnc/LinuxCNC/Components/rio.c
```

## start linuxcnc
```
linuxcnc LinuxCNC/ConfigSamples/rio/rio.ini
```



