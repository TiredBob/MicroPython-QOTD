import network
import time
import sys

def connect_to_wifi(ssid: str, password: str):
    """
    Connects to a Wi-Fi network using the provided SSID and password.

    Args:
        ssid (str): The Wi-Fi network name.
        password (str): The Wi-Fi network password.

    Returns:
        bool: True if connected successfully, False otherwise.
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(ssid, password)

        # Wait for connection with a timeout
        timeout = 10  # seconds
        start_time = time.time()
        while not wlan.isconnected():
            if time.time() - start_time > timeout:
                print("Failed to connect to Wi-Fi: Timeout")
                return False
            time.sleep(1)

    print("Wi-Fi connected!")
    print(f"IP Address: {wlan.ifconfig()[0]}")
    return True

if __name__ == "__main__":
    # Replace with your Wi-Fi credentials
    ssid = "YourSSID"
    password = "YourPassword"

    if not connect_to_wifi(ssid, password):
        print("Could not connect to Wi-Fi. Exiting...")
        sys.exit(1)
