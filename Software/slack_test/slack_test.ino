/*
  Web client

  This sketch connects to a website (http://www.google.com)
  using a WiFi shield.

  This example is written for a network using WPA encryption. For
  WEP or WPA, change the WiFi.begin() call accordingly.

  This example is written for a network using WPA encryption. For
  WEP or WPA, change the WiFi.begin() call accordingly.

  Circuit:
   WiFi shield attached

  created 13 July 2010
  by dlf (Metodo2 srl)
  modified 31 May 2012
  by Tom Igoe
*/
#include <SPI.h>
#include <WiFi101.h>

char ssid[] = "DMC-Public"; //  your network SSID (name)
char pass[] = "elston2222";    // your network password (use for WPA, or use as key for WEP)
//int keyIndex = 0;            // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;
// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server (these are commas!):
//IPAddress server(52,84,32,78);  // numeric IP for Google (no DNS)
char server[] = "slack.com";    // name address for Google (using DNS)

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
//WiFiClient client;
WiFiSSLClient client;

// Slack settings
String message = "<!here|humans>%20slack%20test";
//String tok = "xoxp-3594134292-7713583937-24243203685-bdb3126d5a";
String tok = "xoxb-27486101313-45eVdQkiZBxURIW4Kx8HWBEe";
String chan = "dev";
String GET = "";
String icon = "http://dmc-inet.azurewebsites.net/uploads/furbot3.png";
//String icon = "http%3A%2F%2Fdmc-inet.azurewebsites.net%2Fimages%2Fbot.jpg";
//String botname = "phpbot";
String botname = "furbot";

void setup() {
  // CS, IRQ, RESET
  WiFi.setPins(8, 7, 4);

  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // check for the presence of the shield:
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield not present");
    // don't continue:
    while (true);
  }

  // attempt to connect to WiFi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(4000);
  }
  Serial.println("Connected to wifi");
  printWiFiStatus();

  Serial.println("\nStarting connection to server...");
  // if you get a connection, report back via serial:
  if (client.connect(server, 443)) {
    Serial.println("connected to server");
    
    GET = "GET https://slack.com/api/chat.postMessage?token=";
    GET += tok;
    GET += "&channel=%23";
    GET += chan;
    GET += "&text=";
    GET += message;
    GET += "&username=";
    GET += botname;
    GET += "&icon_url=";
    GET += icon;
    GET += "&pretty=1 HTTP/1.0";
    client.println(GET);
    client.println("Host: www.slack.com");
    client.println("Connection: close");
    client.println();
  }
}

void loop() {
  // if there are incoming bytes available
  // from the server, read them and print them:
  while (client.available()) {
    char c = client.read();

    Serial.write(c);
  }

  // if the server's disconnected, stop the client:
  if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting from server.");
    client.stop();

    // do nothing forevermore:
    while (true);
  }
}


void printWiFiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI): ");
  Serial.print(rssi);
  Serial.println(" dBm");
}




