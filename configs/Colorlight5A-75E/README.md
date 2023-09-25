# Colorlight5A-75E tests

https://github.com/q3k/chubby75/blob/master/5a-75e/README.md


## write bitfile

### via USB
```
openFPGALoader -c usb-blaster -r -f --unprotect-flash rio.bit
```

### via Raspberry-GPIO's
```
openFPGALoader -c libgpiod --pins=21:26:16:20 --detect
```

