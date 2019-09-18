# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
number = (int) sys.args[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while 1:
    print ("Enter data to transmit: ENTER to quit")
    data = sys.stdin.readline().strip()
    if not len(data):
        break
#    s.sendall(data.encode('utf-8')    
    s.sendto(data.encode('utf-8'), server_address)
    
    for (int i = 1; i<=number;i+=1):
        new_message= "Number"+(str)i
        s.endto(new_message.encode('utf-8'),server_address)

s.shutdown(1)

