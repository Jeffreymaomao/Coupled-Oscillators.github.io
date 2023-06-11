#include <Wire.h>
int const btn = 8;
void setup() {
    Serial.begin(9600);
    pinMode(btn, INPUT);
}

void loop() {

    bool press = digitalRead(btn);
    Serial.println(press);
    delay(100);

}
