import sys, time, os, json, pytz
from pysnmp.hlapi import *
from OID_Datacenter import *
from datetime import datetime
import paho.mqtt.client as mqtt


class set_get:

    def Getdata(self, oid, *more_oids):

        cmdGen = cmdgen.CommandGenerator()

        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
            cmdgen.CommunityData(public),
            cmdgen.UdpTransportTarget((192.168.0.100, 161)),
            oid,
            *more_oids
        )

        results = {}


        if errorIndication:
            print(errorIndication)
        else:
            if errorStatus:
                print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex)-1] or '?'
                    )
                )
            else:
                for name, val in varBinds:
                    listdata = ('name':name, 'value':val)
                    results.append( listdata )
                    result = [results]
        return result






#class Menuu():                  #class for unifying functions from set_get() class
#    value = set_get()           #call class set_get()


#    def menu_get(self):         #function to get data
#        value = set_get()


    #    data_send_Temperature = value.Get_Temperature()
#        transport_data(broker, port, data_send_Temperature, '/param/AGITD001/temp')             #deliver data to server


if __name__ == '__main__':
    transpport = Menuu()
    gett = set_get()

    os.system('clear')

    while True:
        AC_Presisi = gett.Getdata(AC_Presisi_1_Status_Dry)
        value_dump = json.dumps(AC_Presisi)
        value_dump.append(value_dump)
        print(value_dump)

        AC_Presisi = gett.Getdata(AC_Presisi_1_Alarm_Dry)
        value_dump = json.dumps(AC_Presisi)
        value_dump.append(value_dump)
        print(value_dump)

        time.sleep(10)
