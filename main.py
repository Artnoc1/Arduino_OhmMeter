from Tkinter import *
import serial
from time import sleep

ser = serial.Serial('COM4', 19200, timeout=1)

x=5
for _ in range(5):
    
    print("strating in {} sec".format(x))
    x=x-1
    sleep(1)

print("port active >> ")

def port_data():
    try:
        data = ser.readline().split()
        return data[1]

    except Exception as e:
        return 0.0
while True:
    
    print(port_data())

        
