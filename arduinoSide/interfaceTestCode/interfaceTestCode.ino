
unsigned long time;
unsigned delay_ms = 100;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  time = millis();
  int data[] = {analogRead(A0) - 330, analogRead(A1) - 330, analogRead(A2) - 330, analogRead(A3) - 330};
  
  char buffer[128] = {0};
  int ledVal = (int) 255 * ((float) (data[0] + 330) / 330);
  if(ledVal > 255) {ledVal = 255;}
  sprintf(buffer, "%ld %d %d %d %d\n", 
  time, data[0], data[1], data[2], data[3]);
  analogWrite(9, ledVal);
  Serial.print(buffer);
//  if(Serial.available() > 0)
//  {
//    String cmd = Serial.readStringUntil('\n');
//    String data = Serial.readStringUntil('\n');
//    Serial.print("Received cmd: ");
//    Serial.print(cmd);
//    Serial.print("\n");
//
//    if(cmd.equals("CMD_NUMBER"))
//    {
//      int num = data.toInt();
//      Serial.print("Received number: ");
//      Serial.print(num);
//      Serial.print("\n");
//    }
//  }
  
  delay(delay_ms);
}
