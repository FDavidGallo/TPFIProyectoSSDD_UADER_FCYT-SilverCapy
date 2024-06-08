#include <ArduinoJson.h>
#include <Arduino.h>
#include <secrets.h>
#include <WiFi.h>
#include <HTTPClient.h>


 //const char* ssid = "Alumnos2.4GHz";
 //const char* password = "alumnosfcyt";
 //const char* serverAddress = "http://172.21.0.205:5000/data";
void setup() {
    Serial.begin(9600);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
   

}

void loop() {
    float gasto = 123.45; // Valor simulado de gasto
    float presion = 67.89; // Valor simulado de presión
    float vibracion = 12.12; // Valor simulado de vibración
/*
    //DynamicJsonDocument jsonDoc(200);
    jsonDoc["gasto"] = gasto;
    jsonDoc["presion"] = presion;
    jsonDoc["vibracion"] = vibracion;

    String payload;
    //serializeJson(jsonDoc, payload);

    HTTPClient http;
    delay(5000); // Espera 5 segundos antes de conectar
    http.setTimeout(10000); // Establece un timeout de 10 segundos
    http.begin(serverAddress);
    Serial.println("Server Address: " + String(serverAddress));
    http.begin(serverAddress);
    http.addHeader("Content-Type", "application/json");
    int httpResponseCode = http.POST(payload);

    if (httpResponseCode > 0) {
        Serial.printf("HTTP Response code: %d\n", httpResponseCode);
        String response = http.getString();
        Serial.println(response);
    } else {
        Serial.printf("HTTP Request failed: %s\n", http.errorToString(httpResponseCode).c_str());
    }
    http.end();
*/
    delay(5000); // Espera 5 segundos antes de enviar el siguiente dato
}