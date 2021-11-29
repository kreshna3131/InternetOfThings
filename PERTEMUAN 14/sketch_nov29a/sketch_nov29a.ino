#include <LiquidCrystal.h>

LiquidCrystal lcd (13, 12, 11, 10, 9, 8);
void setup() {
  lcd.begin(16, 2);

}

void loop() {
  int pirState = digitalRead(1);
  lcd.setCursor(0, 0);
  lcd.print("Kreshna Putra");
  if (pirState == LOW) {
     lcd.setCursor(0, 1);
     lcd.print("V3920032");
     delay(500);
     lcd.clear();
    }
    else if (pirState == HIGH){
     lcd.setCursor(0, 1);
     lcd.print("31-03-2001");
     delay(500);
     lcd.clear();
    }
  }
