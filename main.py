import time
import sys
import _thread  # Module for dual-core threading
from machine import I2C, Pin
from I2C_LCD import I2CLcd
from quote_of_the_day import get_quote_of_the_day
from wifi_connect import connect_to_wifi

# Replace these with your Wi-Fi credentials
SSID = "YourSSID"
PASSWORD = "YourPassword"

# Global variables for LCD scrolling
lcd = None
scroll_queue = []

# Function to handle LCD scrolling on Core 1
def lcd_scroller():
    global scroll_queue
    while True:
        if scroll_queue:
            # Process the first item in the queue
            text, row = scroll_queue.pop(0)
            lcd.scroll_text(text, row=row, delay=0.3, repeat=False)
        time.sleep(0.1)  # Prevent high CPU usage

# Main program logic (Core 0)
def main_program():
    global lcd, scroll_queue

    # Connect to Wi-Fi
    if not connect_to_wifi(SSID, PASSWORD):
        print("Failed to connect to Wi-Fi. Exiting...")
        sys.exit(1)

    i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
    devices = i2c.scan()

    if devices:
        lcd = I2CLcd(i2c, devices[0], 2, 16)  # Initialize the LCD

        # Fetch the quote of the day
        result = get_quote_of_the_day()

        if "error" in result:
            lcd.move_to(0, 0)
            lcd.putstr("Error fetching")  # Display error message
            lcd.move_to(0, 1)
            lcd.putstr("quote")
        else:
            quote = result["quote"]
            author = result["author"]

            # Add scrolling tasks to the queue
            if len(author) > 16:
                scroll_queue.append((author, 1))  # Author on line 1
            else:
                lcd.move_to(0, 1)
                lcd.putstr(author)

            if len(quote) > 16:
                scroll_queue.append((quote, 0))  # Quote on line 0
            else:
                lcd.move_to(0, 0)
                lcd.putstr(quote)

# Start the LCD scroller on Core 1
_thread.start_new_thread(lcd_scroller, ())

# Run the main program on Core 0
main_program()
