import time
from machine import I2C, Pin
from I2C_LCD import I2CLcd

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
devices = i2c.scan()
def scroll_text(lcd, text, row=0, delay=0.3, repeat=False):
    """
    Scrolls text across the I2C LCD.

    Args:
        lcd (I2CLcd): The I2CLcd object.
        text (str): The text to scroll.
        row (int): The row number to display the text (0 or 1 for a 2-row LCD).
        delay (float): The delay between shifts in seconds.
        repeat (bool): Whether to continuously scroll the text (default: False).
    """
    screen_width = 16  # Adjust based on your LCD's width
    padding = " " * screen_width
    scroll_text = padding + text + padding  # Add padding to the text for smooth scrolling

    while True:
        for i in range(len(scroll_text) - screen_width + 1):
            lcd.move_to(0, row)  # Move to the start of the row
            lcd.putstr(scroll_text[i:i+screen_width])  # Display the current slice of text
            time.sleep(delay)  # Wait before scrolling to the next position
        
        if not repeat:  # Break the loop if repeat is False
            break
try:
    if devices != []:
        lcd = I2CLcd(i2c, devices[0], 2, 16)
        lcd = I2CLcd(i2c, devices[0], 2, 16)  # Initialize the LCD
        lcd.move_to(0, 0)
        lcd.putstr("Scrolling...")

# Scroll text on the second row
        scroll_text(lcd, "Hello, this is a scrolling text!", row=1, delay=0.2, repeat=True)
except:
    pass
