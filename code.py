
/*
  Created by: Cristiano S
  Created on: March 2023

  Changes the colours of a RGB LED
*/

void setup()
{
  pinMode(13, OUTPUT); // Red
  pinMode(12, OUTPUT); // Blue
  pinMode(11, OUTPUT); // Green
}

void loop()
{
  // Green
  digitalWrite(11, HIGH);
  digitalWrite(12, LOW);
  digitalWrite(13, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  // Blue
  digitalWrite(11, LOW);
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  // Red
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  // Turquoise
  digitalWrite(11, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  // Purple
  digitalWrite(11, LOW);
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  // White
  digitalWrite(11, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
}
