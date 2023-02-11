import socket
import json

def foo(par_1, ):
	pars = [par_1, ]
	details = {'procedure_name': 'foo', 'parameters': [{'parameter_name': 'par_1', 'data_type': 'int'}], 'return_type': 'str'}
	dataSent = None
	func = details['procedure_name']
	dataSent = func+'$'
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
	res =  s.recv(1024).decode()
	return res
	s.close()

def bar(par_1, par_2, ):
	pars = [par_1, par_2, ]
	details = {'procedure_name': 'bar', 'parameters': [{'parameter_name': 'par_1', 'data_type': 'int'}, {'parameter_name': 'par_2', 'data_type': 'str'}], 'return_type': 'int'}
	dataSent = None
	func = details['procedure_name']
	dataSent = func+'$'
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
	res =  s.recv(1024).decode()
	return res
	s.close()

def random_rating():
	pars = []
	details = {'procedure_name': 'random_rating', 'parameters': [], 'return_type': 'int'}
	dataSent = None
	func = details['procedure_name']
	dataSent = func+'$'
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
	res =  s.recv(1024).decode()
	return res
	s.close()

