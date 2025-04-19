#include "values.h"

void setup() {
  Serial.begin(115200);
}


void loop() {
  delay(1000);
  Serial.println("All good !!!");
  Serial.println(jwtToken);

}
