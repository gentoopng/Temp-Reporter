#include "DHT.h"
#include <Wire.h>
#include "rgb_lcd.h"

#define DHTPIN 2

// Uncomment whatever type you're using!
//#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302)
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

DHT dht(DHTPIN, DHTTYPE);

#if defined(ARDUINO_ARCH_AVR)
    #define debug  Serial

#elif defined(ARDUINO_ARCH_SAMD) ||  defined(ARDUINO_ARCH_SAM)
    #define debug  SerialUSB
#else
    #define debug  Serial
#endif

rgb_lcd lcd;

int colorR = 100;
int colorG = 100;
int colorB = 100;

// Uncomment if you use Sliding Potentiometer or other analog sensor
//int adcPin = A0;
//int adcIn = 0;
float brightness = 255;

float THI = 0;

void setup() 
{
    Serial.begin(115200);
    Wire.begin();
    dht.begin();
    lcd.begin(16, 2);
    lcd.setRGB(colorR, colorG, colorB);
}

void loop() 
{
    //adcIn = analogRead(adcPin);
    //brightness = (float)adcIn / 1023;
    //lcd.setRGB(colorR * brightness, colorG * brightness, colorB * brightness);

    float temp_hum_val[2] = {0};

    if (!dht.readTempAndHumidity(temp_hum_val)) {
        Serial.print(temp_hum_val[0]);
        Serial.print(" ");
        Serial.println(temp_hum_val[1]);

        lcd.setCursor(0, 0);
        lcd.print("T:");
        lcd.setCursor(2, 0);
        lcd.print(temp_hum_val[1]);
        lcd.setCursor(6, 0);
        lcd.print("C  H:");
        lcd.setCursor(11, 0);
        lcd.print(temp_hum_val[0]);
        lcd.setCursor(15, 0);
        lcd.print("%");
    }
    else 
    {
        Serial.println("Faled to get temperature and humidity value.");
        lcd.setCursor(0, 0);
        lcd.print("Failed to get");
        lcd.setCursor(0, 1);
        lcd.print("value.");
    }
    
}
