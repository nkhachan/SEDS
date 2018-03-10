#include <TimerOne.h>

int pkt_received = 0;
char buff[8];
int pressPin = 7, driver1, driver2, driver3, driver4, driver5, driver6, autoControl, pot_reading;
const byte interruptPin = 19;
String msg;
//int msg = 9;

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
  if (msg != ""){
    if (pkt_received != 0){
      parseMsg(msg);
      writeDrivers();
    }
    Serial.println(msg);
    msg = "";
    pkt_received++;
  }
  //readPressure();
  //sendTlm();
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
  //Convert binary data to ascii
  driver6 = int(msg.charAt(msg.length()-1)) - 48;
  driver5 = int(msg.charAt(msg.length()-2)) - 48;
  driver4 = int(msg.charAt(msg.length()-3)) - 48;
  driver3 = int(msg.charAt(msg.length()-4)) - 48;
  driver2 = int(msg.charAt(msg.length()-5)) - 48;
  driver1 = int(msg.charAt(msg.length()-6)) - 48;
  autoControl = int(msg.charAt(1)) - 48;
  pot_reading = msg.substring(2,msg.length()-6).toInt();
  printtoBinary(pot_reading);
  
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

void printtoBinary(int pot_reading){
  digitalWrite(46,pot_reading%2);
  pot_reading /= 2;
  digitalWrite(47,pot_reading%2);
  pot_reading /= 2;
  digitalWrite(48,pot_reading%2);
  pot_reading /= 2;
  digitalWrite(49,pot_reading%2);
  pot_reading /= 2;
  digitalWrite(50,pot_reading%2);
  pot_reading /= 2;
  digitalWrite(51,pot_reading%2);
  pot_reading /= 2;
  digitalWrite(52,pot_reading%2);
  pot_reading /= 2;
  digitalWrite(53,pot_reading%2);
  pot_reading /= 2;
}



void incoming()
{
  while(Serial1.available()){
     msg += Serial1.read();
    //msg = Serial1.readBytes(buff, 1);
    //msg = Serial1.parseInt();
  }//end while
}
