include <TimerOne.h>

int pressPin = 7;
const byte interruptPin = 19;
byte fun;
String msg;
/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
 */
struct info_t
{
  byte driver1;
  byte driver2;
  byte driver3;
  byte driver4;
  byte driver5;
  byte driver6;
  byte automatic;
  byte pot_reading;
};

struct valve_t
{
  byte length;
  byte id;
  byte pressure;
};

// Global variable to hold State of Health tlm packet.
info_t info;
valve_t valve_info;

// the setup function runs once when you press reset or power the board
void setup()
{
  valve_info.id = 1;
  valve_info.pressure = 90;

  pinMode(13, OUTPUT); // initialize digital pin 13 as an output.
  Serial1.begin(57600);  // initialize serial
  Serial.begin(57600);
  attachInterrupt(digitalPinToInterrupt(interruptPin),incoming,HIGH);
  
}

// the loop function runs over and over again forever
void loop()
{
 /*  while(Serial2.available()){
        info.driver1 = Serial2.read();
        Serial.println(info.driver1);//Do what you whant whit your message 
  }//end while*/
}

void readPressure()
{
  valve_info.pressure = analogRead(pressPin);
}

void sendTlm()
{
  valve_info.length = sizeof(valve_info);
  writeTlm((const char*)&valve_info, sizeof(valve_info));
}

void writeTlm(const char* pkt, byte size)
{
  for(int i=0; i<size; i++)
  {
    Serial1.write(pkt[i]);
  }
}     

void incoming()
{
  while(Serial1.available()){
   //     delay(1);
        info.driver1 = Serial1.read();
        Serial.println(info.driver1);//Do what you whant whit your message 
  }//end while
  Serial.println("................................");//Do what you whant whit your message 
}

