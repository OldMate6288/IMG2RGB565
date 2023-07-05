// ST7789 SPRITE TEST (TESTED ON RPi PICO with Waveshare 1.14 v2 and PICO DISPLAY LCD's 240x135)
// github.com/OldMate6288

#include <Adafruit_GFX.h>
#include <Adafruit_ST7789.h>

// Setup LCD pins
#define TFT_CS   9
#define TFT_RST  12
#define TFT_DC   8
#define TFT_MOSI 11
#define TFT_SCLK 10

Adafruit_ST7789 tft = Adafruit_ST7789(TFT_CS, TFT_DC, TFT_MOSI, TFT_SCLK, TFT_RST);

// Sprite dimensions (MAKE SURE TO CHANGE THIS TO THE RESOLUTION OF YOUR CURRENT IMAGE)
#define SPRITE_WIDTH 240
#define SPRITE_HEIGHT 135

// Sprite data
const uint16_t sprite[SPRITE_WIDTH * SPRITE_HEIGHT] = {
// Add RGB565 Binary below here:

};

void setup() {
  tft.init(135, 240);
  tft.setRotation(3);

  tft.fillScreen(ST77XX_WHITE);
}

void loop() {
  // Quick maths
  int xPos = (tft.width() - SPRITE_WIDTH) / 2;
  int yPos = (tft.height() - SPRITE_HEIGHT) / 2;

  for (int y = 0; y < SPRITE_HEIGHT; y++) {
    for (int x = 0; x < SPRITE_WIDTH; x++) {
      // Get the color value of the pixel from the sprite data
      uint16_t color = sprite[x + y * SPRITE_WIDTH];

      // Draw the pixel at the corresponding position on the screen
      tft.drawPixel(xPos + x, yPos + y, color);
    }
  }

  delay(5000);
}
