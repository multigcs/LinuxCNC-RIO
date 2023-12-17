# Colorlight5A-75E tests

https://github.com/q3k/chubby75/blob/master/5a-75e/README.md

### Mini Closed-Loop DC-Servo on LinuxCNC-RIO
[![Mini Closed-Loop DC-Servo on LinuxCNC-RIO](https://img.youtube.com/vi/0cOvUS33U_s/0.jpg)](https://www.youtube.com/shorts/0cOvUS33U_s "Mini Closed-Loop DC-Servo on LinuxCNC-RIO")

## write bitfile

### via USB
```
openFPGALoader -c usb-blaster -r -f --unprotect-flash rio.bit
```

### via Raspberry-GPIO's
```
openFPGALoader -c libgpiod --pins=21:26:16:20 -r -f --unprotect-flash rio.bit
```

