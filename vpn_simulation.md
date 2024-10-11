# Overview of Application
The conversion client and server application provides two conversion games:
1. Converting from string variables to integers
2. Converting from string variables to bytes
The user, or client, will receive instruction of two choices for this conversion application. Then, they input One or Two to start the game. If their input other words or do not follow this syntax (first letter capitalization), they will automatically quit the game.

When user enter the game, both games will let user enter a string. There is no limitation of what they can put in. Then, the server will compute and send the result back to the client. After sending the result back, the server stops. The client receives, prints out the result, and stops the client.

# Client->VPN Message Format
HOST: This is the loopback address.
PORT: The port used by the server.
ADDR: This is the address combining HOST and PORT.
client: The socket store the address and maintains connection between client and server.

deal_w_server(): The primary method responsible for starting the client side, guiding clients' action, and integrating other methods to keep every step in track.

s_to_n(client_choice): Used after selecting track 'One'. Receiving calls from the server and gain responses from the server. Also outputs the result.

s_to_b(client_choice): Used after selecting track 'Two'. Receiving calls from the server and gain responses from the server. Also outputs the result.

# VPN->Server Message Format

# Server->VPN Message Format
HOST: This is the loopback address
PORT: The port used by the server
ADDR: The combination of HOST and PORT
server: The socket store the address and maintains connection between client and server.

choice(conn, addr): The choice function enables the connection between client and server, detects client's choice in action and starts corresponding methods.

str_to_num(conn): The method to perform the conversion between string input to an integer by receiving inputs (bytes) from the client, decode bytes into string, convert letters from string into a list of characters, convert characters into integers and sum them up.

str_to_bytes(conn): The method to perform the conversion between string input to bytes by receiving inputs from the client and outputs it.

start(): A integrating method to start the server.

# VPN->Client Message Format

# Example Output
## Testing with echo client and server application


## Testing with conversion client and server application
*Server 1*
server <starting>
<New Connection> ('127.0.0.1', 56307) connecting
Starting number-letter conversion game :)))
Client choose to convert string to numbers
Starting to convert string to numbers
Convert letters from <byte> to <string>
Convert letters from <string> into <a list of characters>
Convert <a list of characters> into <number>
[SEND THE NUMBER BACK TO CLIENT...]
server is <done>

*Client 1*
Connection start.... Try to connect with server...
Successfully connect to the server
Starting number-letter conversion game :)))
There are two games.
1. Convert your input into number.
2. Convert your input to bytes.
Please enter One or Two:One
choice sent, waiting for reply
Reply received
Please enter a word you want to play with:west
Letter sent to the server, waiting for the final response...
Response Received, the result is 451
test client is done, exiting...

*Server 2*
server <starting>
<New Connection> ('127.0.0.1', 56324) connecting
Starting number-letter conversion game :)))
Client choose to convert from string to bytes
Starting to convert strings to bytes
Convert number from <byte> to <string>
Convert string to <byte>
[SEND THE LETTER BACK TO CLIENT...]
server is <done>

*Client 2*
Connection start.... Try to connect with server...
Successfully connect to the server
Starting number-letter conversion game :)))
There are two games.
1. Convert your input into number.
2. Convert your input to bytes.
Please enter One or Two:Two
choice sent, waiting for reply
Reply received
Please enter a word you want to play with:west
Num sent to the server, waiting for the final response...
Response Received, the result is b'west'
test client is done, exiting...

*Server 3*
server <starting>
<New Connection> ('127.0.0.1', 56342) connecting
Starting number-letter conversion game :)))
This client doesn't want to response.
Connection Off
server is <done>

*Client 3*
Connection start.... Try to connect with server...
Successfully connect to the server
Starting number-letter conversion game :)))
There are two games.
1. Convert your input into number.
2. Convert your input to bytes.
Please enter One or Two:thr
choice sent, waiting for reply
choice sent,quitting...
test client is done, exiting...

# Acknowledgments
In this assignment, I massively searched for python syntax, methods, etc. The link listed below are the websites I went throught, but are unnecessarily implemented in my code.
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

