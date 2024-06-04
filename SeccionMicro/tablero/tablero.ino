#include <WiFi.h>
#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>

// Configura tus credenciales WiFi y MySQL
const char* ssid = "Alumnos2.4GHz";
const char* password = "alumnosfcyt";
  char* host = "192.168.1.12"; // Dirección IP de tu servidor MySQL
 char* user = "micro";
 char* pass = "root";
 char* database = "eso"; // Asegúrate de definir correctamente esta variable
WiFiClient client;
MySQL_Connection conn((Client*)&client);

void setup() {
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }
  Serial.println("Conexión WiFi establecida");

     IPAddress serverIP;
      Serial.println("INTENTANDO");
      if (WiFi.status() == WL_CONNECTED) {
  Serial.println("WiFi connected");
} else {
  Serial.println("WiFi connection failed");
}

if (conn.connect(serverIP, 3306, user, pass, database)) {
  Serial.println("Connected to MySQL server");
} else {
  Serial.println("Failed to connect to MySQL server");
}

  if (serverIP.fromString(host)) {
    if (conn.connect(serverIP, 3306, user, pass, database)) {
      Serial.println("Conexión a MySQL exitosa");
      // Aquí puedes ejecutar consultas o realizar otras operaciones con la base de datos
      conn.close();
    } else {
      Serial.println("Error al conectar a MySQL");
    }
  } else {
    Serial.println("Dirección IP inválida");
  }
  
}



void loop() {
  // Tu código aquí
}