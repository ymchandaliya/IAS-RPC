import json

data = json.load(open("contract.json"))

functions = data['remote_procedures']

clientFile = open("rpc_client1.py", "w")

clientFile.write("import socket\nimport json\n\n")

for i in functions:
    funcName = i['procedure_name']
    # print(funcName)
    clientFile.write("def " + funcName+"(")
    pars = []
    paramString = ""
    for j in i['parameters']:
        clientFile.write(j['parameter_name'] + ', ')
        pars.append(j['parameter_name'])
        paramString += j['parameter_name'] + ', '
    clientFile.write("):\n")
    
    dataSent = {"procedure_name":funcName, "parameters":[], "return_type":i["return_type"]}
    j = 0
    for k in i["parameters"]:            
        # k["value"] = k['parameter_name']
        dataSent["parameters"].append(k)
        # dataSent += k['parameter_name']+ "=" + "eval(" + str(pars[j]) + ")"  + "-"+ k['data_type']+','
        # # str(pars[j])+
        j += 1



    clientFile.write("\tpars = [" + paramString + "]\n")
    # clientFile.write("\tdetails = data['remote_procedures'][0]\n")
    # clientFile.write("\tdataSent = " +  str(dataSent)+ "\n")
    clientFile.write("\tdetails = " +  str(dataSent)+ "\n")
    clientFile.write("\tdataSent = None\n")
    clientFile.write("\tfunc = details['procedure_name']\n")
    clientFile.write("\tdataSent = func+'$'\n")
    clientFile.write("\tj = 0\n")
    clientFile.write("\tfor i in details[\"parameters\"]:\n")
    clientFile.write("\t\tdataSent += i['parameter_name']+\"=\"+str(pars[j])+\"-\"+i['data_type']+','\n")
    clientFile.write("\t\tj += 1\n")
    clientFile.write("\t\tdataSent +=  details['return_type']\n")
    clientFile.write("\tprint(dataSent)\n")

    # print(dataSent)
    clientFile.write("\ts = socket.socket()\n")            
    clientFile.write("\tport = 12345\n")            
    clientFile.write("\ts.connect(('127.0.0.1', port))\n")            
    clientFile.write("\ts.send(dataSent.encode())\n")            
    clientFile.write("\tres =  s.recv(1024).decode()\n")            
    clientFile.write("\treturn res\n")            
    clientFile.write("\ts.close()\n\n")            
    
    
    
        

    

