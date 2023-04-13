int sound = A0;

void setup() {
    pinMode(sound, INPUT);
    Serial.begin(9600);
}

void loop() {
    int sensorValue = analogRead(sound);
    Serial.println(sensorValue);
    delay(100);
}
