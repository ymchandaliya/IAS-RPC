import socket            
from server_procedures import * 

s = socket.socket()        
print ("Socket successfully created")
 
port = 12345               
 
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")           
 
while True:
 
# Establish connection with client.
  c, addr = s.accept()    
  print ('Got connection from', addr )
 
  funcString = c.recv(1024)
  print(funcString.decode())
  funcString = funcString.decode()

  funcName = funcString.split('$')[0]
  paramsList = funcString.split('$')[1].split(',')
  params = paramsList[:len(paramsList)-1]
  retType = funcString.split('$')[1].split(',')[-1]
  print(funcString)
  print(funcName)  
  print(params)  
  print(retType)  

  c.send('Thank you for connecting'.encode())
 
  # Close the connection with the client
  c.close()
   
  # Breaking once connection closed
#   break