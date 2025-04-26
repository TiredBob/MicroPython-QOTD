Grabs a QOTD from [Zenquotes](https://zenquotes.io/api/today), and displays it on a 16x2 LCD using an I2C backpack. Requires the requests library. 

Uses modified code from [Freenove](https://github.com/Freenove/Freenove_Super_Starter_Kit_for_Raspberry_Pi_Pico) which is where the LCD files come from.

This has only been tested on the Pico 2 W, but should work on most dual core chips running Micropython, provided you change the pin definitions and they can connect to wi-fi.

Pico 2 W Pinout: 
GP14>SDA
GP15>SCL
