"""
Task 4 – A Local UDP Server
Overview
This task involves creating 2 pieces of code; a “server” process and a “client” process. 
These will communicate with each other using UDP. The server will listen for messages sent to it and
then respond. The client will send a message to the server then listen to its response.
Details - Server
Your server will need to be in a Python file (*.py). There are instructions on how to set this running
from the command prompt on the module Moodle page.
The server should keep listening for UDP communications on the local machine (127.0.0.1) on port 10805.
Every time it receives a message, it should decode it using ASCII format. It should then count 
(a) the number of letters and 
(b) the number of numbers in the message. 
Finally, it should send these pieces of information back to the process that sent the original message.
The server should print output on the screen each time it receives and sends a message so you can see
what it is doing. It should also print out the total number of messages it has received each time it 
receives a new message.
Details - Client
Your client can be in either a Python file or a Jupyter notebook.
It should send 3 messages to the client using UDP and print out the responses returned. 
The first message should consist of only letters. The second message should have a mixture of letters
and numbers. The final message should contain letters, numbers and punctuation.
""" 
  
#https://pythontic.com/modules/socket/udp-client-server-example
from codecs import ascii_encode
import socket
import binascii
   
localIP     = "127.0.0.1"
localPort   = 10805
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
msg_count = 0
while(True):
    print(msg_count, ' messages received')
    print(msg_count, ' responses to client side\n')

    # receive the message and ip-address as tuple from client
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    # separate message and ip-address from tuple
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client: {} ".format(message).encode()
    clientIP  = "Client IP Address:{}".format(address)

    msgFromServer = binascii.b2a_uu(clientMsg)
    bytesToSend = msgFromServer

    # print message and ip-address
    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)
    
    msg_count += 1
    