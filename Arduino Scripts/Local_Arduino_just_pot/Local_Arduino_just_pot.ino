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

int potPin = 2;

struct pot_t
{
  byte length;
  byte id;
  byte pot_pos_h;
  byte pot_pos_l;
};

// Global variable to hold State of Health tlm packet.
pot_t pot;

// the setup function runs once when you press reset or power the board
void setup()
{
  pot.id = 1;
  Serial.begin(9600);  // initialize serial:
}

// the loop function runs over and over again forever
void loop()
{
  int pot_position = analogRead(potPin);
  pot.pot_pos_h = (byte)(pot_position >> 8);
  pot.pot_pos_l = (byte)(pot_position);
  sendTlm();
  delay(50);
}

void sendTlm()
{
  pot.length = sizeof(pot);
  writeTlm((const char*)&pot, sizeof(pot));
}

void writeTlm(const char* pkt, byte size)
{
  for(int i=0; i<size; i++)
  {
    Serial.write(pkt[i]);
  }
}

