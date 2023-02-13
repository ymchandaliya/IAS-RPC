import json

data = json.load(open("contract.json"))

functions = data['remote_procedures']

serverFile = open("rpc_server2.py", "w")

serverFile.write("import socket\nimport json\n")

serverFile.write("from server_procedures import *\n\n")

serverFile.write("s = socket.socket()\n") 
serverFile.write("print (\"Socket successfully created\")\n") 
serverFile.write("port = 12345\n") 
serverFile.write("s.bind(('', port))\n") 
serverFile.write("print (\"socket binded to %s\" %(port))\n") 
serverFile.write("s.listen(5)\n") 
serverFile.write("print(\"socket is listening\")\n") 

serverFile.write("while True:\n") 
serverFile.write("\tc, addr = s.accept()\n") 
serverFile.write("\tprint ('Got connection from', addr )\n") 
serverFile.write("\tfuncString = c.recv(1024)\n") 
serverFile.write("\tprint(funcString.decode())\n") 
serverFile.write("\tfuncString = funcString.decode()\n") 
serverFile.write("\tfuncString = funcString.replace(\"'\", \"\\\"\")\n") 
serverFile.write("\tfuncDetails = json.loads(funcString)\n") 
serverFile.write("\tfuncName = funcDetails[\"procedure_name\"]\n") 


	# 

	# 
	# print(type(funcDetails))
	# 
	# paramsList = funcDetails["parameters"]
	# retType = funcDetails["return_type"]

	# execString = funcName + "("
	# details = None
	# for x in data:
	# 	if(x["procedure_name"] == funcName):
	# 		details = x
	
	# f = 0
	# if(details is None or len(paramsList) != len(details["parameters"])):
	# 	c.send(str("Invalid Function Call").encode())
	# else:
	# 	for i in range(len(paramsList)):
	# 		if(not isinstance(paramsList[i]["value"], eval(details["parameters"][i]["data_type"]))):
	# 			c.send(str("Invalid Function Call, Type Mismatched").encode())
	# 			f = 1
	# 			break
	# 		execString += "paramsList[" + str(i) + "]['value'], "

	# execString += ")"
	# print()
	# print(execString)
	# if(f == 0):
	# 	res = eval(execString)
	# 	print(res)
	# 	c.send(str(res).encode())










# serverFile.write("\tfuncName = funcString.split('$')[0]\n") 
# serverFile.write("\tparamsList = funcString.split('$')[1].split(',')\n") 
# serverFile.write("\tparams = paramsList[:len(paramsList)-1]\n") 
# serverFile.write("\tretType = funcString.split('$')[1].split(',')[-1]\n") 
# serverFile.write("\tprint(funcName)\n\tprint(params)\n\tprint(retType)\n\n")

# serverFile.write("\tparamSent = []\n")
# serverFile.write("\tfor i in params:\n")
# serverFile.write("\t\ttype_param = i.split('-')[1]\n")
# serverFile.write("\t\tx = (i.split('=')[1].split('-')[0])\n")
# serverFile.write("\t\tif(i.split('=')[1].split('-')[1] == 'int'):\n")
# serverFile.write("\t\t\tx = int(x)\n")
# serverFile.write("\t\tparamSent.append(x)\n")
# serverFile.write("\tprint(paramSent)\n")
# serverFile.write("\texecString = funcName + \"(\"\n")
# serverFile.write("\tfor i in range(len(paramSent)):\n")
# serverFile.write("\t\texecString += \"paramSent[\" + str(i) + \"], \"\n")
# serverFile.write("\texecString += \")\"\n")
# serverFile.write("\tprint(execString)\n")
# serverFile.write("\tres = eval(execString)\n")
# serverFile.write("\tprint(res)\n")
# serverFile.write("\tc.send(str(res).encode())\n")

  

  
    
  

  
  
  






    # print(i.split('=')[1].split('-')[0])
  


# serverFile.write("\tc.send('Thank you for connecting'.encode())\n") 

 
 
# Establish connection with client.
  
 
  
  
  

  
  
#   params = paramsList[:len(paramsList)-1]
#   retType = funcString.split('$')[1].split(',')[-1]
#   print(funcString)
#   print(funcName)  
#   print(params)  
#   print(retType)  

#   c.send('Thank you for connecting'.encode())
 
#   # Close the connection with the client
#   c.close()