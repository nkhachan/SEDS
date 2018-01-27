/#include <TimerOne.h>

int pressPin = 7;
const byte interruptPin = 19;
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
  valve_info.pressure = 250;

  pinMode(13, OUTPUT); // initialize digital pin 13 as an output.
  Serial2.begin(57600);  // initialize serial
  Serial.begin(57600);
  attachInterrupt(digitalPinToInterrupt(interruptPin),incoming,HIGH);
  
}

// the loop function runs over and over again forever
void loop()
{
   sendTlm();
/*    //processCmds();
    if (stringComplete) {
    Serial.println(inputString);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }*/
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
    Serial2.write(pkt[i]);
  }
}     

void incoming()
{
  char _bite;
  sei();//Disable hardware interrupts for a moment
  while(Serial2.available()>0){

        Serial.print(msg);//Do what you whant whit your message
    
  }//end while
cli();//reenabling hardware interrupts
}
