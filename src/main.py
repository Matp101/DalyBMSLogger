import time
import json
import csv
import paho.mqtt.client as mqtt
from daly.dalybms.daly_bms import DalyBMS
from settings import *

#bms
bms = DalyBMS()
bms.connect(serial_port)

#mqtt client
client = mqtt.Client()
client.username_pw_set(mqtt_user, mqtt_password)
client.will_set(mqtt_topic_will, "offline", 0, True)
client.connect(mqtt_server, mqtt_port)
client.publish(mqtt_topic_will, "online", 0, True)
client.loop_start()

#csv file
csv_file = open(csv_path+"bms_"+str(time.time())+".csv", "w")
csv_writer = csv.writer(csv_file)

#write csv header
bms_data = bms.get_all()
csv_writer.writerow(bms_data.keys())

#main loop
while 1:
    bms_data = bms.get_all()
    json_data = json.dumps(bms_data)
    time_json = json.dumps({"time": str(time.time())})
    json_data = json_data[:-1] + "," + time_json[1:]
    client.publish(mqtt_topic, json_data)
    csv_writer.writerow(bms_data.values())

    time.sleep(0.5)

csv_file.close()

