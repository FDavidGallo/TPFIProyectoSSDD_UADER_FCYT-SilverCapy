#include "comunicaciones.h"
void EnviarJsonViaHTTPMetodoPost(String ServerAddress, String Payload) {
    HTTPClient Http; // Instanciamos nuestro cliente http
    delay(5000); // Espera 5 segundos antes de conectar
    Http.setTimeout(10000); // Establece un timeout de 10 segundos
    Http.begin(ServerAddress);
    Serial.println("Server Address: " + String(ServerAddress));
    Http.begin(ServerAddress);
    Http.addHeader("Content-Type", "application/json");
    int HttpResponseCode = Http.POST(Payload);

    if (HttpResponseCode > 0) {
        Serial.printf("HTTP Response code: %d\n", HttpResponseCode);
        String response = Http.getString();
        Serial.println(response);
    } else {
        Serial.printf("HTTP Request failed: %s\n", Http.errorToString(HttpResponseCode).c_str());
    }
    Http.end(); //Destruimos nuestro cliente
}
