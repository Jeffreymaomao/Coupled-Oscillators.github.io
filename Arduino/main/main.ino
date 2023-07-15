#include "Adafruit_VL53L0X.h"
#include "./VL53L0X.h"
#include "./HCSR04.h"


#define I2C_ADDRESS1 0x30
#define I2C_ADDRESS2 0x29

#define XSHUT_pin1 6
#define XSHUT_pin2 7

#define Button_pin A1

#define Trig_pin1 2
#define Echo_pin1 3
#define Trig_pin2 4
#define Echo_pin2 5

double time0 = 0.0;
double distance1_laser0 = 0.0;
double distance2_laser0 = 0.0; 
double distance1_sound0 = 0.0; 
double distance2_sound0 = 0.0;
double distance1_laser = 0.0;
double distance2_laser = 0.0; 
double distance1_sound = 0.0; 
double distance2_sound = 0.0;

Adafruit_VL53L0X sensor1 = Adafruit_VL53L0X();
Adafruit_VL53L0X sensor2 = Adafruit_VL53L0X();

VL53L0X_RangingMeasurementData_t measure1;
VL53L0X_RangingMeasurementData_t measure2;


void setup() {
    Serial.begin(9600);

    pinMode(XSHUT_pin1, OUTPUT);
    pinMode(XSHUT_pin2, OUTPUT);

    pinMode(Trig_pin1,OUTPUT);
    pinMode(Echo_pin1,INPUT);
    pinMode(Trig_pin2,OUTPUT);
    pinMode(Echo_pin2,INPUT);

    pinMode(Button_pin, INPUT);

    setID(sensor1, sensor2, XSHUT_pin1, XSHUT_pin2, I2C_ADDRESS1, I2C_ADDRESS2);
 
}

void loop() {

    bool press = digitalRead(Button_pin);
    double time = micros()/1000000.0;

    // sensor1.rangingTest(&measure1, false);
    // sensor2.rangingTest(&measure2, false);
    // distance1_laser = measure1.RangeMilliMeter/10;
    // distance2_laser = measure2.RangeMilliMeter/10;

    distance1_sound = distance_HC(Trig_pin1, Echo_pin1);
    distance2_sound = distance_HC(Trig_pin2, Echo_pin2);
    if(press){
        time0 = time;
        distance1_laser0 = distance1_laser;
        distance2_laser0 = distance2_laser;
        distance1_sound0 = distance1_sound;
        distance2_sound0 = distance2_sound;
    }
    String dataString = ""; 
    dataString += time-time0; // (s)
    dataString += ",";
    dataString += distance1_laser - distance1_laser0; // (cm)
    dataString += ",";
    dataString += distance2_laser - distance2_laser0; // (cm)
    dataString += ",";
    dataString += distance1_sound - distance1_sound0; // (cm)
    dataString += ",";
    dataString += distance2_sound - distance2_sound0; // (cm)
    dataString += "#";
    Serial.println(dataString);
}




