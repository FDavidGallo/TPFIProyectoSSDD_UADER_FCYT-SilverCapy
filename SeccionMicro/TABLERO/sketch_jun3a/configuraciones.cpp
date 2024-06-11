#include "configuraciones.h"

void ConfigurarWifi( const char* Ssid, const char* Password) {
    Serial.begin(9600);
    WiFi.begin(Ssid, Password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Conectando al wifi...");
    }
    Serial.println("Conexión a Wifi exitosa");
}
