# Import socket module
from socket import * 
import sys # In order to terminate the program
import struct

serverName = 'localhost'
#serverName = '34.69.60.253'
# Assign a port number
serverPort = 12000

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_DGRAM)


#pcode = 0
#entity = 1
#data_string = b'Hello Woorld!!!'
#data_len = len(data)
#data = struct.pack('{}s'.format(data_len), data_string)

#header = [data_len, pcode, entity, data]

#packet = struct.pack('iii'.format(data_len), *datagram)
#orignaldata=struct.unpack('iii',packet)
#print(orignaldata)
#sentence=input('enter your name')
pcode = 0
entity = 1
data = b'Hello World!!!'

data_len = len(data)
while data_len % 4 !=0:
    print(data_len)
    data=data+b' '
    data_len=len(data)

datagram = [data_len, pcode, entity, data]

packet = struct.pack('ihh{}s'.format(data_len), *datagram)
orignaldata=struct.unpack('ihh{}s'.format(data_len),packet)
print(orignaldata)

#clientSocket.connect((serverName, serverPort))
clientSocket. sendto( packet, (serverName, serverPort))
modifiedSentence, serverAddress = clientSocket.recvfrom(2048)
#data_length = len(modifiedSentence) - struct.calcsize('iii')
serverdata = struct.unpack('ihhhhhh', modifiedSentence)

print('From server: ', serverdata)
print('end of phase 1 ...........................')
pcode=serverdata[6]
packet_id=0
#array of zeros
size=serverdata[5]
while size % 4 != 0:
    size=size+1
phaseb_data=size*[0]

print(len(phaseb_data))
print(size)
    
#array of packets
packetarray=[]
while packet_id<serverdata[3]:
    array=[size,pcode,entity,packet_id]
    packet_id=packet_id+1
    s=struct.pack('hhhi',*array)
    packet=s+bytearray(phaseb_data)
    print(len(packet))
    packetarray.append(packet)
for pack in packetarray:
    clientSocket. sendto( pack, (serverName, serverPort))
    
    






































