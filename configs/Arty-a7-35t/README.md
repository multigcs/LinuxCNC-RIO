# Arty a7-35t

only for testing

using vivado toolchain

https://digilent.com/reference/programmable-logic/arty-a7/start

## pinout
https://digilent.com/reference/programmable-logic/arty-a7/reference-manual

## programmer

```
sudo apt-get install xc3sprog
```

or via sources
```
sudo apt-get install subversion libftdi1-dev
svn checkout https://svn.code.sf.net/p/xc3sprog/code/trunk xc3sprog-code
cd xc3sprog-code
mkdir build
cd build
cmake ../
make
sudo make install
```
