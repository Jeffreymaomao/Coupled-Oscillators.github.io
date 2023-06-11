#include <Wire.h>
#include "./VL53L0X.h"
// #include <VL53L0X.h>

VL53L0X sensor;

double distance0 = 0.0;

int const btn = 8;

void setup() {
    Serial.begin(9600);
    pinMode(btn, INPUT);
    Wire.begin();
    sensor.setAddress(0x30);
    delay(1000);
    if (!sensor.init()) {
        Serial.println("none");
    }
    sensor.setTimeout(500);
}

void loop() {
    double distance = sensor.readRangeSingleMillimeters()/10.0; // unit (cm)

    bool press = digitalRead(btn);

    if(press){distance0 = distance;}
    if (sensor.timeoutOccurred()) {
        Serial.println("Reading distance failed!");
    } else {
        Serial.print("Distance: ");
        Serial.print(distance-distance0);
        Serial.println(" cm");
    }
    

}
