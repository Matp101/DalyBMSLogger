## Settings.py

The settings.py file is used to configure the MQTT server and the serial port. The csv_path is used to store the csv file.

Our settings.py file looks like this:

```md
#mqtt server
mqtt_server = "192.168.103.222"
mqtt_port = 1883
mqtt_user = "user"
mqtt_password = "battery"

#serial port
serial_port = "/dev/ttyS0"

#csv file
csv_path = "/home/pi/"
```