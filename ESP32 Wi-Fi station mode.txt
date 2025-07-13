# Project 4: Wi-Fi Station Mode
# Description: Connects the ESP32 to a Wi-Fi network (acting as a station).
#              Prints the IP address upon successful connection.

# Configuration: Update WIFI_SSID and WIFI_PASSWORD with your network credentials.

import network
import time

# Wi-Fi credentials
WIFI_SSID = "YOUR_WIFI_SSID"     # <<< CHANGE THIS to your Wi-Fi network name
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD" # <<< CHANGE THIS to your Wi-Fi password

def connect_to_wifi(ssid, password):
    """Connects the ESP32 to a Wi-Fi network."""
    sta_if = network.WLAN(network.STA_IF) # Create a station interface
    sta_if.active(True)                   # Activate the interface

    if not sta_if.isconnected():
        print(f"Connecting to Wi-Fi network: {ssid}...")
        sta_if.connect(ssid, password) # Connect to the network

        # Wait for connection with a timeout
        timeout = 10 # seconds
        start_time = time.time()
        while not sta_if.isconnected() and (time.time() - start_time) < timeout:
            time.sleep(1)
            print(".", end="") # Print dots while trying to connect
        print() # Newline after dots

    if sta_if.isconnected():
        print("Wi-Fi connected successfully!")
        print("Network config:", sta_if.ifconfig()) # Print IP address, netmask, gateway, DNS
        return True
    else:
        print("Failed to connect to Wi-Fi.")
        return False

# Main execution
if __name__ == "__main__":
    if connect_to_wifi(WIFI_SSID, WIFI_PASSWORD):
        print("ESP32 is now connected to the internet.")
        # You can add more code here to do something with the internet connection
    else:
        print("Please check your Wi-Fi credentials and try again.")

    # Keep the script running (optional, for continuous connection)
    # while True:
    #     time.sleep(5)
    #     if not network.WLAN(network.STA_IF).isconnected():
    #         print("Wi-Fi disconnected. Reconnecting...")
    #         connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)
