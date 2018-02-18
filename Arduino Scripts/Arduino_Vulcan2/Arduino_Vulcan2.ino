
#include <TimerOne.h>

const byte interruptPin = 0;
String msg;

struct sensors_t
{
  byte length;
  byte id;
  int thermo1; 
  int thermo2; 
  int thermo3; 
  int thermo4; 
  int press1; 
  int press2; 
  int press3; 
};

// Global variable to hold State of Health tlm packet.
sensors_t sensor_info;

// the setup function runs once when you press reset or power the board
void setup()
{
  sensor_info.id = 1;
  sensor_info.press1 = 340;
  sensor_info.press2 = 340;
  sensor_info.press3 = 340;
    
  Serial.begin(57600);  // initialize serial:
  attachInterrupt(digitalPinToInterrupt(interruptPin),incoming,HIGH);
}

// the loop function runs over and over again forever
void loop()
{
   /*if (msg != ""){
   writeLaunch();
   msg = "";
  }*/
  sendTlm();
  delay(250);
}

void sendTlm()
{
  sensor_info.length = sizeof(sensor_info);
  writeTlm((const char*)&sensor_info, sizeof(sensor_info));
}

void writeTlm(const char* pkt, byte size)
{
  for(int i=0; i<size; i++)
  {
    Serial.write(pkt[i]);
  }
}

void incoming()
{
  while(Serial.available()){
    msg += Serial.read();
  }//end while
}

void writeLaunch(){
  int stuff = 1;
}
