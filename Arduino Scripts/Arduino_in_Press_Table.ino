/*
Local Arduino in Bunker
 */
struct info_t
{
  byte length;
  byte id;
  byte driver1;
  byte driver2;
  byte driver3;
  byte driver4;
  byte driver5;
  byte driver6;
  byte pot_reading;
  byte automatic;
};

// Global variable to hold State of Health tlm packet.
info_t information;

// the setup function runs once when you press reset or power the board
void setup()
{
  information.id = 1;
  
  for(int i=0; i<6; i++)
  {
    pinMode(i, OUTPUT);
  }
  
  Serial.begin(57600);  // initialize serial port to transceiver and COSMOS
}

// the loop function runs over and over again forever
void loop()
{
  processCmds();
  setDrivers();
  setServo();
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
    information.pot_reading = Serial.read();
    information.automatic = Serial.read();
  }
}

void setDrivers()
{
  digitalWrite(0, driver.driver1);
  digitalWrite(1, driver.driver2);
  digitalWrite(2, driver.driver3);
  digitalWrite(3, driver.driver4);
  digitalWrite(4, driver.driver5);
  digitalWrite(5, driver.driver6);
}

void setServo()
{
  if (information.automatic)
  {
     //Servo do some shit
     //PID function
  }
  else
  {
    //Servo do some shit
    //Get shit from pot_reading
  }
}
