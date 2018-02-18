#include <TimerOne.h>

struct thermocouples_t
{
  byte length;
  byte id;
  int thermo1; 
  int thermo2; 
  int thermo3; 
  int thermo4; 
};

struct press_transducer_t
{
  byte length;
  byte id;
  int press1; 
  int press2; 
  int press3; 
};

// Global variable to hold State of Health tlm packet.
thermocouples_t thermocouples;
press_transducer_t press_trans;

// the setup function runs once when you press reset or power the board
void setup()
{
  thermocouples.id = 1;
  press_trans.id = 2;
    
  Serial.begin(57600);  // initialize serial:
}

// the loop function runs over and over again forever
void loop()
{
  sendTlm(thermocouples);
  sendTlm(press_trans);
  delay(250);
}

void sendTlm(struct packet)
{
  mySoh.length = sizeof(packet);
  writeTlm((const char*)&packet, sizeof(packet));
}

void writeTlm(const char* pkt, byte size)
{
  for(int i=0; i<size; i++)
  {
    Serial.write(pkt[i]);
  }
}
