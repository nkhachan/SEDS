/*
Local Arduino in Bunker
 */

struct drivers_t
{
  byte driver1;
  byte driver2;
  byte driver3;
  byte driver4;
  byte driver5;
  byte driver6;
};


// Global variable to hold State of Health tlm packet.
drivers_t drivers;


// the setup function runs once when you press reset or power the board
void setup()
{
  information.id = 1;
  
  Serial.begin(57600);  // initialize serial port to transceiver and COSMOS
}

// the loop function runs over and over again forever
void loop()
{
  processCmds();
  sendTlm();
}

void processCmds()
{
  while (Serial.available())
  {
    // get the new byte:
    information.driver1 = Serial.read();
    information.driver2 = Serial.read();
    information.driver3 = Serial.read();
    information.driver4 = Serial.read();
    information.driver5 = Serial.read();
    information.driver6 = Serial.read();
    information.automatic = Serial.read();
  }
}

void sendTlm()
{
  information.length = sizeof(information);
  writeTlm((const char*)&information, sizeof(information));
}

void writeTlm(const char* pkt, byte size)
{
  for(int i=0; i<size; i++)
  {
    Serial.write(pkt[i]);
  }
}
