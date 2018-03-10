
#include <TimerOne.h>
const byte interruptPin = 0;
String msg;
struct press_t
{
  byte length;
  byte id;
  
  byte press1_h; 
  byte press1_l;
  
  byte press2_h; 
  byte press2_l;
  
  byte press3_h;
  byte press3_l;
};


struct thermo_t
{
  byte length;
  byte id;
  
  byte thermo1_h; 
  byte thermo1_l; 

  byte thermo2_h; 
  byte thermo2_l; 

  byte thermo3_h; 
  byte thermo3_l; 

  byte thermo4_h; 
  byte thermo4_l; 
};
thermo_t thermo_info;
press_t press_info;

// the setup function runs once when you press reset or power the board
void setup()
{
  thermo_info.id = 1;
  press_info.id = 2;
  
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
  collectSensors();
  sendThermo();
  sendPress();
  delay(250);
}

void sendThermo()
{
  thermo_info.length = sizeof(thermo_info);
  writeTlm((const char*)&thermo_info, sizeof(thermo_info));
}

void sendPress()
{
  press_info.length = sizeof(press_info);
  writeTlm((const char*)&press_info, sizeof(press_info));
}

void writeTlm(const char* pkt, byte size)
{
  for(int i=0; i<size; i++)
  {
    Serial.write(pkt[i]);
  }
}

void collectSensors(){
  int val1 = analogRead(A2);
  thermo_info.thermo1_h = (byte)(val1 >> 8);
  thermo_info.thermo1_l = (byte)(val1);
  
  val1 = analogRead(A3);
  thermo_info.thermo2_h = (byte)(val1 >> 8);
  thermo_info.thermo2_l = (byte)(val1);

  val1 = analogRead(A4);
  thermo_info.thermo3_h = (byte)(val1 >> 8);
  thermo_info.thermo3_l = (byte)(val1);

  val1 = analogRead(A5);
  thermo_info.thermo4_h = (byte)(val1 >> 8);
  thermo_info.thermo4_l = (byte)(val1);

  val1 = analogRead(A0);
  press_info.press1_h = (byte)(val1 >> 8);
  press_info.press1_l = (byte)(val1);
  
  val1 = analogRead(A1);
  press_info.press2_h = (byte)(val1 >> 8);
  press_info.press2_l = (byte)(val1);
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
