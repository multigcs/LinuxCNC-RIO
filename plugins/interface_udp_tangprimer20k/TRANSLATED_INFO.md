UDP and ARP are now in effect.

**Warning: **Author may get confused when transcribing this page, but the basic functionality is normal. The author is not responsible for any problems in the substitute code.
Features

This is a substitute for the following functions:

    ARP Contacts and Replies, and ARP Requests
    Send and receive UDP packages
    Generating and verifying UDP proofs

Note: 该代码仅适用于 IPv4.

Verilog documents for UDP contact can be found here: udp_18k/src/udp.sv

In the top-level documents for this project, the IP address of the FPGA is 192.168.15.14.

This is the end port of the source end port +1 of the source address.
测试

udp_test.py includes了一个测试用例，已在Linux上测试，但未在Windows上测试。 For this example, please set the IP address to 192.168.15.15. 测试用例的异常常结束很多来自于端口无法打开以及没有来得及监听到收到的包，如果需要的话，请增加延时。
Contact and compatibility

This is a RMII port, only suitable for use with 100M or larger networks, not suitable for use with 10M or larger networks.

The RTL8201 is only suitable for the RXDV functionality of the CRS/CRS_DV connector, which is placed in the phy_rdy position (immediately ready for connection) after the connection is established, and then work can begin. If necessary, you can modify this logic to use either of the other PHY cores.

This code uses System Verilog, and is not compatible with Verilog 2005.
Time Generation and Use

Use Gowin's PLL to generate a 1 MHz time clock, but not any other source code.
Maintenance and Issues

If you encounter any problems, please submit them as soon as possible.
Use and assignment

You can use this number for free, but please withhold the author's information.
Author

LAKKA/JA_P_S
UDP and ARP implementation

Warning: This code was written by the author in a drunken state, so it is very confusing, but basically it works. The author assumes no responsibility for any problems in the code.
Features

This code includes the following features

    Receiving and responding to ARP and ARP requests
    Sending and receiving UDP packets
    Generating and verifying UDP checksums

Note: This code is for IPv4 only.

The Verilog file for the UDP interface is located in udp_18k/src/udp.sv.

This is the top-level file for this project, and the FPGA's IP address is set to 192.168.15.14.

This code sends the received packets to the source port +1 of the source address.
Test

udp_test.py contains a test case, which has been tested on Linux but not on Windows. If you use this test case, set the local IP address to 192.168.15.15. Most abnormal termination of the test case is due to the port not being opened or not listening for incoming packets in a timely manner. If necessary, add a delay.
Interface and Compatibility

This code uses the RMII interface and is for 100M Ethernet only; it is not suitable for 10M Ethernet.

The serial management interface in this code is dedicated to RTL8201. It sets the CRS/CRS_DV pins as RXDV functions, waits for the connection to be established,
sets the phy_rdy bit (i.e., sets the ready interface), and then starts working. This logic can be modified for other PHY chips if needed.

This code is written in System Verilog and is not compatible with Verilog 2005.
Clock Generation and Use

This code uses a Gowin PLL to generate a 1 MHz clock and uses no other primitives.
Warranties and Issues

There is no warranty on this code, but if you find a bug, feel free to submit a problem.
Use and Attribution

This code may be used freely, but please retain the author's information.
Author
LAKKA/JA_P_S
