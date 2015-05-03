import socket
from random import randint

dataPoint1 = str(randint(2,99))
dataPoint2 = str(randint(2,99))
dataPoint3 = str(randint(2,99))
dataPoint4 = str(randint(2,99))
dataPoint5 = str(randint(2,99))
dataPoint6 = str(randint(2,99))

host = 'sensehcmc.cloudapp.net'

try:
  UDP_IP = socket.gethostbyname( host )

except socket.gaierror:
  print 'Hostname could not be resolved. Exiting'
  sys.exit()

UDP_PORT = 5005

MESSAGE = """{"Sensor1":""" + dataPoint1 + """, "Sensor2":""" + dataPoint2 + """, "Sensor3":""" + dataPoint3 + """, "Sensor4":""" + dataPoint4 + """, "Sensor5":""" + dataPoint5 + """, "Sensor6":""" + dataPoint6 + "}"

print "TCP target IP:", UDP_IP
print "TCP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_STREAM) # UDP
sock.connect((UDP_IP, UDP_PORT))
sock.send(MESSAGE)
sock.close()