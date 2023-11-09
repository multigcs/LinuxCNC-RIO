#!/bin/bash
#
# flashing ICE40 from raspberry over SPI
#  for the Olimex ICE40HX8K-EVB board
#


sudo rmmod spidev
sudo rmmod spi_bcm2835
sudo modprobe spi_bcm2835
sudo modprobe spidev

echo 24 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio24/direction

dd if=/dev/zero of=/tmp/_flash.bin  bs=2M  count=1
dd if=$1 conv=notrunc of=/tmp/_flash.bin

flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=20000 -w /tmp/_flash.bin


echo in > /sys/class/gpio/gpio24/direction




