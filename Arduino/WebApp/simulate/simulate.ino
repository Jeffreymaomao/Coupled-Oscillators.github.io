
float f(float theta){
  return 2 + sin(3*theta);
}

float theta = 0.0;
float distance = 0.0;


void setup() {
  Serial.begin(9600);
}

void loop() {
  theta += 0.1;
  distance = f(theta);

  String data = String(theta) + "," + String(distance);
  Serial.println(data);
  delay(100);
}
