# Project 1: Blinking an LED
# Description: The classic "Hello, World!" for embedded systems.
#              Blinks an LED connected to a specified GPIO pin at a regular interval.

# Hardware: ESP32, 1 LED, 1 current-limiting resistor (e.g., 220 Ohm), jumper wires.
# Connection: LED Anode (long leg) to ESP32 GPIO (e.g., GPIO2), LED Cathode (short leg) to resistor, resistor to GND.

from machine import Pin
import time

# Define the GPIO pin where the LED is connected
# GPIO2 is often the built-in LED on many ESP32 dev boards
LED_PIN = 2

# Initialize the LED pin as an output
led = Pin(LED_PIN, Pin.OUT)

print(f"Blinking LED on GPIO{LED_PIN}...")

# Main loop to blink the LED
while True:
    led.value(1)  # Turn LED ON (HIGH)
    print("LED ON")
    time.sleep(0.5) # Wait for 0.5 seconds

    led.value(0)  # Turn LED OFF (LOW)
    print("LED OFF")
    time.sleep(0.5) # Wait for 0.5 seconds
