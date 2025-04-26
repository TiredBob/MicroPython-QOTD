import time
from machine import I2C, Pin
from I2C_LCD import I2CLcd

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
devices = i2c.scan()

try:
    if devices:
        lcd = I2CLcd(i2c, devices[0], 2, 16)  # Initialize the LCD
        lcd.move_to(0, 0)
        lcd.putstr("Scrolling...")

        # Use the scroll_text method directly from the library
        lcd.scroll_text("Hello, this is a scrolling text!", row=1, delay=0.2, repeat=True)
except:
    pass
