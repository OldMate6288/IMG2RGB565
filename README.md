# IMG2RGB565
A Python GUI used to convert PNG or JPG images to 16-bit RGB565 C array for displaying sprites on TFT displays

![IMG2RGB565 5_07_2023 8_33_54 PM](https://github.com/OldMate6288/IMG2RGB565/assets/93004427/e797d71e-086f-4665-83ad-add2f360d3f8)
![RGB565](https://github.com/OldMate6288/IMG2RGB565/assets/93004427/e943c74d-5ee5-4d71-85f2-78eecb8b9673)

I made this because I needed to test some sprites on my Pico but was sick of using online tools and couldn't find a decent script to convert image files to RGB565 C array, so I decided to make my own.

**HOW TO USE:**

1. Either run the EXE or run the script directly using CMD from wherever you have saved the script (python IMG2RGB565.py)
2. Open image file and save the output .C file to your device
3. Open the .C file and copy the RGB565 binary
4. Paste the binary into my example Arduino sketch (or your own code)
5. Change the sprite resolution in the Arduino sketch to match your image resolution (DON'T FORGET TO CHANGE THE PIN DEFINITIONS, ROTATION AND RESOLUTION FOR YOUR LCD)
6. Upload your code to your MCU and pray all works well

***ONLY PNG AND JPG ARE CURRENTLY SUPPORTED, WILL ADD SUPPORT FOR GIFS WHEN I FIND OUT HOW TO CONVERT MORE THAN ONE IMAGE AT A TIME.***

**<sub>P.S. I couldn't find a reliable way to resize the image using pillow so for now resize your image manually before converting by using Photoshop or whatever photo editing software you prefer.<sub/>**

***TESTED ON RASPBERRY PI PICO WITH ST7789 240x135 LCD, THIS SHOULD THEORETICALLY WORK WITH ANY MCU WITH A LCD SUPPORTED BY THE ADAFRUIT ST7789/ST7735/TFT_eSPI libraries***

![picosprite (1)](https://github.com/OldMate6288/IMG2RGB565/assets/93004427/aa25e666-f02d-4846-a615-1f0bd7f733dd)


**<sub>Special thanks to http://rinkydinkelectronics.com for giving me a starting point on this project, their RGB565 converter is awesome.<sub/>**
