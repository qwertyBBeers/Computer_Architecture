int Buzzer_Pin = 5;

#define C 262
#define D 294
#define E 330
#define F 349
#define G 392
#define A 440
#define B 494

int tempo = 500;
int notes[] = {C, D, E, F, G, A, B};
byte nSize = sizeof(notes) / sizeof(notes[0]);

void setup() {
    pinMode(Buzzer_Pin, OUTPUT);
}

void loop() {
    for(int i = 0; i < nSize; i++) {
        tone(Buzzer_Pin, notes[i], tempo);
        delay(500);
    }
    noTone(Buzzer_Pin);
    delay(1000);
}