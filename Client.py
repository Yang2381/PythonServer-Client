'''
This is a client socket program
Website for reference
http://www.binarytides.com/python-socket-programming-tutorial/
'''

import socket
import sys

#create an AF_INET (DK what this is), STREAM socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_data(throw_message_here):
     #Sending
     #The message
     message = throw_message_here
     try:
         #Send the message
         #This method continues to send data
         s.sendall(message)
         #Optional send
         #s.send(message)
         result = 'Send done'
         print result
     except socket.error:
         #Send Failed
         result = 'Failed sending'
         sys.exit()
         print result

def _init_socket(host,port):
    try:
        server_ip = socket.gethostbyname(host)
        #Connect to Server
        s.connect ((server_ip , port))
        print 'succed'
    except socket.error, msg:
        print 'Failed to start socket'
        sys.exit()

def _recv_data(buffer_size):
    #Recieve Data
    #1024 represent how much bit recieve at once
    try:
        print 'Data recieved'
        reply = s.recv(1024)
        return reply
    except:
        print 'Failed to recieve'

def _close_socket():
    s.close()
