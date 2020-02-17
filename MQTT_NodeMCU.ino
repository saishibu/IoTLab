// for ESP8266 NocdeMCU 12E.
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//define variables to store ssid, password,broker address and port number
char* ssid = "WIFISSID";
char* password =  "PASSWORD";
const char* mqttBroker = "MQTT Host";
const int mqttPort = 1883;

//create a WiFi client that manages the WiFi connections
WiFiClient espClient;

//create a MQTT Client that handles MQTT Publish & Subscribe
PubSubClient client(espClient);

void setup() {

  Serial.begin(115200);
  //Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {

    delay(500);
    Serial.print("..");

  }

  Serial.println("\nConnected to the WiFi network");

  //Connect to MQTT Broker
  client.setServer(mqttBroker, mqttPort);

  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");

    if (client.connect("ESP32Client" )) {

      Serial.println("connected");

    } else {

      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
      Serial.println("Reset");
      delay(1000);

    }
  }
}
void loop() {
  //Serial.println(WiFi.status());
  //Publish/subscribe to/from the broker once the client is connected
  if (client.connected()) {
  client.publish("TOPIC/Channel", "Hello");
  }
}


