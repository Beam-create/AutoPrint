#include <Arduino.h>

void setup() {

  pinMode(13, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

  digitalWrite(13, 1);
  digitalWrite(LED_BUILTIN, 1);
  
  delay(1000);

  digitalWrite(13, 0);
  digitalWrite(LED_BUILTIN, 0);

  delay(1000);
}
