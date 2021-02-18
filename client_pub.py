import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

client = mqtt.Client("inside_temperature_publisher")
client.connect("localhost", 1883) 

while True:
    randNumber = uniform(2.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)
