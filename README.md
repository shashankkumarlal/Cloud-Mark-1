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

# Python Code for Sensor Data Collection:

import RPi.GPIO as GPIO
import time
import requests

#GPIO pin setup
GPIO.setmode(GPIO.BCM)
TRIG = 17
ECHO = 27
IR_SENSOR_PIN = 22

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

#Function to read distance from ultrasonic sensor
def get_distance():
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(2)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

#Function to check IR sensor state
def get_ir_state():
    return GPIO.input(IR_SENSOR_PIN)

#Main loop
while True:
    distance = get_distance()
    ir_state = get_ir_state()
    
    print(f"Distance: {distance} cm")
    print(f"IR Sensor State: {'Detected' if ir_state else 'Not Detected'}")

    # Send data to cloud (ThingSpeak or IFTTT)
    data = {
        'field1': distance,
        'field2': ir_state
    }
    url = 'https://api.thingspeak.com/update?api_key=YOUR_API_KEY'
    response = requests.get(url, params=data)

    if response.status_code == 200:
        print("Data sent to ThingSpeak successfully!")

    time.sleep(5)

# Explanation:
The ultrasonic sensor measures the distance to nearby obstacles.
The IR sensor detects obstacles or humans.
Data is sent to the cloud platform (ThingSpeak in this case) every 5 seconds.

# Cloud Integration:
Choose Cloud Platform:

Option 1: ThingSpeak (for simplicity):

Create a free account on ThingSpeak.
Create a new channel with two fields: one for distance and one for IR sensor state.
Use the Write API Key provided by ThingSpeak to send sensor data from the Raspberry Pi.
Option 2: IFTTT for Notifications:

Set up an account on IFTTT.
Create an applet where the Webhooks service sends data from your Raspberry Pi to trigger a notification on your phone.
Use ThingSpeak as the service to send the distance and IR sensor data.
Option 3: Google Cloud Functions (for AI/ML processing):

You can send data to Google Cloud and use a basic AI/ML model (like a classification model) to process the sensor data.
Create a Google Cloud Function that takes the sensor data and processes it to classify whether an object is an obstacle, a human, or safe.

# Cloud AI/ML Processing (Optional but Recommended):
Here you can use cloud AI tools to classify the data and provide meaningful results.

Step 1: Train a Basic AI Model:

Use a simple machine learning model (like Logistic Regression, Decision Tree, or Random Forest) to classify the sensor data.
For example, if the distance is below 10 cm and the IR sensor detects an object, classify it as an obstacle.
Step 2: Deploy AI on Google Cloud or AWS Lambda:

Train the model on Google Colab or AWS SageMaker using a small dataset.
Deploy it as a cloud function (Google Cloud Functions or AWS Lambda).
Step 3: Real-time Prediction:

Once the Raspberry Pi sends the data to the cloud, the cloud function can process it and classify the object (e.g., "object ahead," "human detected").
Send the classification result back to the Raspberry Pi or to IFTTT for notification.

# Mobile Notification (Using IFTTT):
You can trigger a notification on a mobile phone using IFTTT:

Create an IFTTT applet:

Set the Webhooks service to listen for incoming HTTP requests.
Configure the action to send a notification (e.g., "Object detected ahead" or "Human detected").
Setup Webhooks on ThingSpeak:

Use the Webhooks feature on ThingSpeak to call the IFTTT applet when certain conditions (like proximity of an object) are met.

# Final Steps:
Test the Setup:

After running the Python code on the Raspberry Pi, observe the data being sent to ThingSpeak.
If you're using IFTTT, check for mobile notifications when an object or human is detected.
Refine and Add AI Later:

Once everything works, you can refine the AI portion in the cloud by integrating more sophisticated models.
