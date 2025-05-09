#include <Servo.h>

Servo myServo;

void setup() {
  Serial.begin(9600);
  pinMode(4, OUTPUT); // Buzzer
  pinMode(5, OUTPUT); // LED
  myServo.attach(9);
  myServo.write(0);   // Locked position
  
  // Ensure buzzer and LED are OFF at startup
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char received = Serial.read();
    
    Serial.print("Received: ");
    Serial.println(received);
    
    if (received == '1') {  
      digitalWrite(4, LOW);  // Buzzer OFF
      digitalWrite(5, HIGH); // LED ON (Access Granted)
      myServo.write(90);     // Unlock
      delay(5000);           // Stay unlocked
      myServo.write(0);      // Lock
    } else if (received == '0') {  
      digitalWrite(4, HIGH); // Buzzer ON (short beep)
      digitalWrite(5, LOW);  // LED OFF (Access Denied)
      delay(100);            // Reduce buzz duration
      digitalWrite(4, LOW);  // Buzzer OFF
      myServo.write(0);      // Keep locked
    } else {  
      // Handle invalid input (optional)
      Serial.println("Invalid input received.");
      digitalWrite(4, LOW);  // Ensure buzzer is off
      digitalWrite(5, LOW);  // Ensure LED is off
      myServo.write(0);      // Keep locked
    }
  }
}