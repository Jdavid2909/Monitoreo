
import psutil
import multiprocessing
import random
import time
import json
from paho.mqtt import client as mqtt_client
from datetime import datetime
from ..db.dbConnection import insertMetaData


topic = "arquitectura/group/jhonattan"
broker = "broker.hivemq.com"
port = 1883

# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def getMetaDataOnOS():
    current_datetime = datetime.now()
    data = { "id": "jhonattan","cpu": psutil.cpu_percent(), "memory": psutil.cpu_percent(), "disco": psutil.disk_usage('/').total, "num procesadores":multiprocessing.cpu_count() , "inserDT":current_datetime.strftime("%Y-%m-%d %H:%M:%S")}

    # Convert the dictionary to a JSON string
    json_string = json.dumps(data, indent=2)  # The indent parameter is optional and adds indentation for better readability
    return json_string


def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"{getMetaDataOnOS()}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1



def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
       
        print(f"Received `{msg.payload}` from `{msg.topic}` topic")
        insertMetaData(msg.payload.decode())
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == "__main__":
    run()