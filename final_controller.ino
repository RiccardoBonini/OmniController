#include <Bridge.h>
#include <YunClient.h>
#include <ArduinoJson.h>
#define PORT 255

#define asseX A5 
#define asseY A4 
#define PressPin 7

#define O0 11
#define O1 10
#define O2 9
#define O3 6
#define O4 5
#define O5 3
#define I0 A0
#define I1 A1
#define I2 A2
#define I3 A3
#define I5 A5

const int analogInPin1 = I0; // Analog input pin that the Accelerometer's first pin is attached to

const int analogInPin2 = I1; // Analog input pin that the Accelerometer's second pin is attached to

const int analogInPin5 = I5; //Analog input pin that the Switch Configuration button is attached to

const int analogOutPin1= O0; // Analog output pin that the LED is attachedto

const int analogOutPin2= O1; // Analog output pin that the LED is attachedto

int sensorValue1 = 0; // value read from the Accelerometer's first pin

int sensorValue2 = 0; // value read from the Accelerometer's second pin

int outputValue1 = 0; // value output to the PWM (analog out)

int outputValue2 = 0; // value output to the PWM (analog out)

YunClient client;
bool Connected;

IPAddress addr(192, 168, 43, 209);

DynamicJsonDocument  doc(200);

void setup()
{
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);

  Bridge.begin();

  doc["X"] = 0;
  doc["Y"] = 0;
  doc["B"] = false;
  
  Serial.begin(115200);
  Serial.println("Client connecting on port 255");
  Connected = false;
}

void loop()
{
  if (!Connected)
  {
    client.connect(addr, PORT);
    if (client.connected())
    {
      Serial.println("Connected to the server.");      

      Connected = true;
    }
    else
    {
      Serial.println("Could not connect to the server.");  

      delay(5000);
    }
  }

  if (Connected)
  {

    if (client.connected())
    {
      int xVal, yVal;
      bool buttonVal;
   
      xVal = analogRead (analogInPin1);
      yVal = analogRead (analogInPin2);
      buttonVal = digitalRead (analogInPin5);

      doc["X"] = xVal;
      doc["Y"] = yVal;
      doc["B"]= buttonVal;
      serializeJson(doc, Serial);
      Serial.println();
      serializeJson(doc, client);
      delay(100);

    }
    else
    {
       Serial.println("Server connection closed!");

       client.stop();
      
       Connected = false;
    }
  }
}
