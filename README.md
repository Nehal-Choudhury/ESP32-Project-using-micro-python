# ESP32-Project-using-micro-python
Introduction
This repository serves as a practical guide and collection of examples for working with MicroPython on the ESP32. Each project is designed to be straightforward, focusing on a specific concept or hardware interaction. They are excellent starting points for learning embedded programming with MicroPython.

Prerequisites
Before you begin, ensure you have:

ESP32 Development Board: Any standard ESP32 board (e.g., ESP32-DevKitC, NodeMCU ESP32).

USB to Micro-USB Cable: For connecting the ESP32 to your computer.

Python 3: Installed on your computer.

esptool.py: For flashing MicroPython firmware.

pip install esptool

ampy or thonny: For uploading MicroPython code to the ESP32.

pip install adafruit-ampy

(Alternatively, Thonny IDE provides an integrated environment for flashing and uploading.)

Breadboard, Jumper Wires, LEDs, Resistors, Buttons, Sensors: (As required by individual projects).

Getting Started with MicroPython on ESP32
Install Drivers: Ensure your computer has the necessary USB-to-serial drivers (e.g., CP210x or CH340G) for your ESP32 board.

Erase Flash (Optional but Recommended):

esptool.py --port /dev/ttyUSB0 erase_flash
# On Windows, use COMx instead of /dev/ttyUSB0 (e.g., COM3)

Download MicroPython Firmware: Get the latest stable ESP32 firmware from micropython.org/download/esp32/. Download the .bin file.

Flash MicroPython Firmware:

esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-YYYYMMDD-vX.X.bin
# Replace esp32-YYYYMMDD-vX.X.bin with your downloaded firmware file name

Note: You might need to press and hold the "BOOT" button on your ESP32 board while plugging it in or during the flashing process for it to enter download mode, then release it once flashing starts.

Connect with a Serial Terminal: Use screen, PuTTY, minicom, or Thonny IDE's built-in serial terminal to connect to your ESP32 (usually at 115200 baud). You should see the MicroPython REPL prompt (>>>).

Project List
Each project directory contains a main.py file (and sometimes other modules) that implements the described functionality.

Project 1: Blinking an LED
Description: The classic "Hello, World!" for embedded systems. Blinks an LED connected to a specified GPIO pin at a regular interval.

Hardware: ESP32, 1 LED, 1 current-limiting resistor (e.g., 220 Ohm), jumper wires.
Connection: LED Anode (long leg) to ESP32 GPIO (e.g., GPIO2), LED Cathode (short leg) to resistor, resistor to GND.

Project 2: Button Input
Description: Reads the state of a push button connected to a GPIO pin and prints whether it's pressed or released to the REPL.

Hardware: ESP32, 1 push button, jumper wires.
Connection: One side of button to ESP32 GPIO (e.g., GPIO13), other side of button to GND. Use internal pull-up resistor.

Project 3: PWM LED Fading
Description: Uses Pulse Width Modulation (PWM) to fade an LED in and out smoothly, demonstrating analog-like control with digital pins.

Hardware: ESP32, 1 LED, 1 current-limiting resistor.
Connection: Same as Project 1.

Project 4: Wi-Fi Station Mode
Description: Connects the ESP32 to a Wi-Fi network (acting as a station). Prints the IP address upon successful connection.

Configuration: Update SSID and PASSWORD in main.py.

Project 5: Simple Web Server (Toggle LED)
Description: Sets up the ESP32 as a Wi-Fi station and hosts a basic web server. You can access an IP address in your browser to toggle an LED on/off.

Hardware: ESP32, 1 LED, 1 current-limiting resistor.
Connection: Same as Project 1.
Configuration: Update SSID and PASSWORD in main.py.

Project 6: DHT11/DHT22 Temperature & Humidity Sensor
Description: Reads temperature and humidity data from a DHT11 or DHT22 sensor and prints it to the REPL.

Hardware: ESP32, DHT11/DHT22 sensor, jumper wires.
Connection: DHT Data pin to ESP32 GPIO (e.g., GPIO4), VCC to 3.3V, GND to GND.
Library: Requires dht.py library (often pre-installed or easily found online).

Project 7: I2C LCD Display (16x2)
Description: Displays text on a 16x2 LCD screen connected via an I2C PCF8574 adapter.

Hardware: ESP32, 16x2 LCD with I2C adapter, jumper wires.
Connection: ESP32 SDA to LCD SDA, ESP32 SCL to LCD SCL, VCC to 3.3V, GND to GND.
Library: Requires lcd_api.py and i2c_lcd.py libraries.

Project 8: MQTT Client (Publish Sensor Data)
Description: Connects to an MQTT broker and publishes dummy sensor data (or actual sensor data if combined with Project 6) to a topic.

Configuration: Update MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, WIFI_SSID, WIFI_PASSWORD.

Project 9: Analog Read (Potentiometer)
Description: Reads analog voltage from a potentiometer connected to an ADC (Analog-to-Digital Converter) pin and prints the raw value.

Hardware: ESP32, 1 potentiometer (e.g., 10k Ohm), jumper wires.
Connection: Potentiometer outer pins to 3.3V and GND, middle pin to an ADC-enabled GPIO (e.g., GPIO34, GPIO35, GPIO36, GPIO39).

Project 10: Deep Sleep Mode
Description: Demonstrates using ESP32's deep sleep feature to conserve power. The ESP32 wakes up after a set duration, performs a task (e.g., blinks an LED), and goes back to deep sleep.

Hardware: ESP32, 1 LED, 1 current-limiting resistor.
Connection: Same as Project 1.
Note: For reliable deep sleep wake-up, connect GPIO16 to RST.

Project 11: SPI Communication (e.g., with an SD Card - conceptual)
Description: A conceptual example showing how to initialize SPI communication. While a full SD card example is complex, this provides the basic SPI setup.

Hardware: ESP32, SPI device (e.g., SD card module, SPI sensor).
Connection: Connect MISO, MOSI, SCK, CS pins.
Note: A full SD card example would require an SD card library.

Project 12: WebREPL Access
Description: Enables WebREPL on the ESP32, allowing you to access the MicroPython REPL and upload files wirelessly via a web browser.

Configuration: Set a password for WebREPL.
Usage: Access http://<ESP32_IP_ADDRESS>/html/ in your browser.

Project 13: HTTP GET Request
Description: Connects to Wi-Fi and performs an HTTP GET request to a specified URL, printing the response content to the REPL.

Configuration: Update WIFI_SSID, WIFI_PASSWORD, and URL_TO_FETCH.

Project 14: Wi-Fi Access Point Mode
Description: Configures the ESP32 to act as a Wi-Fi Access Point (AP), creating its own network that other devices can connect to.

Configuration: Set AP_SSID and AP_PASSWORD.

Project 15: RTC (Real-Time Clock) Usage
Description: Demonstrates how to set and retrieve time from the ESP32's internal Real-Time Clock (RTC). Useful for time-stamping data or scheduling tasks.

Note: The RTC on ESP32 is typically not battery-backed, so time will reset on power loss unless synchronized (e.g., via NTP).

How to Run a Project
Connect ESP32: Plug your ESP32 board into your computer via USB.

Navigate to Project Directory: Open your terminal/command prompt and cd into the specific project directory (e.g., cd project_01_blink_led).

Upload main.py (and any other .py files):

Using ampy:

ampy --port /dev/ttyUSB0 put main.py
# If there are other files, e.g., dht.py for Project 6:
# ampy --port /dev/ttyUSB0 put dht.py

(Replace /dev/ttyUSB0 with your ESP32's serial port.)

Using Thonny IDE:

Open main.py in Thonny.

Go to Run -> Configure interpreter... and select "MicroPython (ESP32)" and your correct port.

Go to Run -> Upload current script as main.py.

If there are multiple files, use View -> Files to upload them manually.

Reset ESP32: After uploading, press the "EN" or "RST" button on your ESP32 board to restart it and run the new main.py.

Monitor REPL: Observe the output in your serial terminal.

Contributing
Feel free to contribute to this repository by:

Adding new projects.

Improving existing code or documentation.

Reporting issues or suggesting enhancements.

Please follow standard GitHub practices (fork, create a branch, commit, push, pull request).
