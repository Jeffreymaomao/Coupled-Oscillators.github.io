#define TrigPin 4  //接腳
#define EchoPin 5

double Trigger(){
  digitalWrite(TrigPin,LOW);
  delayMicroseconds(5);
  digitalWrite(TrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPin,LOW);
  return pulseIn(EchoPin,HIGH);
}


void setup() {
    // put your setup code here, to run once:
    pinMode(TrigPin,OUTPUT);
    pinMode(EchoPin,INPUT);
    Serial.begin(9600);
}
void loop() {
    Serial.println(Trigger()/59.0);
    delay(100);
}
