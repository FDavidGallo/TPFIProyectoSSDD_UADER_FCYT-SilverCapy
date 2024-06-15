
/***
 *                                                                                                                                                              
 *       d888888o.    8 8888 8 8888 `8.`888b           ,8' 8 8888888888   8 888888888o.      ,o888888o.           .8.          8 888888888o  `8.`8888.      ,8'   
 *     .`8888:' `88.  8 8888 8 8888  `8.`888b         ,8'  8 8888         8 8888    `88.    8888     `88.        .888.         8 8888    `88. `8.`8888.    ,8'  
 *     8.`8888.   Y8  8 8888 8 8888   `8.`888b       ,8'   8 8888         8 8888     `88 ,8 8888       `8.      :88888.        8 8888     `88  `8.`8888.  ,8'   
 *     `8.`8888.      8 8888 8 8888    `8.`888b     ,8'    8 8888         8 8888     ,88 88 8888               . `88888.       8 8888     ,88   `8.`8888.,8'    
 *      `8.`8888.     8 8888 8 8888     `8.`888b   ,8'     8 888888888888 8 8888.   ,88' 88 8888              .8. `88888.      8 8888.   ,88'    `8.`88888'     
 *       `8.`8888.    8 8888 8 8888      `8.`888b ,8'      8 8888         8 888888888P'  88 8888             .8`8. `88888.     8 888888888P'      `8. 8888      
 *        `8.`8888.   8 8888 8 8888       `8.`888b8'       8 8888         8 8888`8b      88 8888            .8' `8. `88888.    8 8888              `8 8888      
 *    8b   `8.`8888.  8 8888 8 8888        `8.`888'        8 8888         8 8888 `8b.    `8 8888       .8' .8'   `8. `88888.   8 8888               8 8888      
 *    `8b.  ;8.`8888  8 8888 8 8888         `8.`8'         8 8888         8 8888   `8b.     8888     ,88' .888888888. `88888.  8 8888               8 8888      
 *     `Y8888P ,88P'  8 8888 8 888888888888  `8.`          8 888888888888 8 8888     `88.    `8888888P'  .8'       `8. `88888. 8 8888               8 8888      
 */





/***
 *     #                                                             
 *     #        #  #####   #####   ######  #####   #    ##     ####  
 *     #        #  #    #  #    #  #       #    #  #   #  #   #      
 *     #        #  #####   #    #  #####   #    #  #  #    #   ####  
 *     #        #  #    #  #####   #       #####   #  ######       # 
 *     #        #  #    #  #   #   #       #   #   #  #    #  #    # 
 *     #######  #  #####   #    #  ######  #    #  #  #    #   ####  
 *                                                                   
 */

#include <WiFi.h>  //Necesaria para usar el wifi
#include <HTTPClient.h> // Necesaria para aplicar el protocolo HTTP
#include <ArduinoJson.h>// Necesaria para manipular y crear archivos Json
#include "secrets.h"    // Contiene nuestras claves Ultrasecretas
// Secrets.h tiene las siguientes cosas interesantes:
//const char* Ssid = " tu red wifi";
//const char* Password = " contraseña de tu red wifi";
//const char* ServerAddress = "ip de tu servidor"; // Cambia la dirección IP con la de tu PC
#include "configuraciones.h" // Tiene nuestras configuraciones
#include "comunicaciones.h"  // Tiene las funciones para comunicar al esp con el servidor

/***
 *     #     #                                                                                                                                
 *     #     #    ##    #####   #    ##    #####   #       ######   ####        ####   #        ####   #####     ##    #       ######   ####  
 *     #     #   #  #   #    #  #   #  #   #    #  #       #       #           #    #  #       #    #  #    #   #  #   #       #       #      
 *     #     #  #    #  #    #  #  #    #  #####   #       #####    ####       #       #       #    #  #####   #    #  #       #####    ####  
 *      #   #   ######  #####   #  ######  #    #  #       #            #      #  ###  #       #    #  #    #  ######  #       #            # 
 *       # #    #    #  #   #   #  #    #  #    #  #       #       #    #      #    #  #       #    #  #    #  #    #  #       #       #    # 
 *        #     #    #  #    #  #  #    #  #####   ######  ######   ####        ####   ######   ####   #####   #    #  ######  ######   ####  
 *                                                                                                                                            
 */
  String Direccion = String(DireccionDelServidor); // Esta es la dirección general  del servidor, a esto le sumaremos
                                            // La subdirección especí fica a la que debe "pegarle" el Esp32  ej "+ "String Direccion = String(ServerAddress)+"/home";"
                                            // Para nuestro caso serán:
                                            //  1-Partida 1; 2-Partida 2; 3- Partida 3, 4.- Partida 4 
  int NumeroDePartida=1 ;// Por defecto iniciamos en la partida uno
  int NumeroMovimiento=0 ;// En un inicio no se ha realizado ningún Movimiento
  String Movimiento;

/***
 *     #######                                                                                       
 *     #        #    #  #    #   ####   #   ####   #    #       ####   ######  #####  #    #  #####  
 *     #        #    #  ##   #  #    #  #  #    #  ##   #      #       #         #    #    #  #    # 
 *     #####    #    #  # #  #  #       #  #    #  # #  #       ####   #####     #    #    #  #    # 
 *     #        #    #  #  # #  #       #  #    #  #  # #           #  #         #    #    #  #####  
 *     #        #    #  #   ##  #    #  #  #    #  #   ##      #    #  #         #    #    #  #      
 *     #         ####   #    #   ####   #   ####   #    #       ####   ######    #     ####   #      
 *                                                                                                   
 */


void setup() {
   // ATENCIÓN, la comunicación serial se configura dentro  de "ConfigurarWifi"
   ConfigurarWifi(Ssid, Password);

}


/***
 *     #######                                                 #                               
 *     #        #    #  #    #   ####   #   ####   #    #      #         ####    ####   #####  
 *     #        #    #  ##   #  #    #  #  #    #  ##   #      #        #    #  #    #  #    # 
 *     #####    #    #  # #  #  #       #  #    #  # #  #      #        #    #  #    #  #    # 
 *     #        #    #  #  # #  #       #  #    #  #  # #      #        #    #  #    #  #####  
 *     #        #    #  #   ##  #    #  #  #    #  #   ##      #        #    #  #    #  #      
 *     #         ####   #    #   ####   #   ####   #    #      #######   ####    ####   #      
 *                                                                                             
 */

void loop() {
    int NumeroDeMovimiento=12;
    DynamicJsonDocument jsonDoc(200);
   
    jsonDoc["Movimiento"] = "PEPE";
    jsonDoc["ReyBlanco"] = "gasto";
    jsonDoc["ReyNegro"] = "presion";
    jsonDoc["NumeroDeMovimiento"] = NumeroDeMovimiento;

    String SPayload;
    String ServerAddress=Direccion+"1";
    serializeJson(jsonDoc, SPayload);
    EnviarJsonViaHTTPMetodoPost(ServerAddress,SPayload);
    delay(5000); // Espera 5 segundos antes de enviar el siguiente dato
}
