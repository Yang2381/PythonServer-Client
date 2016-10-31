'''
This is a Server program.
Szu Kai Yang

Website for reference
http://www.binarytides.com/python-socket-programming-tutorial/
'''
import socket
import sys
from array import array
from thread import *

#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to a particular address and port
#host = '' #Symbolic name meaning all available interface
#port = 8888 #Arbitrary non-privileged port

def bind_socket(host,port):
    try:
        s.bind((host, port))
    except socket.error , msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

print 'Socket bind complete'

#Start to listen
def start_listen_incoming(number_kept_waiting, buffer_size):
        s.listen(number_kept_waiting)
        #Ex: s.listen(10) 10 connections are waiting to be processed, the 11th will be drop
        print 'Socket now listening'
        while True:
            conn , addr = s.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])
            data = []
            data = conn.recv(buffer_size) #Store data recieved to data array
            return data
            if  not data:
                break
        close_connection()
        while 1:
            #Wait to accept connection
            conn , addr = s.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])

            #Start new thread
            start_new_thread(clientthread ,(conn,))

#Send message to client 1st Argument is the function name to be run, second is the tuple of arguments to the function
def send_to_client(message):
    conn.sendall(message)

#Close listening
def  close_connection():
    conn.close()

#Close socket
def close_socket():
    s.close()
