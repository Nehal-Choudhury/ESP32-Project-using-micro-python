# Project 9: Analog Read (Potentiometer)
# Description: Reads analog voltage from a potentiometer connected to an ADC (Analog-to-Digital Converter) pin
#              and prints the raw value (0-4095 for 12-bit ADC) to the REPL.

# Hardware: ESP32, 1 potentiometer (e.g., 10k Ohm), jumper wires.
# Connection: Potentiometer outer pins to 3.3V and GND, middle pin to an ADC-enabled GPIO.
#             Recommended ADC pins on ESP32: GPIO32, GPIO33, GPIO34, GPIO35, GPIO36, GPIO39.
#             Note: GPIO36, GPIO39 are input-only.

from machine import Pin, ADC
import time

# Define the GPIO pin for ADC input
# Use an ADC-capable pin. GPIO34 is a good choice as it's ADC1_CH6 and input-only.
ADC_PIN = 34

# Initialize the ADC pin
adc = ADC(Pin(ADC_PIN))

# Set the ADC attenuation. This determines the input voltage range.
# ADC.ATTN_0DB: 0-1.0V
# ADC.ATTN_2_5DB: 0-1.34V
# ADC.ATTN_6DB: 0-2.0V
# ADC.ATTN_11DB: 0-3.6V (recommended for 3.3V power supply)
adc.atten(ADC.ATTN_11DB)

# Set the ADC width (resolution). ESP32 supports up to 12-bit.
# ADC.WIDTH_9BIT: 0-511
# ADC.WIDTH_10BIT: 0-1023
# ADC.WIDTH_11BIT: 0-2047
# ADC.WIDTH_12BIT: 0-4095 (default and most common)
adc.width(ADC.WIDTH_12BIT)

print(f"Reading analog value from GPIO{ADC_PIN} (ADC channel)..")
print("Rotate the potentiometer to see values change.")

while True:
    analog_value = adc.read() # Read the raw analog value
    print(f"Analog Value: {analog_value}")

    # You can map this value to a different range if needed, e.g., 0-100
    # mapped_value = (analog_value / 4095) * 100
    # print(f"Mapped Value (0-100): {mapped_value:.1f}")

    time.sleep(0.1) # Read every 100ms
