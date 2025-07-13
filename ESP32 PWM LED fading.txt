# Project 3: PWM LED Fading
# Description: Uses Pulse Width Modulation (PWM) to fade an LED in and out smoothly,
#              demonstrating analog-like control with digital pins.

# Hardware: ESP32, 1 LED, 1 current-limiting resistor.
# Connection: LED Anode (long leg) to ESP32 GPIO (e.g., GPIO2), LED Cathode (short leg) to resistor, resistor to GND.

from machine import Pin, PWM
import time

# Define the GPIO pin for PWM output
PWM_PIN = 2 # Use a PWM-capable pin, GPIO2 is common for onboard LEDs

# PWM frequency (Hz) - controls how fast the PWM signal switches
PWM_FREQ = 5000

# Initialize PWM on the specified pin
pwm_led = PWM(Pin(PWM_PIN), freq=PWM_FREQ)

print(f"Fading LED on GPIO{PWM_PIN}...")

while True:
    # Fade in (increase brightness)
    for duty in range(0, 1024, 8): # Duty cycle from 0 to 1023 (10-bit resolution)
        pwm_led.duty(duty)
        time.sleep(0.005) # Small delay for smooth transition

    # Fade out (decrease brightness)
    for duty in range(1023, -1, -8): # Duty cycle from 1023 down to 0
        pwm_led.duty(duty)
        time.sleep(0.005) # Small delay for smooth transition
