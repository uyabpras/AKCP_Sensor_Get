import sys, time, os, json, pytz
from pysnmp.hlapi import *
from res_mqtt_akcp import *
from datetime import datetime
import paho.mqtt.client as mqtt

while True:
    mesage = subsrequest("52.184.24.179")                               #receive data from server
    mesage = mesage.decode('UTF-8')                                 #decode from subsrequest
    print(mesage, "\n\n")
