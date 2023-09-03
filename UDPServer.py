# Import socket module
from socket import * 
import sys # In order to terminate the program
import struct
from random import randrange

# Assign a port number
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to server address and server port
serverSocket.bind(("localhost", serverPort))
entity=2
repeat=randrange(5,20)
udp_port=randrange(20000,30000)
size=randrange(50,100)
codeA=randrange(100,400)


while True:
        
	print('The server is ready to receive')
	

	packet, clientAddress = serverSocket.recvfrom(1024)
	
	data_len = len(packet) - struct.calcsize('ihh')
	originaldata = struct.unpack('ihh{}s'.format(data_len), packet)
	print(originaldata[0])
	print(originaldata[1])
	datagram=[originaldata[0], originaldata[1], entity, repeat, udp_port, size, codeA]
	print(*datagram)
	serverpacket=struct.pack('ihhhhhh',*datagram)
        
        
       
        
        
	#packet = struct.pack('iii{}s'.format(data_len), *originaldata)
	

	serverSocket.sendto(serverpacket, clientAddress)
        
	#pack, clientAddress = serverSocket.recvfrom(1024)
	#packarraysize = len(pack) - struct.calcsize('hhhi')
	#phaseb=struct.unpack('hhhi',pack)
	#print(*phaseb)
	

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
