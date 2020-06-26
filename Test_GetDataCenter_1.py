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






class Menuu():                  #class for unifying functions from set_get() class
    gett = set_get()           #call class set_get()
    value_dumps= {}

    def AC_Presisi():
        AC_Presisii = gett.Getdata(AC_Presisi_1_Status_Dry)
        value_dumps = json.dumps(AC_Presisii)
        value_dumps['AC_Presisi_1_Status_Dry']= value_dumps
        print(value_dumps)

        AC_Presisii = gett.Getdata(AC_Presisi_1_Alarm_Dry)
        value_dumps = json.dumps(AC_Presisii)
        value_dumps['AC_Presisi_1_Alarm_Dry']= value_dumps
        print(value_dumps)

        AC_Presisii = gett.Getdata(AC_Presisi_1_WaterLeak_Dry)
        value_dumps = json.dumps(AC_Presisii)
        value_dumps['AC_Presisi_1_WaterLeak_Dry']= value_dumps
        print(value_dumps)

        return value_dumps


    def AC_Standing():
        AC_Standingg = gett.Getdata(AC_Standing_OnOff_Dry)
        value_dumps = json.dumps(AC_Standingg)
        value_dumps['AC_Standing_OnOff_Dry']= value_dumps
        print(value_dumps)

        AC_Standingg = gett.Getdata(AC_Standing_WaterLeak_Dry)
        value_dumps = json.dumps(AC_Standingg)
        value_dumps['AC_Standing_WaterLeak_Dry']= value_dumps
        print(value_dumps)

        return value_dumps


    def Panel_Listrik():
        Panel_Listrikk = gett.Getdata(Panel_Listrik_Dry)
        value_dumps = json.dumps(Panel_Listrikk)
        value_dumps['Panel_Listrik_Dry']= value_dumps
        print(value_dumps)

        return value_dumps

    def Pintu_Lobby():
        Pintu_Lobbyy = gett.Getdata(Pintu_Lobby_Dry)
        value_dumps = json.dumps(Pintu_Lobbyy)
        value_dumps['Pintu_Lobby_Dry']= value_dumps
        print(value_dumps)

        return value_dumps

    def UPS_No1():
        UPS = gett.Getdata(Panel_Listrik_Dry)
        value_dumps = json.dumps(UPS)
        value_dumps['UPS_No1_Dry']= value_dumps
        print(value_dumps)

        return value_dumps


    def MDF_Room():
        MDF = gett.Getdata(MDF_Room_Dry)
        value_dumps = json.dumps(MDF)
        value_dumps['MDF_Room']= value_dumps
        print(value_dumps)

        return value_dumps


    def FM200Server():
        FM200Serverr = gett.Getdata(FM200Server_SingleZones_Dry)
        value_dumps = json.dumps(FM200Serverr)
        value_dumps['FM200Server_SingleZones_Dry']= value_dumps
        print(value_dumps)

        FM200Serverr = gett.Getdata(FM200Server_CrossZones_Dry)
        value_dumps = json.dumps(FM200Serverr)
        value_dumps['FM200Server_CrossZones_Dry']= value_dumps
        print(value_dumps)

        FM200Serverr = gett.Getdata(FM200Server_GasDischarge_Dry)
        value_dumps = json.dumps(FM200Serverr)
        value_dumps['FM200Server_GasDischarge_Dry']= value_dumps
        print(value_dumps)

        FM200Serverr = gett.Getdata(FM200_Trouble_Dry)
        value_dumps = json.dumps(UPS)
        value_dumps['FM200_Trouble_Dry']= value_dumps
        print(value_dumps)

        return value_dumps

    def Ruang_Power():
        Ruang_Powerr= gett.Getdata(Ruang_Power_Hum)
        value_dumps = json.dumps(Ruang_Powerr)
        value_dumps['Ruang_Power_Hum']= value_dumps
        print(value_dumps)

        Ruang_Powerr = gett.Getdata(Ruang_Power_Temp)
        value_dumps = json.dumps(Ruang_Powerr)
        value_dumps['Ruang_Power_Temp']= value_dumps
        print(value_dumps)

        return value_dumps


    def Ruang_Network():
        Ruang_Networkk= gett.Getdata(Ruang_Network_Hum)
        value_dumps = json.dumps(Ruang_Networkk)
        value_dumps['Ruang_Network_Hum']= value_dumps
        print(value_dumps)

        Ruang_Networkk = gett.Getdata(Ruang_Network_Temp)
        value_dumps = json.dumps(Ruang_Networkk)
        value_dumps['Ruang_Network_Temp']= value_dumps
        print(value_dumps)

        return value_dumps


    def Ruang_Monitor():
        Ruang_Monitorr= gett.Getdata(Ruang_Power_Hum)
        value_dumps = json.dumps(Ruang_Monitorr)
        value_dumps['Ruang_Power_Hum']= value_dumps
        print(value_dumps)

        Ruang_Monitorr = gett.Getdata(Ruang_Monitor_Temp)
        value_dumps = json.dumps(Ruang_Monitorr)
        value_dumps['Ruang_Monitor_Temp']= value_dumps
        print(value_dumps)

        return value_dumps

    def Entrance():
        Entrancee= gett.Getdata(Entrance_Besar_Hum)
        value_dumps = json.dumps(Entrancee)
        value_dumps['Entrance_Besar_Hum']= value_dumps
        print(value_dumps)

        Entrancee = gett.Getdata(Entrance_Besar_Temp)
        value_dumps = json.dumps(Entrancee)
        value_dumps['Entrance_Besar_Temp']= value_dumps
        print(value_dumps)

        return value_dumps

    def RunAll():
        while True:
        AC_Presisi()
        AC_Standing()
        Panel_Listrik()
        Pintu_Lobby()
        UPS_No1()
        MDF_Room()
        FM200Server()
        Ruang_Power()
        Ruang_Network()
        Ruang_Monitor()
        Entrance()
        time.sleep(10)

    #def menu_get(self):         #function to get data
    #    value = set_get()


    #    data_send_Temperature = value.Get_Temperature()
    #    transport_data(broker, port, data_send_Temperature, '/param/AGITD001/temp')             #deliver data to server


if __name__ == '__main__':
    transpport = Menuu()
    gett = set_get()

    os.system('clear')

    transpport.RunAll()
