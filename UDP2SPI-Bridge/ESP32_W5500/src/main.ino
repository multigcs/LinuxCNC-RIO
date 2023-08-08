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

SPIClass * hspi = NULL;

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

void printMacAddress(byte mac[]) ;

void setup() {

  Serial.begin(115200);

  hspi = new SPIClass(HSPI);
  hspi->begin(HSPI_CLK, HSPI_MISO, HSPI_MOSI, HSPI_SS);
  pinMode(HSPI_SS, OUTPUT);


  IPAddress ip(MYIPADDR);
  IPAddress dns(MYDNS);
  IPAddress gw(MYGW);
  IPAddress sn(MYIPMASK);


  Serial.println("Init Ethernert");

  Serial.println("Configuring Ethernet using STATIC IP address");
  
  
  
  // Static IP setup

  // Ethernet.begin(mac, ip, dns, gw, sn);
    
  // Dynamic IP setup

  if (Ethernet.begin(mac)) {
    Serial.println("DHCP OK!");
  }
  else{
    Serial.println("Failed to configure Ethernet using DHCP");

    if (Ethernet.linkStatus() == LinkOFF) {
      Serial.println("Ethernet cable is not connected.");
    }
    Serial.println("Configuring Ethernet using STATIC IP address");
    Ethernet.begin(mac, ip, dns, gw, sn);
  }

  // You can use Ethernet.init(pin) to configure the CS pin

  //Ethernet.init(10);  // Most Arduino shields
  Ethernet.init(5);   // MKR ETH Shield <---- this worked on ESP32 WROOM32 VSPI CS GPIO5
  //Ethernet.init(0);   // Teensy 2.0
  //Ethernet.init(20);  // Teensy++ 2.0
  //Ethernet.init(15);  // ESP8266 with Adafruit FeatherWing Ethernet
  //Ethernet.init(33);  // ESP32 with Adafruit FeatherWing Ethernet
  
  // Check for Ethernet hardware present

  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); // do nothing, no point running without Ethernet hardware
    }
  }

  // Serial.print("Local IP : ");
  // Serial.println(Ethernet.localIP());
  // Serial.print("Subnet Mask : ");
  // Serial.println(Ethernet.subnetMask());
  // Serial.print("Gateway IP : ");
  // Serial.println(Ethernet.gatewayIP());
  // Serial.print("DNS Server : ");
  // Serial.println(Ethernet.dnsServerIP());

  Serial.println("Ethernet Successfully Initialized");

  Udp.begin(localPort);

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
    IPAddress remote = Udp.remoteIP();
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

}

void printMacAddress(byte mac[]) {
  for (int i = 0; i < 6; ++i) {
    if (mac[i] < 16) Serial.print("0");
    Serial.print(mac[i], HEX);
    if (i < 5) Serial.print(":");
  }
}