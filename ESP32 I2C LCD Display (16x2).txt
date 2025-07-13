# Project 7: I2C LCD Display (16x2)
# Description: Displays text on a 16x2 LCD screen connected via an I2C PCF8574 adapter.

# Hardware: ESP32, 16x2 LCD with I2C adapter, jumper wires.
# Connection: ESP32 SDA to LCD SDA, ESP32 SCL to LCD SCL, VCC to 3.3V, GND to GND.
#             ESP32 I2C pins: SDA=GPIO21, SCL=GPIO22 (default for I2C(0) on many boards)
# Library: Requires 'lcd_api.py' and 'i2c_lcd.py' libraries.
#          You need to upload these files to your ESP32's filesystem first.
#          Find them here:
#          - lcd_api.py: https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/display/lcd_api.py
#          - i2c_lcd.py: https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/display/i2c_lcd.py

from machine import Pin, I2C
from time import sleep_ms
from i2c_lcd import I2cLcd # Make sure i2c_lcd.py is uploaded

# I2C configuration
I2C_SDA_PIN = 21 # Default SDA pin for I2C(0) on ESP32
I2C_SCL_PIN = 22 # Default SCL pin for I2C(0) on ESP32
I2C_FREQ = 400000 # 400kHz

# LCD configuration
# You might need to find your LCD's I2C address. Common ones are 0x27 or 0x3F.
# Use an I2C scanner script to find it if unsure.
# Example scanner:
# i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
# print(i2c.scan()) # This will print a list of addresses
I2C_ADDR = 0x27
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Initialize I2C bus
i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=I2C_FREQ)

# Initialize LCD object
lcd = I2cLcd(i2c, I2C_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

print(f"Initializing I2C LCD on SDA={I2C_SDA_PIN}, SCL={I2C_SCL_PIN}...")

# Clear the display
lcd.clear()
sleep_ms(100)

# Write some text
lcd.putstr("Hello, MicroPython!")
lcd.move_to(0, 1) # Move cursor to column 0, row 1 (second row)
lcd.putstr("ESP32 LCD Demo")

# Loop to update display (optional, for dynamic content)
counter = 0
while True:
    lcd.move_to(0, 0) # Go to first row
    lcd.putstr(f"Time: {counter:04d}s") # Update time
    counter += 1
    sleep_ms(1000) # Wait 1 second
    lcd.clear() # Clear for next update to prevent ghosting
    lcd.putstr("Hello, MicroPython!")
    lcd.move_to(0, 1)
    lcd.putstr("ESP32 LCD Demo")
