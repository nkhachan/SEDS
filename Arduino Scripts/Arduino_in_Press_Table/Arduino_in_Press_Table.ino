#include <TimerOne.h>

int pressPin = 7, driver1, driver2, driver3, driver4, driver5, driver6, autoControl, pot_reading;
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
struct valve_t
{
  byte length;
  byte id;
  byte pressure;
};

// Global variable to hold State of Health tlm packet.
valve_t valve_info;

// the setup function runs once when you press reset or power the board
void setup()
{
  valve_info.id = 1;
  valve_info.pressure = 90;

  pinMode(50, OUTPUT); // initialize digital pin 13 as an output.
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
  if (msg != ""){
  // Serial.println(msg);
   parseMsg(msg);
   writeDrivers();
   msg = "";
  }
  delay(250);
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

void parseMsg(String msg){
  driver6 = int(msg.charAt(msg.length()-2)) - 48;
  driver5 = int(msg.charAt(msg.length()-3)) - 48;
  driver4 = int(msg.charAt(msg.length()-4)) - 48;
  driver3 = int(msg.charAt(msg.length()-5)) - 48;
  driver2 = int(msg.charAt(msg.length()-6)) - 48;
  driver1 = int(msg.charAt(msg.length()-7)) - 48;
  autoControl = int(msg.charAt(msg.length()-1)) - 48;
  pot_reading = msg.substring(0,msg.length()-7).toInt();
  Serial.print(pot_reading);
}

void writeDrivers(){
  digitalWrite(2,driver1);
  digitalWrite(3,driver2);
  digitalWrite(4,driver3);
  digitalWrite(5,driver4);
  digitalWrite(6,driver5);
  digitalWrite(7,driver6);
  digitalWrite(8,autoControl);
}


void incoming()
{
  while(Serial1.available()){
    msg += Serial1.read();
  }//end while
}
