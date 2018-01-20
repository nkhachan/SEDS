/*
Local Arduino in Bunker
 */
int pressPin = 6;

struct info_t
{
  byte driver1;
  byte driver2;
  byte driver3;
  byte driver4;
  byte driver5;
  byte driver6;
  byte pot_reading;
  byte automatic;
};

struct press_t
{
  byte length;
  byte id;
  byte pressure;
};

// Global variable to hold State of Health tlm packet.
info_t information;
press_t valve_info;
// the setup function runs once when you press reset or power the board
void setup()
{
  Serial.begin(57600);  // initialize serial port to transceiver and COSMOS
  valve_info.id = 1;
  
  for(int i=0; i<6; i++)
  {
    pinMode(i, OUTPUT);
  }
}

// the loop function runs over and over again forever
void loop()
{
  //processCmds();
  //setDrivers();
  //setServo();
  //readPressure();
  sendTlm();
  delay(1000);
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
     Serial.write(pkt[i]); 
   } 
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
    //information.pot_reading = Serial.read();
    information.automatic = Serial.read();
  }
}

void setDrivers()
{
  digitalWrite(0, information.driver1);
  digitalWrite(1, information.driver2);
  digitalWrite(2, information.driver3);
  digitalWrite(3, information.driver4);
  digitalWrite(4, information.driver5);
  digitalWrite(5, information.driver6);
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

