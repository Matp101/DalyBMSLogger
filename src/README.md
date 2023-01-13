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

## Example json
```json
{
  "soc": {
    "total_voltage": 52.5,
    "current": 0.0,
    "soc_percent": 18.9
  },
  "cell_voltage_range": {
    "highest_voltage": 3.78,
    "highest_cell": 14,
    "lowest_voltage": 3.728,
    "lowest_cell": 1
  },
  "temperature_range": {
    "highest_temperature": 15,
    "highest_sensor": 1,
    "lowest_temperature": 15,
    "lowest_sensor": 1
  },
  "mosfet_status": {
    "mode": "stationary",
    "charging_mosfet": true,
    "discharging_mosfet": true,
    "capacity_ah": 5.67
  },
  "status": {
    "cells": 14,
    "temperature_sensors": 1,
    "charger_running": false,
    "load_running": false,
    "states": {
      "DI1": false,
      "DI2": true
    },
    "cycles": 21
  },
  "cell_voltages": {
    "1": 3.728,
    "2": 3.734,
    "3": 3.734,
    "4": 3.736,
    "5": 3.736,
    "6": 3.742,
    "7": 3.757,
    "8": 3.766,
    "9": 3.768,
    "10": 3.761,
    "11": 3.744,
    "12": 3.78,
    "13": 3.749,
    "14": 3.78
  },
  "temperatures": {
    "1": 15
  },
  "balancing_status": {
    "error": "not implemented"
  },
  "errors": [
    "SOC is too low. level one alarm"
  ]
}
```