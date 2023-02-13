import socket
import json
from server_procedures import *

s = socket.socket()
print ("Socket successfully created")
port = 12345
s.bind(('', port))
print ("socket binded to %s" %(port))
s.listen(5)
print("socket is listening")
while True:
	c, addr = s.accept()
	print ('Got connection from', addr )
	funcString = c.recv(1024)
	print(funcString.decode())
	funcString = funcString.decode()
	funcString = funcString.replace("'", "\"")
	funcDetails = json.loads(funcString)
	funcName = funcDetails["procedure_name"]
