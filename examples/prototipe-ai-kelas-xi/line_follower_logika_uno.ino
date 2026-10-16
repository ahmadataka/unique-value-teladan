// Two pushbuttons simulate sensors. Pressed means black line detected.
const int KIRI = 2, KANAN = 3;

const char* arah(bool kiri, bool kanan) {
  if (kiri && kanan) return "MAJU";
  if (kiri) return "KIRI";
  if (kanan) return "KANAN";
  return "STOP";
}

void setup() {
  Serial.begin(115200);
  pinMode(KIRI, INPUT_PULLUP);
  pinMode(KANAN, INPUT_PULLUP);
}

void loop() {
  bool kiri = digitalRead(KIRI) == LOW;
  bool kanan = digitalRead(KANAN) == LOW;
  Serial.println(arah(kiri, kanan));
  delay(100);
}
