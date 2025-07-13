# Project 8: MQTT Client (Publish Sensor Data)
# Description: Connects to an MQTT broker and publishes dummy sensor data
#              (or actual sensor data if combined with Project 6) to a topic.

# Configuration: Update MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, WIFI_SSID, WIFI_PASSWORD.
# Library: Requires 'umqtt.simple' or 'umqtt.robust' client.
#          You need to upload 'umqtt/simple.py' (or robust.py) to your ESP32's /umqtt directory.
#          Find them here: https://github.com/micropython/micropython-lib/tree/master/micropython/umqtt

import network
import time
from umqtt.simple import MQTTClient # Ensure umqtt folder with simple.py is uploaded
import random # For dummy sensor data

# Wi-Fi credentials
WIFI_SSID = "YOUR_WIFI_SSID"     # <<< CHANGE THIS
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD" # <<< CHANGE THIS

# MQTT Broker details
MQTT_BROKER = "broker.hivemq.com" # Public test broker, or your own
MQTT_PORT = 1883
MQTT_CLIENT_ID = b"esp32_sensor_client_" + str(random.randint(0, 1000)).encode() # Unique ID
MQTT_TOPIC = b"esp32/sensor/data" # Topic to publish to

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
        return True
    else:
        print("Wi-Fi connection failed.")
        return False

def connect_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
    try:
        client.connect()
        print(f"Connected to MQTT broker: {MQTT_BROKER}")
        return client
    except Exception as e:
        print(f"Could not connect to MQTT broker: {e}")
        return None

# Main execution
if __name__ == "__main__":
    if not connect_to_wifi(WIFI_SSID, WIFI_PASSWORD):
        print("Exiting: Wi-Fi not connected.")
    else:
        mqtt_client = None
        while mqtt_client is None:
            mqtt_client = connect_mqtt()
            if mqtt_client is None:
                time.sleep(5) # Wait before retrying MQTT connection

        # Simulate sensor readings and publish
        counter = 0
        while True:
            try:
                # Generate dummy sensor data
                temperature = 20.0 + random.uniform(-2.0, 2.0)
                humidity = 60.0 + random.uniform(-5.0, 5.0)
                message = f"{{'temperature': {temperature:.2f}, 'humidity': {humidity:.2f}, 'counter': {counter}}}"

                mqtt_client.publish(MQTT_TOPIC, message.encode())
                print(f"Published to topic '{MQTT_TOPIC.decode()}': {message}")

                counter += 1
                time.sleep(10) # Publish every 10 seconds

            except Exception as e:
                print(f"Error publishing: {e}. Reconnecting MQTT...")
                mqtt_client.disconnect()
                mqtt_client = None
                while mqtt_client is None:
                    mqtt_client = connect_mqtt()
                    if mqtt_client is None:
                        time.sleep(5)
