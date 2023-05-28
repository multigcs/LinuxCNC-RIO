
#define ETH_CLK_MODE ETH_CLOCK_GPIO17_OUT
#define ETH_PHY_POWER 12

#include <ETH.h>
#include <ESPmDNS.h>
#include <WiFiUdp.h>
#include <SPI.h>

static const int spiClk = 2000000;

#define HSPI_MOSI 13
#define HSPI_MISO 16
#define HSPI_CLK 14
#define HSPI_SS 15
#define BUFFER_SIZE 4096

char packetBuffer[BUFFER_SIZE];
unsigned int localPort = 2390;

WiFiUDP Udp;
SPIClass * hspi = NULL;


void setup(){
    delay(250);
    //Serial.begin(115200);
    Serial.begin(2000000);
    while (!Serial);

    ETH.begin();

    Udp.begin(localPort);
    hspi = new SPIClass(HSPI);
    hspi->begin(HSPI_CLK, HSPI_MISO, HSPI_MOSI, HSPI_SS);
    pinMode(HSPI_SS, OUTPUT);

    Serial.println("UDP2SPI Bridge");
}


void loop(){
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
