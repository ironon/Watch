/*
  Ellipse drawing example

  This sketch does not use any fonts.
*/

#include <LilyGoLib.h> // Hardware-specific library


// Invoke custom library

void setup(void)
{
    watch.begin();

    watch.setRotation(1);

}

void loop()
{

    watch.fillScreen(TFT_BLACK);

    // Draw some random ellipses
    for (int i = 0; i < 40; i++) {
        int rx = random(60);
        int ry = random(60);
        int x = rx + random(320 - rx - rx);
        int y = ry + random(240 - ry - ry);
        watch.fillEllipse(x, y, rx, ry, random(0xFFFF));
    }

    delay(2000);
    watch.fillScreen(TFT_BLACK);

    for (int i = 0; i < 40; i++) {
        int rx = random(60);
        int ry = random(60);
        int x = rx + random(320 - rx - rx);
        int y = ry + random(240 - ry - ry);
        watch.drawEllipse(x, y, rx, ry, random(0xFFFF));
    }

    delay(2000);
}



