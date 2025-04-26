import time
from machine import I2C, Pin
from I2C_LCD import I2CLcd
from quote_of_the_day import get_quote_of_the_day
from wifi_connect import connect_to_wifi

# Replace these with your Wi-Fi credentials
SSID = "YourSSID"
PASSWORD = "YourPassword"

# Connect to Wi-Fi
if not connect_to_wifi(SSID, PASSWORD):
    print("Failed to connect to Wi-Fi. Exiting...")
    sys.exit(1)

i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
devices = i2c.scan()

try:
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

            # Display the quote
            if len(quote) > 16:
                lcd.scroll_text(quote, row=0, delay=0.3, repeat=False)
            else:
                lcd.move_to(0, 0)
                lcd.putstr(quote)

            # Display the author
            if len(author) > 16:
                lcd.scroll_text(author, row=1, delay=0.3, repeat=False)
            else:
                lcd.move_to(0, 1)
                lcd.putstr(author)

except Exception as e:
    print(f"An error occurred: {e}")
