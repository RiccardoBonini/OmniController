#include <WiFi.h>
#include <WiFiMulti.h>

WiFiMulti WiFiMulti;


const char ssid[13] = "BonsiAndroid";//Cellai 8
const char password[10] = "bonsi666";//00000000

const uint16_t port = 255;
const char host[16] = "192.168.43.209";


const int upsx = 2;
const int dwnsx = 4;
const int dwndx = 12;
const int updx = 13;
static boolean clientActive = false;
boolean connesso=false;
 WiFiClient client;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin ledPin as an output.
  pinMode(upsx, OUTPUT);
  pinMode(dwnsx, OUTPUT);
  pinMode(dwndx, OUTPUT);
  pinMode(updx, OUTPUT);
  
  //Serial.begin(115200);


  WiFiMulti.addAP(ssid, password);

    //Serial.println();
    //Serial.println();
    //Serial.print("Waiting for WiFi... ");

    while(WiFiMulti.run() != WL_CONNECTED) {
        //Serial.print(".");
        delay(500);
    }

    //Serial.println("");
    //Serial.println("WiFi connected");
    //Serial.println("IP address: ");
    //Serial.println(WiFi.localIP());


    delay(500);
  
}

// the loop function runs over and over again forever
void loop() {
  
  if(connesso==false){
  client.connect(host, port);
  if(client.connected()){
   //Serial.println("Connected to server successful!");
   connesso=true;
  }
  }
  else{
   int c = client.read();
   if (c!=-1)
   {
    //Serial.print(c);
    //Serial.print("   ");
    if(c==97)
    {
      //Serial.print("avanti");
      digitalWrite(upsx, HIGH);
      digitalWrite(updx, HIGH);
      delay(100);
      digitalWrite(upsx, LOW);
      digitalWrite(updx, LOW);
    }
    if(c==105)//indietro
    {
      //Serial.print("indietro");
      digitalWrite(dwnsx, HIGH);
      digitalWrite(dwndx, HIGH);
      delay(100);
      digitalWrite(dwnsx, LOW);
      digitalWrite(dwndx, LOW);
    }
    if(c==115)//sinistra
    {
      //Serial.print("sinistra");
      digitalWrite(updx, HIGH);
      digitalWrite(dwnsx, HIGH);
      delay(100);
      digitalWrite(updx, LOW);
      digitalWrite(dwnsx, LOW);
    }
    if(c==100)//destra
    {
      //Serial.print("destra");
      digitalWrite(upsx, HIGH);
      digitalWrite(dwndx, HIGH);
      delay(100);
      digitalWrite(upsx, LOW);
      digitalWrite(dwndx, LOW);
    }
   }
}
}
