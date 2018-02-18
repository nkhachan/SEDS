#include <TimerOne.h>
#include <LiquidCrystal.h>

int pressPin = 7, driver1, driver2, driver3, driver4, driver5, driver6, autoControl, pot_reading;
const byte interruptPin = 19;
byte fun;
String msg;
LiquidCrystal lcd(48, 49, 50, 51, 52, 53);

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
  
  lcd.begin(16,2);
  lcd.print("Hello World");
  
}

// the loop function runs over and over again forever
void loop()
{
  
  if (msg != ""){
   lcd.print(msg.substring(2,msg.length()-6));
   parseMsg(msg);
   writeDrivers();
   msg = "";
  }
  delay(250);
  readPressure();
  sendTlm();
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
  digitalWrite(22,pot_reading%2);
  pot_reading /= 2;
  digitalWrite(23,pot_reading%2);
 pot_reading /= 2;
  digitalWrite(24,pot_reading%2);
 pot_reading /= 2;
  digitalWrite(25,pot_reading%2);
 pot_reading /= 2;
  digitalWrite(26,pot_reading%2);
 pot_reading /= 2;
  digitalWrite(27,pot_reading%2);
 pot_reading /= 2;
   digitalWrite(28,pot_reading%2);
 pot_reading /= 2;
   digitalWrite(29,pot_reading%2);
 pot_reading /= 2;
}



void incoming()
{
  while(Serial1.available()){
    msg += Serial1.read();
  }//end while
}
