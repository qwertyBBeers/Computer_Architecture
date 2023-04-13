int tilt = 3;
int Led_Pin = 13;

void setup() {
    Serial.begin(9600);
    pinMode(tilt, INPUT);
    pinMode(Led_Pin, OUTPUT);
}

void loop() {
    int a = digitalRead(tilt);
    if(a == HIGH) {
        Serial.println("ball up");
        digitalRead(Led_Pin) = HIGH;
        delay(2000);
    }
    else{
        Serial.println("ball down");
        delay(2000);
    }
}