#include <Wire.h>
 
 #define DEVICE (0x53)    
 #define TO_READ (6)        
 
 byte buff[TO_READ] ;  
 char str[512];                     
 
 void setup()
 {
   Wire.begin();        
   Serial.begin(9600);  
  pinMode(11,OUTPUT);
  
   writeTo(DEVICE, 0x2D, 0);      
   writeTo(DEVICE, 0x2D, 16);
   writeTo(DEVICE, 0x2D, 8);
 }
void loop()
 {
   int regAddress = 0x32;  
   int x, y, z;
   
   readFrom(DEVICE, regAddress, TO_READ, buff);
   

   x = (((int)buff[1]) << 8) | buff[0];   
   y = (((int)buff[3])<< 8) | buff[2];
   z = (((int)buff[5]) << 8) | buff[4];
   

   //sprintf(str, "%d %d %d", x, y, z);  
   //Serial.println(str);
   Serial.println(x);
   //Serial.print(',');
   Serial.println(y);
   //Serial.print(',');
   //Serial.println(z);
   
   
   delay(25);
  // x = map(x, -250, 290, 0, 255);
  // Serial.println(x);
   //analogWrite(11,x);
 }

void writeTo(int device, byte address, byte val) {
    Wire.beginTransmission(device); 
    Wire.write(address);       
    Wire.write(val);      
    Wire.endTransmission(); 
 }
 void readFrom(int device, byte address, int num, byte buff[]) {
   Wire.beginTransmission(device); 
   Wire.write(address);       
   Wire.endTransmission();
   Wire.beginTransmission(device); 
   Wire.requestFrom(device, num);  
    
   int i = 0;
   while(Wire.available()) 
  { 
     buff[i] = Wire.read();
     i++;
   }
   Wire.endTransmission();
 }
