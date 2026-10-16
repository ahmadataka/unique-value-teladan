// Arduino Uno: potentiometer on A0, external LED on D8.
const int SENSOR = A0;
const int LED = 8;
bool aktif = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
}

void loop() {
  int nilai = analogRead(SENSOR);
  if (nilai < 400) aktif = true;
  else if (nilai > 600) aktif = false;
  digitalWrite(LED, aktif ? HIGH : LOW);
  Serial.print(nilai);
  Serial.print(" LED=");
  Serial.println(aktif);
  delay(100);
}
