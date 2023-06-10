
#include "./VL53L0X.h"

// address we will assign if dual sensor is present
#define LOX1_ADDRESS 0x30
#define LOX2_ADDRESS 0x31
// set the pins to shutdown
#define SHT_LOX1 7
#define SHT_LOX2 6

// objects for the vl53l0x
VL53L0X sensor1;
VL53L0X sensor2;

// button 
int const btn = 8;

bool setID() {
    sensor1.setAddress(LOX1_ADDRESS);
    sensor2.setAddress(LOX2_ADDRESS);
    // all reset
    digitalWrite(SHT_LOX1, LOW);    
    digitalWrite(SHT_LOX2, LOW);
    delay(10);
    // all unreset
    digitalWrite(SHT_LOX1, HIGH);
    digitalWrite(SHT_LOX2, HIGH);
    delay(10);
    // activating LOX1 and reseting LOX2
    digitalWrite(SHT_LOX1, HIGH);
    digitalWrite(SHT_LOX2, LOW);

    // initing LOX1
    if(!sensor1.init()) {
        Serial.println("\nFailed to boot first VL53L0X");
        return 0;
    }
    delay(10);

    // activating LOX2
    digitalWrite(SHT_LOX2, HIGH);
    delay(10);

    //initing LOX2
    if(!sensor2.init()) {
        Serial.println("\nFailed to boot second VL53L0X"); 
        return 0;
    }
    return 1;
}
void setup() {
    Serial.begin(9600);
    pinMode(btn, INPUT);
    Wire.begin();

    pinMode(SHT_LOX1, OUTPUT);
    pinMode(SHT_LOX2, OUTPUT);

    while(true){
        Serial.println("Shutdown pins inited...");
        digitalWrite(SHT_LOX1, LOW);
        digitalWrite(SHT_LOX2, LOW);
        Serial.println("Both in reset mode...(pins are low)");
        Serial.println("\n\n\nset ID ----------- ");
        if(!setID()){
            delay(5000);
            continue;
        }
        Serial.println("end set ID -------------");
    }
    
}

void loop() {
}
 