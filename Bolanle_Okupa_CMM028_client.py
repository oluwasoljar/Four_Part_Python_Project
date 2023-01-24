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
import socket

msg_count = 1
msg_entry_count = 0
while msg_entry_count <= 2:
    print('\n')
    msgFromClient = input('Enter message: ')

    # items sent to server
    bytesToSend         = str.encode(msgFromClient)
    serverAddressPort   = ("127.0.0.1", 10805)
    bufferSize          = 1024

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)

    split_server_msg = list(format(msgFromServer[0]))
    num_count = 0
    letter_count = 0

    for i in range(len(split_server_msg)):
        if split_server_msg[i] in ['0','1','2','3','4','5','6','7','8','9']:
            num_count += 1
        if split_server_msg[i] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            letter_count += 1
        
    #print(split_server_msg)
    print(num_count, ' numbers in ASCII')
    print(letter_count, ' letters in ASCII')
    print(msg_count, ' messages sent')
    msg_count += 1
    msg_entry_count += 1
