# Project 6: DHT11/DHT22 Temperature & Humidity Sensor
# Description: Reads temperature and humidity data from a DHT11 or DHT22 sensor
#              and prints it to the REPL.

# Hardware: ESP32, DHT11/DHT22 sensor, jumper wires.
# Connection: DHT Data pin to ESP32 GPIO (e.g., GPIO4), VCC to 3.3V, GND to GND.
# Library: Requires 'dht.py' library.
#          You need to upload 'dht.py' to your ESP32's filesystem first.
#          Find dht.py here: https://github.com/micropython/micropython-lib/blob/master/micropython/umodules/dht/dht.py

from machine import Pin
import time
import dht # Make sure dht.py is uploaded to your ESP32

# Define the GPIO pin where the DHT sensor's data pin is connected
DHT_PIN = 4 # Common choice for DHT sensors

# Initialize the DHT sensor object
# For DHT11: sensor = dht.DHT11(Pin(DHT_PIN))
# For DHT22: sensor = dht.DHT22(Pin(DHT_PIN))
sensor = dht.DHT22(Pin(DHT_PIN)) # Using DHT22 for better accuracy

print(f"Reading temperature and humidity from DHT sensor on GPIO{DHT_PIN}...")

while True:
    try:
        sensor.measure() # Perform the measurement
        temperature = sensor.temperature()
        humidity = sensor.humidity()

        print(f"Temperature: {temperature:.1f}°C")
        print(f"Humidity: {humidity:.1f}%")

    except OSError as e:
        if e.args[0] == 110: # Error code 110 typically means timeout/no response
            print("Failed to read sensor. Check wiring or sensor.")
        else:
            print(f"An error occurred: {e}")

    time.sleep(5) # Read every 5 seconds
