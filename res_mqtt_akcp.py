import paho.mqtt.client as mqtt
import time, json, pytz
from datetime import datetime
import paho.mqtt.subscribe as subscribe

broker="52.184.24.179"
port = 1883
data_buffer = ["Data_buffer"]

mqtt.Client.connected_flag=False

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        print("Connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_publish(client, userdata, result):
    print("data published \n")
    pass


def transport_data(broker, port, data, topic):
    global data_buffer
    i = 0
    time.sleep(1)
    client = mqtt.Client("client_data")
    client.on_connect=on_connect
    client.loop_start()
    try:
        print("Connecting to broker ",broker)
        client.connect(broker,port)
        data_buffer.append(data)
        for i in range(4):
            if i<3 and client.connected_flag == False:
                print("Prepare to connection")
                time.sleep(1)
            elif i>=3 and client.connected_flag == False:
                i += 1
                pass
    except:
        for i in range(4):
            if i<3 and client.connected_flag == False:
                print("In wait loop, Bad Connection")
                time.sleep(1)
                i += 1
            elif i>=3 and client.connected_flag == False:
                if data_buffer[-1] != data:
                    data_buffer.append(data)
                    print("\n", data_buffer, "\n")
                elif data_buffer[-1] == data:
                    pass
            else:
                data_buffer.append(data)

    try:
        print("publising data")
        client.on_publish = on_publish
        client.connect(broker, port)
        ret= client.publish(topic, json.dumps(data_buffer))
        client.loop_stop()
        client.disconnect()
        data_buffer = ["Data_buffer"]
    except Exception as e:
        print("\n", data_buffer, "\n\n")
        pass




def subsrequest(broker):
    data_temp = subscribe.simple("/param/AGITD001/temp", hostname="52.184.24.179")
    # data_hum = subscribe.simple("/param/AGITD001/hum", hostname="52.184.24.179")
    # data_relay = subscribe.simple("/param/AGITD001/relay", hostname="52.184.24.179")
    # data_voltage = subscribe.simple("/param/AGITD001/voltage", hostname="52.184.24.179")
    # interval = subscribe.simple("/param/AGITD001/interval", hostname="52.184.24.179")
    # response = {"temp": data_temp.payload, "hum": data_hum.payload, "relay": data_relay.payload, "voltage":data_voltage.payload, "interval": interval.payload}
    return data_temp.payload

#while True:
#    mesage = subsrequest("52.184.24.179")
#    print(mesage)
