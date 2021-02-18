* install broker (mosquitto)
  [Download | Eclipse Mosquitto](https://mosquitto.org/download/)

```shell
sudo apt-get install mosquitto
```

* install mqtt client (paho-mqtt)
  [eclipse/paho.mqtt.python： paho.mqtt.python](https://github.com/eclipse/paho.mqtt.python)

```shell
pip install paho-mqtt
```

* run mosquitto

```shell
mosquitto -v
```

* publish

```shell
python3 client_pub.py
```

* subscribe

```shell
python3 client_sub.py
```

ref. [MQTT Beginners Guide with Python examples | Python Point](https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4)
