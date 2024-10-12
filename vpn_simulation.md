# Overview of Application
This Client, VPN, Server application include transferring inforamation in 2 directions:
1. Client -> VPN -> Server
2. Server -> VPN -> Client

This application includes a VPN server (VPN.py), 2 pairs of client and server applications (client and echo server, conversion client and server, basic math client and server).

The client firstly connect to VPN, send their message and the IP address and port to VPN. VPN receives client message, server IP, and server port. Then, VPN connects to the server and send the client message to the server. Server process the message and generates a reply. The server send the reply back to the VPN. Then, after receiving the reply from server, VPN send the server response back to client. 
If there is no proper messages or data send between client, server, and VPN, the connections close.

Here is a simple explanation of conversion client and server application:
The conversion client and server application provides two conversion games:
1. Converting from string variables to integers
2. Converting from string variables to bytes
The user, or client, will receive instruction of two choices for this conversion application. Then, they input One or Two to start the game. If their input other words or do not follow this syntax (first letter capitalization), they will automatically quit the game.

When user enter the game, both games will let user enter a string. There is no limitation of what they can put in. Then, the server will compute and send the result back to the client. After sending the result back, the server stops. The client receives, prints out the result, and stops the client.

# VPN Message Format
HOST: This is the loopback address.
PORT: The port used by the server.
ADDR: This is the address combining HOST and PORT.
client: The socket store the address and maintains connection between client and server.


# Example Output
## Commandline tracing with echo client and server application
*Server*
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 52541)
Received client message: 'b'Hello, world'' [12 bytes]
echoing 'b'Hello, world'' back to client
server is done!

*VPN*
---Setting up for VPN
---VPN starts to listen
---Set up ADDR
---Bind ADDR
---VPN starts to accept connection and address
---Listening success on ('127.0.0.1', 55554)
---Accepting connection from <<CLIENT>>
---Connection created
<New Connection> ('127.0.0.1', 54659) connecting client
---Receiving message from client
VPN received message: b'127.0.0.1#65432#Hello, world'
---Parsing messages: b'127.0.0.1#65432#Hello, world'
Server IP: 127.0.0.1
Server Port: 65432
Client Message: Hello, world
---Set up ADDR
---Connect to ADDR
---Estabilishing connection to <<SERVER>>
---Connected to server
<New Connection> ('127.0.0.1', '65432') connecting server
---Sending the information to server
---Connection established, sending message 'Hello, world'
---Decoding message Hello, world
Message sent, waiting for reply from server
---Receving message: b'Hello, world'
---Sending server's reply to client
---Successfully send server's reply
<<VPN is DONE!>>
---Close the connection to server
---Close the connection to client
<<EXIT>>

*Client*
client starting - connecting to VPN at IP 127.0.0.1 and port 55554
connection established, sending message '127.0.0.1#65432#Hello, world'
message sent, waiting for reply
Received response: 'Hello, world' [12 bytes]
client is done!

## Commandline Tracing with basic math client and server application
*Server*
basic math server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 55808)
Received client message: 'b'+1:3:5'' [6 bytes]
requested operation is addition
request includes 3 arguments: 1 3 5
result of operation: 9
sending result message 1+3+5=9
server is done!

*VPN*
---Setting up for VPN
---VPN starts to listen
---Set up ADDR
---Bind ADDR
---VPN starts to accept connection and address
---Listening success on ('127.0.0.1', 55554)
---Accepting connection from <<CLIENT>>
---Connection created
<New Connection> ('127.0.0.1', 55807) connecting client
---Receiving message from client
VPN received message: b'127.0.0.1#65432#+1:3:5'
---Parsing messages: b'127.0.0.1#65432#+1:3:5'
Server IP: 127.0.0.1
Server Port: 65432
Client Message: +1:3:5
---Set up ADDR
---Connect to ADDR
---Estabilishing connection to <<SERVER>>
---Connected to server
<New Connection> ('127.0.0.1', '65432') connecting server
---Sending the information to server
---Connection established, sending message '+1:3:5'
---Decoding message +1:3:5
Message sent, waiting for reply from server
---Receving message: b'1+3+5=9'
---Sending server's reply to client
---Successfully send server's reply
<<VPN is DONE!>>
---Close the connection to server
---Close the connection to client
<<EXIT>>

*Client*
client starting - connecting to VPN at IP 127.0.0.1 and port 55554
would you like to connect to basic math or other? (1 for basic math, 2 for other, 3 to exit) [disclaimer: you can only connect to the server you run, otherwise there will be errors]    1
What (addition/subtraction) equation would you like solved? (Please enter your equation in the following format: +1:3:5 or -1:3:5. The order of the numbers matter.)   +1:3:5
connection established, sending message '127.0.0.1#65432#+1:3:5'
message sent, waiting for reply
Received response: '1+3+5=9' [7 bytes]
client is done!

## Commandline Tracing with conversion client and server application
There is no proper commandline tracing for conversion client and server due to error:


# Acknowledgments
The basic math client and server are created by Emily Ren. I borrowed her model to test the VPN.py because there is an error : *[Errno 35] Resource temporarily unavailable* using conversion client and server. I really appreciate her patience and help in another contry with a 6-hours timezone difference. We did not discussed much, but she solved my biggest problem about the order of enabling files in the terminal.

In this assignment, I massively searched for python syntax, exceptions, and errors mainly related to stopping the connections. The link listed below are the websites I went throught. I was inspired by some of the websites, but not all of the contents from the links listed below are implemented in this application.
https://www.youtube.com/watch?v=3QiPPX-KeSc
https://stackoverflow.com/questions/23267305/python-sockets-peer-to-peer
https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ
https://github.com/MattCrook/python_sockets_multi_threading
https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
https://www.geeksforgeeks.org/multithreading-python-set-1/
https://www.google.com/search?q=self+is+not+defined+python&oq=self+is+not+defined+python&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDU4NTFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
https://groups.google.com/g/ansible-project/c/XVMSdM1dLd8
https://docs.python.org/3/library/socket.html
https://www.youtube.com/watch?v=Iu8_IpztiOU
https://www.youtube.com/watch?v=1_DmPRyvJUQ
https://www.geeksforgeeks.org/__init__-in-python/
https://stackoverflow.com/questions/11576934/creating-peer-to-peer-connections-using-intermediate-server
https://www.w3schools.com/python/gloss_python_raise.asp
https://www.w3schools.com/python/python_classes.asp
https://www.geeksforgeeks.org/with-statement-in-python/
https://www.geeksforgeeks.org/self-in-python-class/
https://stackoverflow.com/questions/55032621/oserror-errno-57-socket-is-not-connected
https://stackoverflow.com/questions/11866792/how-to-prevent-errno-32-broken-pipe
https://stackoverflow.com/questions/7360520/connectiontimeout-versus-sockettimeout
https://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method
