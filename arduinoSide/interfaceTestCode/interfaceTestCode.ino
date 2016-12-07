/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int data[] = {analogRead(A0) - 330, analogRead(A1) - 330, analogRead(A2) - 330, analogRead(A3) - 330, analogRead(A4)};

  char buffer[128] = {0};
  int ledVal = (int) 255 * ((float) (data[0] + 330) / 330);
  sprintf(buffer, "0:[%d] [%d] [%d] [%d] debug %d, leg %d\n", 
  data[0], data[1], data[2], data[3], data[4], ledVal);
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
  
  delay(50);
}
