#include <Wire.h>
#include "./VL53L0X.h"
// #include <VL53L0X.h>

VL53L0X sensor;

void setup() {
    Serial.begin(9600);
    Wire.begin();
    sensor.setAddress(0x30);
    delay(1000);
    if (!sensor.init()) {
        while(1){
            Serial.println("none");
        }
    }
    sensor.setTimeout(500);
    sensor.setMeasurementTimingBudget(200000);
}

void loop() {
    double distance = sensor.readRangeSingleMillimeters();
    if (sensor.timeoutOccurred()) {
        Serial.println("Reading distance failed!");
    } else {
        Serial.print("Distance: ");
        Serial.print(distance/10);
        Serial.println(" cm");
    }

}
