import serial
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
from eload2 import *
# COM_PORT = "COM11"
PORT= input("Input COM PORT NUM: ")
COM_PORT = "COM"+PORT
print(COM_PORT)
serialPort = serial.Serial(
    port=COM_PORT, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
# serialPort.write("m 1 v 1\r\n".encode())
init_socket_connection('192.168.1.101', 60000, 1024)
cell = 1

# cell = None;
send = True
# MAX_COUNT = 1001
serialString = ""  # Used to hold data coming over UART
SmartCell_data = []
chroma_data = []
chroma_time_list = []
step_time_list = []
measure_time_list = []
raw_vol = []
avg_num = 256
def get_plot(data):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_ylabel("Voltage")
    plt.plot(data)
    plt.grid(True)
    plt.show()

def get_precesion(data):
    max_num = max(data)
    min_num = min(data)
    precesion = (max_num - min_num) * 1000
    print(data)
    print(precesion)

def write_csv(SmartCell_data, step_time_list, chroma_data, chroma_time_list):
    print("CSV SAVE")
    with open('output.csv', 'w', newline='', encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Raw", "Cell MEAS time","Chroma MEAS time",])
        for i in range(0, len(SmartCell_data)):
            writer.writerow([raw_vol[i], step_time_list[i], chroma_data[i], chroma_time_list[i]])
set_ClearUVPAlarm(False)
set_Mode('CVC', False)
set_TrunONOFFload('OFF', False)
set_OneChanelNumber('13', False)
set_CutOffTime('30', False)
set_POWerAMPLitude('1.000', False)
set_TrunONOFFload('ON', False)

for i in np.arange(3.400,3.4500,0.001):
    set_Voltage(str(i), False)
    start = time.time()
    for i in range(0, 10):
        serialString = ""
        if send:
            serialPort.write("m ".encode() + "v ".encode() +"avg ".encode()+ str(avg_num).encode() +" ".encode() + "\r\n".encode())
            chroma_val = round(float(get_MEASVOLT(False)),'13')
            time.sleep(1)
            send = False
        while serialPort.in_waiting > 0:
            serialString = serialPort.readline()
            # print(serialString)
            if b"Debug : Raw_Voltage_Orig = " in serialString:
                x = serialString.split(b"=")
                raw = x[1].decode("utf-8")
                raw = raw.split("\n")
                raw = float(raw[0])
                # print(type(raw))
                print(raw)
                chroma_data.append(chroma_val)
                SmartCell_data.append(raw)
                send = True
            if b"Time = " in serialString:
                x = serialString.split(b"=")
                meas_time = x[1].decode("utf-8")
                meas_time = meas_time.split("\n")
                meas_time = float(meas_time[0]) / 1000.0
                # print("執行時間：%f ms" % (meas_time))
                endtime = time.time()
                chroma_time = get_TIME()
                print("Smart CellMEAS時間：%f 秒" % ((endtime - start) + meas_time))
                print("Chroma MEAS時間：%f 秒" % chroma_time)
                chroma_time_list.append(chroma_time)
                step_time_list.append(((endtime - start) + meas_time))
                send = True
                
start = time.time()
for i in range(0, 90):
    while(time.time() < start +(45*(i))):
        pass
    print("Next vol"+" "+ str(i+1))
    for j in range(0, 10):
        if send:
            # serialPort.write("m ".encode() + str(cell).encode() +" ".encode()+ "v".encode() +" ".encode()+ "0".encode() + "\r\n".encode())
            serialPort.write("m ".encode() + "v ".encode() +"avg ".encode()+ str(avg_num).encode() +" ".encode() + "\r\n".encode())
            # print("m "+ str(cell) +" "+ "v" +" "+ str(cell) + "\r\n")
            time.sleep(1)
            send = False
        while serialPort.in_waiting > 0:
            serialString = serialPort.readline()
            # print(serialString)
            if b"Debug : Raw_Voltage_Orig = " in serialString:
                x = serialString.split(b"=")
                raw = x[1].decode("utf-8")
                raw = raw.split("\n")
                raw = float(raw[0])
                # print(type(raw))
                print(raw)
                SmartCell_data.append(raw)
                send = True

            if b"Time = " in serialString:
                x = serialString.split(b"=")
                meas_time = x[1].decode("utf-8")
                meas_time = meas_time.split("\n")
                meas_time = float(meas_time[0]) / 1000.0
                # print("執行時間：%f ms" % (meas_time))
                endtime = time.time()
                print("執行時間：%f 秒" % ((endtime - start) + meas_time))
                measure_time_list.append(meas_time)
                step_time_list.append(((endtime - start) + meas_time))
        # if b"Debug : Calibrated Voltage :" in serialString:
        #     x = serialString.split(b"=")
        #     raw = x[1].decode("utf-8")
        #     print(str(raw))
        #     send = True
write_csv(SmartCell_data, step_time_list, chroma_data, chroma_time_list)
destroy_socket_connection()


      
