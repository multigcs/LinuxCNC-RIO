
#define ETH_CLK_MODE ETH_CLOCK_GPIO17_OUT
#define ETH_PHY_POWER 12

#include <ETH.h>
#include <ESPmDNS.h>
#include <WiFiUdp.h>
#include <SPI.h>

#define HSPI_MOSI 13
#define HSPI_MISO 16
#define HSPI_CLK 14
#define HSPI_SS 15
#define BUFFER_SIZE 4096
static const int spiClk = 2000000;
char packetBuffer[BUFFER_SIZE];
unsigned int localPort = 2390;
SPIClass * hspi = NULL;

WiFiUDP Udp;


void setup(){
    Serial.begin(115200);
    while (!Serial);

    ETH.begin();

    /*
    // setup static ip
    IPAddress myIP(192, 168, 10, 132);
    IPAddress myGW(192, 168, 10, 1);
    IPAddress mySN(255, 255, 255, 0);
    ETH.config(myIP, myGW, mySN);
    */

    Udp.begin(localPort);
    hspi = new SPIClass(HSPI);
    hspi->begin(HSPI_CLK, HSPI_MISO, HSPI_MOSI, HSPI_SS);
    pinMode(HSPI_SS, OUTPUT);

    Serial.println("UDP2SPI Bridge for LinuxCNC - RIO");
}

void loop() {
    int packetSize = Udp.parsePacket();
    if (packetSize) {
        IPAddress remoteIp = Udp.remoteIP();
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

    if (Serial.available() > 0) {
        int len = 0;
        while (Serial.available() > 0 && len < BUFFER_SIZE) {
            packetBuffer[len] = Serial.read();
            len++;
        }
        if (len < BUFFER_SIZE) {
            hspi->beginTransaction(SPISettings(spiClk, MSBFIRST, SPI_MODE0));
            digitalWrite(hspi->pinSS(), LOW);
            hspi->transfer(packetBuffer, len);
            digitalWrite(hspi->pinSS(), HIGH);
            hspi->endTransaction();
            Serial.write((uint8_t*)packetBuffer, len);
        }
    }
}
