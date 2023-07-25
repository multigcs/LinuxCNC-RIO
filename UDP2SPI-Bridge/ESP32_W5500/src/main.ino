#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>


#define HSPI_MOSI 13
#define HSPI_MISO 12
#define HSPI_CLK 14
#define HSPI_SS 15

// Set the static IP address to use if the DHCP fails to assign
#define MYIPADDR 192,168,10,28
#define MYIPMASK 255,255,255,0
#define MYDNS 192,168,10,1
#define MYGW 192,168,10,1

#define BUFFER_SIZE 4096


static const int spiClk = 2000000;
// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = { 0xCA, 0xFE, 0xCA, 0xFE, 0xCA, 0xFE };

unsigned int localPort = 2390;      // local port to listen on

// // buffers for receiving and sending data
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; //buffer to hold incoming packet,
// char  ReplyBuffer[] = "acknowledged";       // a string to send back

SPIClass * hspi = NULL;

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

void printMacAddress(byte mac[]) ;

void setup() {

  Serial.begin(115200);

  delay(1000);

  Serial.println("Begin Ethernet");

  // You can use Ethernet.init(pin) to configure the CS pin
  //Ethernet.init(10);  // Most Arduino shields
  Ethernet.init(5);   // MKR ETH Shield <---- this worked on ESP32 WROOM32 VSPI CS GPIO5
  //Ethernet.init(0);   // Teensy 2.0
  //Ethernet.init(20);  // Teensy++ 2.0
  //Ethernet.init(15);  // ESP8266 with Adafruit FeatherWing Ethernet
  // Ethernet.init(33);  // ESP32 with Adafruit FeatherWing Ethernet


  if (Ethernet.begin(mac)) { // Dynamic IP setup
      Serial.println("DHCP OK!");
  }else{
      Serial.println("Failed to configure Ethernet using DHCP");
      // Check for Ethernet hardware present
      if (Ethernet.hardwareStatus() == EthernetNoHardware) {
        Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
        while (true) {
          delay(1); // do nothing, no point running without Ethernet hardware
        }
      }
      if (Ethernet.linkStatus() == LinkOFF) {
        Serial.println("Ethernet cable is not connected.");
      }

        IPAddress ip(MYIPADDR);
        IPAddress dns(MYDNS);
        IPAddress gw(MYGW);
        IPAddress sn(MYIPMASK);
        Ethernet.begin(mac, ip, dns, gw, sn);
        Serial.println("STATIC OK!");
  }
  delay(5000);


  Serial.print("Local IP : ");
  Serial.println(Ethernet.localIP());
  Serial.print("Subnet Mask : ");
  Serial.println(Ethernet.subnetMask());
  Serial.print("Gateway IP : ");
  Serial.println(Ethernet.gatewayIP());
  Serial.print("DNS Server : ");
  Serial.println(Ethernet.dnsServerIP());

  Serial.println("Ethernet Successfully Initialized");

  // Serial.print("MOSI: ");
  // Serial.println(MOSI);
  // Serial.print("MISO: ");
  // Serial.println(MISO);
  // Serial.print("SCK: ");
  // Serial.println(SCK);
  // Serial.print("SS: ");
  // Serial.println(SS);  

  // SPI.begin(1); // Use SPI Bus 2 (VSPI)

  // start the Ethernet and UDP:
  


  hspi = new SPIClass(HSPI);
  hspi->begin(HSPI_CLK, HSPI_MISO, HSPI_MOSI, HSPI_SS);

  pinMode(HSPI_SS, OUTPUT);

  // hspi = new SPIClass(HSPI);
  // hspi->begin(HSPI_CLK, HSPI_MISO, HSPI_MOSI, HSPI_SS);
  // pinMode(HSPI_SS, OUTPUT);
  
  // // Check for Ethernet hardware present
  // if (Ethernet.hardwareStatus() == EthernetNoHardware) {
  //     Serial.println(
  //             "Ethernet shield was not found.  Sorry, can't run without hardware. :(");
  //     while (true) {
  //         delay(1); // do nothing, no point running without Ethernet hardware
  //     }
  // }
  // if (Ethernet.linkStatus() == LinkOFF) {
  //     Serial.println("Ethernet cable is not connected.");
  // }
  
  IPAddress ip(MYIPADDR);
  IPAddress dns(MYDNS);
  IPAddress gw(MYGW);
  IPAddress sn(MYIPMASK);

  Ethernet.begin(mac, ip, dns, gw, sn);

  Udp.begin(localPort);

  Serial.println("STATIC OK!");


  Serial.println("Ethernet connected");
  Serial.print("MAC Address: ");
  printMacAddress(mac);
  Serial.println();
  
  // Print the assigned IP address
  Serial.print("IP Address: ");
  Serial.println(Ethernet.localIP());
  Serial.println("UDP2SPI Bridge for LinuxCNC - RIO");

}

void loop() {
  // if there's data available, read a packet
  

  int packetSize = Udp.parsePacket();
  if (packetSize)
  {

    // Serial.print("Received packet of size ");
    // Serial.println(packetSize);
    // Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    // for (int i = 0; i < 4; i++)
    // {
    //   Serial.print(remote[i], DEC);
    //   if (i < 3)
    //   {
    //     Serial.print(".");
    //   }
    // }
    // Serial.print(", port ");
    // Serial.println(Udp.remotePort());

    // read the packet into packetBufffer
    int len = Udp.read(packetBuffer, BUFFER_SIZE);
    hspi->beginTransaction(SPISettings(spiClk, MSBFIRST, SPI_MODE0));
    digitalWrite(hspi->pinSS(), LOW);
    hspi->transfer(packetBuffer, len);
    digitalWrite(hspi->pinSS(), HIGH);
    hspi->endTransaction();
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    Udp.write((uint8_t*)packetBuffer, len);
    Udp.endPacket();
  }

  //delay(10);

  // if (Serial.available() > 0) {
  //   int len = 0;
  //   while (Serial.available() > 0 && len < BUFFER_SIZE) {
  //       packetBuffer[len] = Serial.read();
  //       len++;
  //   }
  //   if (len < BUFFER_SIZE) {
  //       Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
  //       Udp.write(packetBuffer);
  //       Udp.endPacket();
  //   }
  // }
}

void printMacAddress(byte mac[]) {
  for (int i = 0; i < 6; ++i) {
    if (mac[i] < 16) Serial.print("0");
    Serial.print(mac[i], HEX);
    if (i < 5) Serial.print(":");
  }
}