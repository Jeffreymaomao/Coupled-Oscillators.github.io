// double distance_HC(int TrigPin, int EchoPin){
//     digitalWrite(TrigPin,0);
//     delayMicroseconds(5);
//     digitalWrite(TrigPin, 1);
//     delayMicroseconds(10);
//     digitalWrite(TrigPin,0);
//     return (pulseIn(EchoPin,1)/59.0);
// }

double distance_HC(int TrigPin, int EchoPin) {
    unsigned long timeout = 20000;
    digitalWrite(TrigPin, LOW);
    delayMicroseconds(5);
    digitalWrite(TrigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(TrigPin, LOW);

    unsigned long startTime = micros();
    while (digitalRead(EchoPin) == LOW) {
        if ((micros() - startTime) > timeout) {
            // 超過設定的時間上限，回傳一個錯誤值或處理方式
            return 0.0*(timeout/59.0);
        }
    }

    startTime = micros();
    while (digitalRead(EchoPin) == HIGH) {
        if ((micros() - startTime) > timeout) {
            // 超過設定的時間上限，回傳一個錯誤值或處理方式
            return 0.0*(timeout/59.0);
        }
    }

    unsigned long duration = micros() - startTime;
    return (duration / 59.0);
}
