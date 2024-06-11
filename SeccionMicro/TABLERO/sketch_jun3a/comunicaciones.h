#ifndef COMUNICACIONES_H
#define COMUNICACIONES_H

#include <WiFi.h>  //Necesaria para usar el wifi
#include <HTTPClient.h> // Necesaria para aplicar el protocolo HTTP
void EnviarJsonViaHTTPMetodoPost(String ServerAddress, String Payload);

#endif // COMUNICACIONES_H
