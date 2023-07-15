int main(){

    init();
    Serial.begin(9600);
    Serial.println("Start");
    double t = 0.00;
    double dt = 0.1;
    while(true){
        double x1_laser = 5*sin(5*t)*cos(3*t) + 0.0001 * random(100);
        double x2_laser = 5*cos(5*t)*sin(3*t) + 0.0001 * random(100);
        double x1_sound = 5*sin(5*t)*sin(3*t) + 0.0001 * random(100);
        double x2_sound = 5*cos(5*t)*cos(3*t) + 0.0001 * random(100);
        t = t + dt;
        Serial.print(x1_laser);
        Serial.print(",");
        Serial.print(x2_laser);
        Serial.print(",");
        Serial.print(x1_sound);
        Serial.print(",");
        Serial.print(x2_sound);
        Serial.println("#");
        delay(50);
    }
    return 0;
}