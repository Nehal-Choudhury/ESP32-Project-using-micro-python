# Project 5: Simple Web Server (Toggle LED)
# Description: Sets up the ESP32 as a Wi-Fi station and hosts a basic web server.
#              You can access an IP address in your browser to toggle an LED on/off.

# Hardware: ESP32, 1 LED, 1 current-limiting resistor.
# Connection: LED Anode (long leg) to ESP32 GPIO (e.g., GPIO2), LED Cathode (short leg) to resistor, resistor to GND.
# Configuration: Update WIFI_SSID and WIFI_PASSWORD.

import network
import socket
from machine import Pin
import time

# Wi-Fi credentials
WIFI_SSID = "YOUR_WIFI_SSID"     # <<< CHANGE THIS
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD" # <<< CHANGE THIS

# LED pin
LED_PIN = 2
led = Pin(LED_PIN, Pin.OUT)
led_state = "OFF" # Initial state

# HTML content for the web page
def web_page():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>ESP32 LED Control</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            .button {{
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            }}
            .button.off {{ background-color: #f44336; /* Red */ }}
            h1 {{ color: #333; }}
            p {{ color: #666; }}
        </style>
    </head>
    <body>
        <h1>ESP32 LED Control</h1>
        <p>LED is currently: <strong>{led_state}</strong></p>
        <p>
            <a href="/?led=on"><button class="button">TURN ON</button></a>
            <a href="/?led=off"><button class="button off">TURN OFF</button></a>
        </p>
    </body>
    </html>
    """
    return html

# Connect to Wi-Fi
def connect_to_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print("Connecting to Wi-Fi...")
        sta_if.connect(ssid, password)
        timeout = 10
        start_time = time.time()
        while not sta_if.isconnected() and (time.time() - start_time) < timeout:
            time.sleep(1)
            print(".", end="")
        print()
    if sta_if.isconnected():
        print("Wi-Fi connected:", sta_if.ifconfig())
        return sta_if.ifconfig()[0] # Return IP address
    else:
        print("Wi-Fi connection failed.")
        return None

# Main execution
if __name__ == "__main__":
    ip_address = connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)

    if ip_address:
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 80)) # Bind to all interfaces on port 80 (HTTP)
        s.listen(5)      # Listen for incoming connections (max 5 queued)

        print(f"Web server listening on http://{ip_address}/")

        while True:
            conn, addr = s.accept() # Accept a new connection
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024) # Read the request
            request = str(request)
            print('Content = %s' % request)

            # Check for LED control commands in the request URL
            global led_state
            if '/?led=on' in request:
                led.value(1)
                led_state = "ON"
            elif '/?led=off' in request:
                led.value(0)
                led_state = "OFF"

            response = web_page() # Get the HTML response
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response) # Send the HTML content
            conn.close() # Close the connection
            print("Connection closed.")
    else:
        print("Cannot start web server without Wi-Fi connection.")

