#include "Adafruit_VL53L0X.h"
#include "./VL53L0X.h"

#define I2C_ADDRESS1 0x30
#define I2C_ADDRESS2 0x29

#define XSHUT_pin1 6
#define XSHUT_pin2 7

Adafruit_VL53L0X sensor1 = Adafruit_VL53L0X();
Adafruit_VL53L0X sensor2 = Adafruit_VL53L0X();

VL53L0X_RangingMeasurementData_t measure1;
VL53L0X_RangingMeasurementData_t measure2;

void setup() {
    Serial.begin(9600);

    pinMode(XSHUT_pin1, OUTPUT);
    pinMode(XSHUT_pin2, OUTPUT);
    setID(sensor1, sensor2, XSHUT_pin1, XSHUT_pin2, I2C_ADDRESS1, I2C_ADDRESS2);
 
}

void loop() {
    sensor1.rangingTest(&measure1); // pass in 'true' to get debug data printout!
    sensor2.rangingTest(&measure2); // pass in 'true' to get debug data printout!

    double distance1 = measure1.RangeMilliMeter;
    double distance2 = measure2.RangeMilliMeter;
    Serial.print(distance1); // (mm)
    Serial.print(",");
    Serial.print(distance2); // (mm)
    Serial.println("#");
    delay(100);
}