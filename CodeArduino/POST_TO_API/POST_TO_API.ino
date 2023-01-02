#include <OneWire.h>
#include <DallasTemperature.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* serverName = "http://192.168.1.37:8000/api/post";
const char* ssid = "CAFE VENOM 2.4 G";
const char* password = "@77779999";
// GPIO where the DS18B20 is connected to
const int oneWireBus = D2; 
float vbat=4200;    
// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);
// Pass our oneWire reference to Dallas Temperature sensor 
DallasTemperature sensors(&oneWire);
void setup() {
  // Start the Serial Monitor
  Serial.begin(115200);
  // Start the DS18B20 sensor
  sensors.begin();
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}


void loop() {
  sensors.requestTemperatures(); 
  float temperatureC = sensors.getTempCByIndex(0);

  Serial.print(temperatureC);
  Serial.println("ºC");
  if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;
      http.begin(client, serverName);
      http.addHeader("Content-Type", "application/json");
      int httpResponseCode = http.POST("{\"temp\":"+String(temperatureC)+"}");

      if (httpResponseCode>0) {
                 Serial.print("HTTP Response code: ");
                 Serial.println(httpResponseCode);
                }
                else {
                  Serial.print("Error code: ");
                  Serial.println(httpResponseCode);
                }
                // Free resources
                http.end();
              }
              else {
                Serial.println("WiFi Disconnected");
              }
              //Send an HTTP POST request every 30 seconds
              delay(60000);
}
