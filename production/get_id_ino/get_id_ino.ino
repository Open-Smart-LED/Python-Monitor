String chipString = "";

void setup() {
  Serial.begin(115200);

  uint64_t chipId = ESP.getEfuseMac();
  char chipStr[17]; // 16 caractères + null terminator
  sprintf(chipStr, "%016llX", chipId); // Format hexa sur 16 caractères (64 bits)
  chipString = String(chipStr);
}


void loop() {
  delay(1000);
  Serial.println(chipString);
  delay(10000);
}
