



all: build flash monitor


build:
	platformio run

flash:
	platformio run --target upload

monitor:
	gtkterm --port /dev/ttyUSB0 --speed 115200


