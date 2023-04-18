#coding:utf-8

from socket import *
from time import ctime
import time
import json

#load configuration
# f = open('battery.json')
# battery_config = json.load(f)["channel"]
# f.close()

tcpCliSock = ""

#Create socket connection
def init_socket_connection(host, port, bufsize):
    global tcpCliSock, BUFSIZ
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    BUFSIZ = bufsize
    print('HOST IP: ' + host)
    print('PORT: ' + str(port))
    tcpCliSock.connect((host, port))

def destroy_socket_connection():
    tcpCliSock.close()

#Ask total chanel number
# def get_ChanelNumber(isshow=False):
#     if (isshow == True):
#         print('Send command - :CHANnel[:SOURce]? ')
#     meg = "CHANnel[:SOURce]?\r\n"
#     tcpCliSock.send(meg.encode())
#     print("Output Channel:")
#     print("CH: "+tcpCliSock.recv(BUFSIZ).decode('gbk'))
#     # print("Total Channel Numbers:")
#     # print(tcpCliSock.recv(BUFSIZ).decode('gbk'))
#     return tcpCliSock.recv(BUFSIZ).decode('gbk')

#Set one channel number
def set_OneChanelNumber(CH,isshow):
    if (isshow == True):
        print('Send command - :CHANnel[:SOURce]' +str(CH))
    meg = "CHANnel[:SOURce] "+str(CH)+"\r\n"
    tcpCliSock.send(meg.encode())

#Ask setting channel number
def get_OneChanelNumber(isshow):
    if (isshow == True):
        print('Send command - :CHANnel[:SOURce]?')
    meg = "CHANnel[:SOURce]?\r\n"
    tcpCliSock.send(meg.encode())
    print("Output Channel:")
    print("CH: "+tcpCliSock.recv(BUFSIZ).decode('gbk'))
    return tcpCliSock.recv(BUFSIZ).decode('gbk')

#Ask after setting parallel channel number
def get_ChanelNumberAfterParallel(isshow):
    if (isshow == True):
        print('Send command - :CHAN:PARA:NUMB?  ')
    meg = "CHAN:PARA:NUMB?  \r\n"
    tcpCliSock.send(meg.encode())
    print("Output Channel Numbers (After parallel):")
    print("CH: "+tcpCliSock.recv(BUFSIZ).decode('gbk'))
    return tcpCliSock.recv(BUFSIZ).decode('gbk')

class SpecData():
    def __init__(self,VoltageHighLimit,VoltageLowLimit,CurrentLimit)
#Ask channel spec. <voltage high limit value, voltage low limit value, current limit value, power limit value, CR high limit value, CR low limit value>
def get_ChanelSpec(isshow):
    if (isshow == True):
        print('Send command - :SPEC:ALL?  ')
    meg = "SPEC:ALL?  \r\n"
    tcpCliSock.send(meg.encode())
    str1 = tcpCliSock.recv(BUFSIZ).decode('gbk')
    chunks1 = str1.split(',')
    print("Output Channel:")
    print("CH: "+tcpCliSock.recv(BUFSIZ).decode('gbk'))
    return chunks1

# Set CCC, CVC, CCCVC, CPC, CPCVC, CCD, CVD, CCCVD, CPD and CPCVD modes
def set_Mode(arg1, isshow):
    if (isshow == True):
        print('Send command - :SOUR:MODE' + arg1)
    meg = "SOUR:MODE"+ arg1 + "\r\n"
    tcpCliSock.send(meg.encode())
    
#Set Cutoff time
def set_CutOffTime(arg1, isshow):
    if (isshow == True):
        print('Send command - :SOUR:TIME:CUTOFF' + arg1)
    meg = "SOUR:TIME:CUTOFF"+ arg1 + "\r\n"
    tcpCliSock.send(meg.encode())

#Set Voltage
def set_Voltage(arg1, isshow):
    if(isshow == True):
        print('Send command - :SOUR:VOLT' + arg1)
    meg = "SOUR:VOLT "+ arg1 +"\r\n"
    tcpCliSock.send(meg.encode())

# Set Current Range
def set_CURRent_RANGe(isshow):
    if (isshow == True):
        print('Send command - :SOUR:CURR:RANG:AUTO ON')
    meg = "SOUR:CURR:RANG:AUTO ON\r\n"
    tcpCliSock.send(meg.encode())
# Set Current
def set_CuRRent(arg1, isshow):
    if(isshow == True):
        print('Send command - :SOUR:CURR' + arg1)
    meg = "SOUR:CURR "+ arg1 +"\r\n"
    tcpCliSock.send(meg.encode())
#Set load power
def set_POWerAMPLitude(arg1, isshow):
    if (isshow == True):
        print('Send command - SOUR:POW  ' + arg1)
    meg = "SOUR:POW "+ arg1 +"\r\n"
    tcpCliSock.send(meg.encode())

# Get current mode   
def get_Mode(isshow):
    if (isshow == True):
        print('Send command - SOURce:MODE?')
    meg = "SOURce:MODE? \r\n"
    tcpCliSock.send(meg.encode())
    recv_data = tcpCliSock.recv(BUFSIZ)
    return recv_data.decode('gbk')

# Get current channel
def get_Channel(isshow):
    if (isshow == True):
        print('Send command - CHANnel[:SOURce]?')
    meg = "CHANnel[:SOURce]? \r\n"
    tcpCliSock.send(meg.encode())
    recv_data = tcpCliSock.recv(BUFSIZ)
    return recv_data.decode('gbk')

#Get Cutoff time
def get_CutOffTime(isshow):
    if (isshow == True):
        print('Send command - SOUR:TIME:CUTOFF?')
    meg = "SOUR:TIME:CUTOFF? \r\n"
    tcpCliSock.send(meg.encode())
    recv_data = tcpCliSock.recv(BUFSIZ)
    return recv_data.decode('gbk')

#Get ALL Setting
def get_AllSetting(isshow):
    if (isshow == True):
        print('Send command - SOURce:ALL?')
    meg = "SOURce:ALL? \r\n"
    tcpCliSock.send(meg.encode())
    recv_data = tcpCliSock.recv(BUFSIZ)
    return recv_data.decode('gbk')

#Get Current Voltage
def get_MEASVOLT(isshow, CH):
    if (isshow == True):
        print('Send command - MEAS:VOLT?' + CH)
    meg = "MEAS:VOLT? "+ CH +"\r\n"
    tcpCliSock.send(meg.encode())
    recv_data = tcpCliSock.recv(BUFSIZ)
    return recv_data.decode('gbk')

#Get Current Current
def get_MEASCURR(isshow):
    if (isshow == True):
        print('Send command - MEAS:CURR?')
    meg = "MEAS:CURR?\r\n"
    tcpCliSock.send(meg.encode())
    recv_data = tcpCliSock.recv(BUFSIZ)
    return recv_data.decode('gbk')

#Get Measure Time
def get_MEASTime(isshow):
    if (isshow == True):
        print('Send command - MEASure:TIME?')
    meg = "MEAS:TIME?\r\n"
    tcpCliSock.send(meg.encode())
    recv_data = tcpCliSock.recv(BUFSIZ)
    return recv_data.decode('gbk')

#Clear UVP alarm
def set_ClearUVPAlarm(isshow):
    if (isshow == True):
        print('*CLS')
    meg = "*CLS\r\n"
    tcpCliSock.send(meg.encode())

#Get load state
# def get_Loadstate(isshow):
#     if (isshow == True):
#         print('Send command - OUTPut:STATe?')
#     meg = "OUTPut:STATe?\r\n"
#     tcpCliSock.send(meg.encode())
#     recv_data = tcpCliSock.recv(BUFSIZ)
#     return recv_data.decode('gbk')

#Turn ON/OFF load
def set_TrunONOFFload(arg1,isshow):
    if (isshow == True):
        print('Send command -OUTP:STAT'+ arg1 +"\r\n")
    meg = "OUTP:STAT "+ arg1 +"\r\n"
    tcpCliSock.send(meg.encode())


#Run API
# init_socket_connection('192.168.1.101', 60000, 1024)
# set_CURRentAMPLitude("3",False)
# print(get_CURRentAMPLitude(False))
# set_Function("CP",False)
# print(get_Function(True))
# set_POWerAMPLitude("15",False)
# print(get_POWerAMPLitude(False))
# set_FunctionCVOption("0",False)
# print(get_FunctionCVOption(False))
# set_VoltageRange("LOW",False)
# print(get_VoltageRange(False))
# set_CurrentRange("MED",False)
# set_PUVP("1",False)
# print(get_PUVP(False))
# print(get_CurrentRange(False))
# set_ClearUVPAlarm(False)
# get_hw(False,14,"CVC")
# print(get_MEASVOLT(False))
# print(get_MEASCURR(False))

# set_TrunONOFFload("0",False)
# print(get_MEASCAP(False))
# destroy_socket_connection()