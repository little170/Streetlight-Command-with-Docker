import serial
import time
import binascii
import base64
from time import sleep

port=serial.Serial("/dev/ttyUSB0",baudrate=57600) # to bluetooth HC-05 
lamp_status="off"
def send_command_to_lamp(status):
        if status=="on":
                command="Rx 2 020312013231\r\n"
        if status=="off":
                command="Rx 2 020312003230\r\n"
        port.write(bytes(command,'ASCII'))
        print("sent commmand:"+command+" to lamp")

send_command_to_lamp("off") #shut down light



