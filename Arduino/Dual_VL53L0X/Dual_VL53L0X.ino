#include "Adafruit_VL53L0X.h"
#include "./VL53L0X.h"

// address we will assign if dual sensor is present
#define LOX1_ADDRESS 0x30
#define LOX2_ADDRESS 0x29

// set the pins to shutdown
#define SHT_LOX1 7
#define SHT_LOX2 6

// objects for the vl53l0x
Adafruit_VL53L0X lox1 = Adafruit_VL53L0X();
Adafruit_VL53L0X lox2 = Adafruit_VL53L0X();

// this holds the measurement
VL53L0X_RangingMeasurementData_t measure1;
VL53L0X_RangingMeasurementData_t measure2;


void setup() {
  Serial.begin(9600);

  // wait until serial port opens for native USB devices
  while (! Serial) { delay(1); }

  pinMode(SHT_LOX1, OUTPUT);
  pinMode(SHT_LOX2, OUTPUT);
  
  
  Serial.println("Starting...");
  setID(lox1, lox2, 6, 7, 0x30, 0x29);
 
}

void loop() {
    lox1.rangingTest(&measure1); // pass in 'true' to get debug data printout!
    lox2.rangingTest(&measure2); // pass in 'true' to get debug data printout!

    // print sensor one reading
    Serial.print("1: ");
    if(measure1.RangeStatus != 4) {     // if not out of range
        sensor1 = measure1.RangeMilliMeter;    
        Serial.print(sensor1);
        Serial.print("mm");    
    } else { Serial.print("Out of range");}

    Serial.print("\t");

    // print sensor two reading
    Serial.print("2: ");
    if(measure2.RangeStatus != 4) {
        sensor2 = measure2.RangeMilliMeter;
        Serial.print(sensor2);
        Serial.print("mm");
    } else {Serial.print("Out of range");
    }

    Serial.println();
    delay(100);
}