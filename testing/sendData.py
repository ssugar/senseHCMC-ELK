import socket
from random import randint

dataPoint = str(randint(2,99))

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = """{"Sensor1":""" + dataPoint + "}"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
