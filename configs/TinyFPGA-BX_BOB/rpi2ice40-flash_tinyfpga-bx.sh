#!/bin/bash
#
# flashing TinyFPGA-BX from raspberry over SPI
# please use the latest flashrom from: https://github.com/flashrom/flashrom.git
#
#


sudo rmmod spidev
sudo rmmod spi_bcm2835
sudo modprobe spi_bcm2835
sudo modprobe spidev

echo 25 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio25/direction
sleep 1

dd if=/dev/zero of=/tmp/_flash.bin  bs=1M  count=1
dd if=$1 conv=notrunc of=/tmp/_flash.bin

flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=20000 -w /tmp/_flash.bin || \
flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=20000 -w /tmp/_flash.bin


echo in > /sys/class/gpio/gpio25/direction


