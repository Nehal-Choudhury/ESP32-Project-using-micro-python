# Project 2: Button Input
# Description: Reads the state of a push button connected to a GPIO pin and
#              prints whether it's pressed or released to the REPL.

# Hardware: ESP32, 1 push button, jumper wires.
# Connection: One side of button to ESP32 GPIO (e.g., GPIO13), other side of button to GND.
#             Use internal pull-up resistor.

from machine import Pin
import time

# Define the GPIO pin where the button is connected
# GPIO13 is a good choice as it's not typically used by internal components
BUTTON_PIN = 13

# Initialize the button pin as an input with an internal PULL_UP resistor.
# This means the pin will be HIGH when the button is not pressed, and LOW when pressed.
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

print(f"Monitoring button on GPIO{BUTTON_PIN}...")
print("Press the button to see changes.")

last_button_state = button.value() # Store initial state to detect changes

while True:
    current_button_state = button.value()

    # Check if the button state has changed
    if current_button_state != last_button_state:
        if current_button_state == 0: # Button is pressed (LOW because of PULL_UP)
            print("Button Pressed!")
        else: # Button is released (HIGH)
            print("Button Released!")
        last_button_state = current_button_state # Update last state

    time.sleep(0.1) # Small delay to debounce and prevent rapid readings
