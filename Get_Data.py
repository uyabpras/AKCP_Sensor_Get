import sys, time, os, json, pytz
from pysnmp.hlapi import *
from res_mqtt_akcp import *
from datetime import datetime
import paho.mqtt.client as mqtt


class set_get: #class function set and get data

    def Get_Temperature(self, timestamp=1):

        dumpdict = []
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in getCmd(SnmpEngine(),
                                  CommunityData('public'),
                                  UdpTransportTarget(('192.168.0.100', 161)),
                                  ContextData(),
                                  ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.1.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.2.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.3.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.4.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.5.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.6.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.8.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.9.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.10.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.11.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.12.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.13.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.14.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.15.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.16.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.17.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.18.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.19.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.20.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.21.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.35.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.36.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.37.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.45.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.46.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.47.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.48.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.49.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.50.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.51.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.54.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.55.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.56.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.57.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.58.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.59.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.2.1.70.0.0.1.1'))):

            if errorIndication:
                print(errorIndication, file = sys.stderr)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
                break

            else:
                if(timestamp):
                    currenttime = str(datetime.now(pytz.timezone('Asia/Jakarta'))).split('.')[0]
                    data_type = {'oid':"data_type", 'value':"Temperature"}
                    dumpdict.append(data_type)                              #append data_type
                    timestampoid = {'oid':"timestamp", 'value':currenttime}
                    dumpdict.append(timestampoid)                           #append time stamp oid

                for varBind in varBinds:
                    oidmsg = varBind.prettyPrint()                                  #data oid
                    oidvalue = str(oidmsg[oidmsg.index("=")+2::])                   #parsing data to get value
                    oiddesc = str(oidmsg[oidmsg.index("::")+2:oidmsg.index("=")])   #parsing data to get MIB
                    listdata = {'oid':oiddesc, 'value':oidvalue}
                    dumpdict.append(listdata)
                    with open('AKCP-data-Temperature.txt', 'a+') as f:
                        f.write("MIB = %s \nValue = %s\n\n" %(oiddesc, oidvalue))
                        f.close


            value_dump = json.dumps(dumpdict)
            print(value_dump)
        return value_dump


    def Get_Humidity(self, timestamp=1):

        dumpdict = []
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in getCmd(SnmpEngine(),
                                  CommunityData('public'),
                                  UdpTransportTarget(('192.168.0.100', 161)),
                                  ContextData(),
                                  ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.1.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.2.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.4.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.4.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.5.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.6.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.8.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.9.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.10.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.11.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.12.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.13.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.14.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.15.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.16.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.17.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.18.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.19.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.20.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.21.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.35.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.36.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.37.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.45.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.46.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.47.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.48.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.49.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.50.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.51.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.54.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.55.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.56.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.57.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.58.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.59.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.70.0.0.1.1')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.3.1.71.0.0.1.0'))):

            if errorIndication:
                print(errorIndication, file=sys.stderr)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
                break

            else:
                if(timestamp):
                    currenttime = str(datetime.now(pytz.timezone('Asia/Jakarta'))).split('.')[0]
                    data_type = {'oid':"data_type", 'value':"Humidity"}
                    dumpdict.append(data_type)                              #append data_type
                    timestampoid = {'oid':"timestamp", 'value':currenttime}
                    dumpdict.append(timestampoid)                           #append time stamp oid

                for varBind in varBinds:
                    oidmsg = varBind.prettyPrint()                                 #data oid
                    oidvalue = str(oidmsg[oidmsg.index("=")+2::])                   #parsing data to get value
                    oiddesc = str(oidmsg[oidmsg.index("::")+2:oidmsg.index("=")])   #parsing data to get MIB
                    listdata = {'oid':oiddesc, 'value':oidvalue}
                    dumpdict.append(listdata)
                    with open('AKCP-data-humidity.txt', 'a+') as f:
                        f.write("MIB = %s \nValue = %s\n\n" %(oiddesc, oidvalue))
                        f.close



            value_dump = json.dumps(dumpdict)
            print(value_dump)
        return value_dump


    def Get_Relay(self, timestamp=1):

        dumpdict = []
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in getCmd(SnmpEngine(),
                                  CommunityData('public'),
                                  UdpTransportTarget(('192.168.0.100', 161)),
                                  ContextData(),
                                  ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.1.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.2.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.6.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.8.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.24.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.25.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.26.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.35.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.36.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.37.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.52.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.53.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.60.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.61.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.12.1.70.0.0.3.0'))):

            if errorIndication:
                print(errorIndication, file=sys.stderr)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
                break

            else:
                if(timestamp):
                    currenttime = str(datetime.now(pytz.timezone('Asia/Jakarta'))).split('.')[0]
                    data_type = {'oid':"data_type", 'value':"Relay"}
                    dumpdict.append(data_type)                              #append data_type
                    timestampoid = {'oid':"timestamp", 'value':currenttime}
                    dumpdict.append(timestampoid)                           #append time stamp oid

                for varBind in varBinds:
                    oidmsg = varBind.prettyPrint()                                 #data oid
                    oidvalue = str(oidmsg[oidmsg.index("=")+2::])                   #parsing data to get value
                    oiddesc = str(oidmsg[oidmsg.index("::")+2:oidmsg.index("=")])   #parsing data to get MIB
                    if oiddesc == "enterprises.3854.2.5.12.1.26.0.0.3.0 " and oidvalue == "1":          #append condition power sensor relay
                        status_relay = {'oid':"status_sensor", 'value':"OFF"}
                        dumpdict.append(status_relay)
                        listdata = {'oid':oiddesc, 'value':oidvalue}
                        dumpdict.append(listdata)
                    elif oiddesc == "enterprises.3854.2.5.12.1.26.0.0.3.0 " and oidvalue == "0":          #append condition power sensor relay
                        status_relay = {'oid':"status_sensor", 'value':"ON"}
                        dumpdict.append(status_relay)
                        listdata = {'oid':oiddesc, 'value':oidvalue}
                        dumpdict.append(listdata)
                    else:
                        listdata = {'oid':oiddesc, 'value':oidvalue}
                        dumpdict.append(listdata)
                    with open('AKCP-data-relay.txt', 'a+') as f:
                        f.write("MIB = %s \nValue = %s\n\n" %(oiddesc, oidvalue))
                        f.close



            value_dump = json.dumps(dumpdict)
            print(value_dump)
        return value_dump



    def Get_Voltage(self, timestamp=1):
        dumpdict = []

        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in getCmd(SnmpEngine(),
                                  CommunityData('public'),
                                  UdpTransportTarget(('192.168.0.100', 161)),
                                  ContextData(),
                                  ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.1.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.2.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.6.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.8.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.35.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.36.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.37.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.46.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.48.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.54.0.0.3.0')), ObjectType(ObjectIdentity('1.3.6.1.4.1.3854.2.5.13.1.56.0.0.3.0'))):
            if errorIndication:
                print(errorIndication, file=sys.stderr)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
                break

            else:
                if(timestamp):
                    currenttime = str(datetime.now(pytz.timezone('Asia/Jakarta'))).split('.')[0]
                    data_type = {'oid':"data_type", 'value':"Voltage"}
                    dumpdict.append(data_type)
                    timestampoid = {'oid':"timestamp", 'value':currenttime}
                    dumpdict.append(timestampoid)

                for varBind in varBinds:
                    oidmsg = varBind.prettyPrint()                                   #append data_type
                    oidvalue = str(oidmsg[oidmsg.index("=")+2::])                   #parsing data to get value
                    oiddesc = str(oidmsg[oidmsg.index("::")+2:oidmsg.index("=")])   #parsing data to get MIB
                    listdata = {'oid':oiddesc, 'value':oidvalue}
                    dumpdict.append(listdata)
                    with open('AKCP-data-Voltage.txt', 'a+') as f:
                        f.write("MIB = %s \nValue = %s\n\n" %(oiddesc, oidvalue))
                        f.close


            value_dump = json.dumps(dumpdict)
            print(value_dump)
        return value_dump

    def countdownTimer(self):                      #countdownTimer for interval
        total_second = 3 * 60 + 00
        while total_second:
            mins, secs = divmod(total_second, 60)
            print('next get data in', f'{mins:02d}:{secs:02d}', end='\r')
            time.sleep(1)
            total_second -= 1
        print("Done!")






class Menuu():                  #class for unifying functions from set_get() class
    value = set_get()           #call class set_get()


    def menu_get(self):         #function to get data
        value = set_get()


        data_send_Temperature = value.Get_Temperature()
        transport_data(broker, port, data_send_Temperature, '/param/AGITD001/temp')             #deliver data to server

        data_send_Humidity = value.Get_Humidity()
        transport_data(broker, port, data_send_Humidity, '/param/AGITD001/hum')             #deliver data to server

        data_send_Relay = value.Get_Relay()
        transport_data(broker, port, data_send_Relay, '/param/AGITD001/relay')             #deliver data to server

        data_send_Voltage = value.Get_Voltage()
        transport_data(broker, port, data_send_Voltage, '/param/AGITD001/voltage')             #deliver data to server

        value.countdownTimer()

if __name__ == '__main__':
    set_getter = Menuu()
    value = set_get()

    os.system('clear')

    while True:
        value.Get_Temperature()
        value.Get_Humidity()
        value.Get_Relay()
        value.Get_Voltage()

        time.sleep(10)
