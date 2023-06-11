//Couple Oscillator Mode estimated by HC-SRO4
#define TrigPinA 2  //接腳
#define EchoPinA 3
#define TrigPinB 4
#define EchoPinB 5

double ProTimeA,ProTimeB;
double DistA,DistB;
double DistA0 = 0.0;
double DistB0 = 0.0;
int Td = 100;
int const btn = 8;
bool pressed = 0;



double TriggerA(){
  digitalWrite(TrigPinA,LOW);
  delayMicroseconds(5);
  digitalWrite(TrigPinA, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPinA,LOW);
  return pulseIn(EchoPinA,HIGH);
}

double TriggerB(){
  digitalWrite(TrigPinB,LOW);
  delayMicroseconds(5);
  digitalWrite(TrigPinB, HIGH);
  delayMicroseconds(10);
  digitalWrite(TrigPinB,LOW);
  return pulseIn(EchoPinB,HIGH);
}


void setup() {
  // put your setup code here, to run once:
  pinMode(TrigPinA,OUTPUT);
  pinMode(EchoPinA,INPUT);
  pinMode(TrigPinB,OUTPUT);
  pinMode(EchoPinB,INPUT);
  pinMode(btn,INPUT);
  Serial.begin(9600);
}

void writeTworesult(double(DistA),double(DistB)){
  Serial.print(DistA);
  Serial.print("\t");
  Serial.println(DistB);
}

void loop() {
  // put your main code here, to run repeatedly:
  pressed = digitalRead(btn);
  ProTimeA = TriggerA()/59;
  ProTimeB = TriggerB()/59;
  if(pressed){
    DistA0 = ProTimeA;
    DistB0 = ProTimeB;
  }
  DistA = ProTimeA;
  DistA = DistA - DistA0;
  DistB = ProTimeB;
  DistB = DistB - DistB0;
  writeTworesult(DistA,DistB);
  delay(Td);
}
