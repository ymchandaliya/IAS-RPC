import socket            
import json

data = json.load(open("contract.json"))
 
# close the connection
print()


def foo(par_1):
    pars = [par_1]
    details = data['remote_procedures'][0]
    dataSent = ""

    func = details['procedure_name']
    dataSent += func+'$'
    j = 0
    for i in details["parameters"]:
        dataSent += i['parameter_name']+"="+str(pars[j])+"-"+i['data_type']+','
        j += 1

    dataSent +=  details['return_type']
    print(dataSent)
    s = socket.socket()            
    port = 12345                   
    s.connect(('127.0.0.1', port))
    s.send(dataSent.encode())
    # receive data from the server and decoding to get the string.
    res =  s.recv(1024).decode()
    return res

    s.close()    
def bar(par_1, par_2):
    pars = [par_1, par_2]
    details = data['remote_procedures'][1]
    dataSent = ""

    func = details['procedure_name']
    dataSent += func+"$"
    j = 0
    for i in details["parameters"]:
        dataSent += i['parameter_name']+"="+str(pars[j])+"-"+i['data_type']+','
        j += 1

    dataSent +=  details['return_type']
    print(dataSent)
    s = socket.socket()            
    port = 12345                   
    s.connect(('127.0.0.1', port))
    s.send(dataSent.encode())

    # receive data from the server and decoding to get the string.
    print (s.recv(1024).decode())

    s.close()    
def random_rating():
    pars = []
    details = data['remote_procedures'][2]
    dataSent = ""

    func = details['procedure_name']
    dataSent += func+":"
    j = 0
    for i in details["parameters"]:
        dataSent += i['parameter_name']+"="+str(pars[j])+"-"+i['data_type']+','
        j += 1

    dataSent +=  details['return_type']
    print(dataSent)
    # s = socket.socket()            
    # port = 12345                   
    # s.connect(('127.0.0.1', port))

    # # receive data from the server and decoding to get the string.
    # print (s.recv(1024).decode())

    # s.close()    