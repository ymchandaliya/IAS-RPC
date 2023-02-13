import socket
import json
from server_procedures import *


data = json.load(open("contract.json"))
data = data["remote_procedures"]
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
	print(type(funcString))
	funcString = funcString.replace("'", "\"")

	funcDetails = json.loads(funcString)
	print(type(funcDetails))
	funcName = funcDetails["procedure_name"]
	paramsList = funcDetails["parameters"]
	retType = funcDetails["return_type"]

	execString = funcName + "("
	details = None
	for x in data:
		if(x["procedure_name"] == funcName):
			details = x
	
	f = 0
	if(details is None or len(paramsList) != len(details["parameters"])):
		c.send(str("Invalid Function Call").encode())
	else:
		for i in range(len(paramsList)):
			if(not isinstance(paramsList[i]["value"], eval(details["parameters"][i]["data_type"]))):
				c.send(str("Invalid Function Call, Type Mismatched").encode())
				f = 1
				break
			execString += "paramsList[" + str(i) + "]['value'], "

	execString += ")"
	print()
	print(execString)
	if(f == 0):
		res = eval(execString)
		print(res)
		c.send(str(res).encode())
