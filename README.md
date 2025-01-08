# Cloud-Mark-1

# PROJECT IDEA : AI-Enabled Smart Assistant for the Visually Impaired

# OBJECTIVE:
Develop an obstacle-detection system that notifies blind users via a mobile phone. Notifications are sent to the cloud and read out loud on the phone as real-time alerts like "Careful, object ahead" or "Careful, human ahead."

# AI Component for Obstacle Detection:
We'll be using a Decision Tree Classifier or K-Nearest Neighbors (KNN) model, both of which are easy to implement and are effective for small datasets. These models will classify the obstacle type (e.g., human, object, no obstacle) based on data from your ultrasonic and IR sensors.

# Components:
Raspberry Pi Zero (used as the controller)
Ultrasonic Sensor (for distance measurement)
IR Sensors (for detecting obstacles and human presence)
LCD Display (optional for local display)
Internet Access (via Wi-Fi)
Cloud Integration Platform (Google Cloud, AWS, or ThingSpeak)

# Step-by-Step Plan:
1. Hardware Setup with Raspberry Pi Zero:
Ultrasonic Sensor:

Connections:
VCC → 3.3V or 5V
GND → Ground
Trig → GPIO Pin (e.g., GPIO 17)
Echo → GPIO Pin (e.g., GPIO 27)
IR Sensor:

Connections:
VCC → 3.3V
GND → Ground
OUT → GPIO Pin (e.g., GPIO 22)
LCD (Optional for local display):

Can use I2C or 16x2 LCD to show real-time status of sensors.

