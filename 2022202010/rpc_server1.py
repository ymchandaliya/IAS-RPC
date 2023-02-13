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
	funcName = funcString.split('$')[0]
	paramsList = funcString.split('$')[1].split(',')
	params = paramsList[:len(paramsList)-1]
	retType = funcString.split('$')[1].split(',')[-1]
	print(funcName)
	print(params)
	print(retType)

	paramSent = []
	for i in params:
		type_param = i.split('-')[1]
		x = (i.split('=')[1].split('-')[0])
		if(i.split('=')[1].split('-')[1] == 'int'):
			x = int(x)
		paramSent.append(x)
	print(paramSent)
	execString = funcName + "("
	for i in range(len(paramSent)):
		execString += "paramSent[" + str(i) + "], "
	execString += ")"
	print(execString)
	res = eval(execString)
	print(res)
	c.send(str(res).encode())
