bool setID(Adafruit_VL53L0X& sensor1, Adafruit_VL53L0X& sensor2, int XSHUT_PIN1, int XSHUT_PIN2, unsigned char IC2_ADDRESS_1, unsigned char IC2_ADDRESS_2) {

    Serial.println("Shutdown pins inited...");

    digitalWrite(XSHUT_PIN1, 0);
    digitalWrite(XSHUT_PIN2, 0);

    Serial.println("Both in reset mode...(pins are 0)");
    // all reset
    digitalWrite(XSHUT_PIN1, 0);    
    digitalWrite(XSHUT_PIN2, 0);
    delay(10);
    // all unreset
    digitalWrite(XSHUT_PIN1, 1);
    digitalWrite(XSHUT_PIN2, 1);
    delay(10);

    // activating LOX1 and reseting LOX2
    digitalWrite(XSHUT_PIN1, 1);
    digitalWrite(XSHUT_PIN2, 0);

    // initing LOX1
    if(!sensor1.begin(IC2_ADDRESS_1)) {
        Serial.println(F("Failed to boot first VL53L0X"));
        return 0;
    }
    delay(10);

    // activating LOX2
    digitalWrite(XSHUT_PIN2, 1);
    delay(10);

    //initing LOX2
    if(!sensor2.begin(IC2_ADDRESS_2)) {
        Serial.println(F("Failed to boot second VL53L0X"));
        return 0;
    }
    return 1;
}