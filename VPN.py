#!/usr/bin/env python3

import socket
import arguments
import argparse

# Run 'python3 VPN.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and prints the response')
parser.add_argument('--VPN_IP', help='IP address at which to host the VPN', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which to host the VPN', **arguments.vpn_port_arg)
args = parser.parse_args()

VPN_IP = args.VPN_IP  # Address to listen on
VPN_PORT = args.VPN_port  # Port to listen on (non-privileged ports are > 1023)

def __init__(self, server_ip, server_port, message, server_reply):
    self.SERVER_IP = server_ip
    self.SERVER_PORT = server_port
    self.msg = message
    self.server_reply = server_reply
    self.vpn_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.vpn_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

def parse_message(msg_input):
    msg = msg_input.decode("utf-8")
    # Parse the application-layer header into the destination SERVER_IP, destination SERVER_PORT,
    # and message to forward to that destination
    SERVER_IP, SERVER_PORT, message = msg.split("#")
    return SERVER_IP, SERVER_PORT, message

def connect_client(self):
    print("---Set up ADDR")
    ADDR = (VPN_IP, VPN_PORT)
    print("---Bind ADDR")
    self.vpn_client.bind(ADDR)
    
    print("---VPN starts to accept connection and address")
    self.vpn_client.listen()
    print(f"---Listening success on {ADDR}")
        
# A method to handle client
def handle_client(self):
    print("---Accepting connection from <<CLIENT>>")
    conn,addr = self.vpn_client.accept()
    print("---Connection created")
    print(f"<New Connection> {addr} connecting client")
    connected = True
    while connected:
        print("---Receiving message from client")
        client_msg = conn.recv(1024)
        if not client_msg:
            break
        else:
            print(f"VPN received message: {client_msg}")

            print(f"---Parsing messages: {client_msg}")
            list_client_msg = parse_message(client_msg)
            self.SERVER_IP, self.SERVER_PORT, self.message = list_client_msg
            print(f"Server IP: {self.SERVER_IP}")
            print(f"Server Port: {self.SERVER_PORT}")
            print(f"Client Message: {self.message}")

# A method to send back server's reply to client
def reply_client(self):
    # After receiving server's reply, send the information back to client
    print("---Sending server's reply to client")
    self.vpn_client.sendall(self.server_reply)
    print("---Successfully send server's reply")   

# A method to set up connection with server
def connect_server(self):
    print("---Set up ADDR")
    ADDR = (self.SERVER_IP, self.SERVER_PORT)
    print("---Bind ADDR")
    self.vpn_server.bind(ADDR)
    
def handle_server(self):
    print("---Accepting connection from <<SERVER>>")
    conn,addr = self.vpn_server.accept()
    print("---Connection accepted")
    connected = True
    while connected:
        print(f"---Connected to server")
        print(f"<New Connection> {self.SERVER_IP, self.SERVER_PORT} connecting server")
        print("---Sending the information to server")

        print(f"---Connection established, sending message '{self.message}'")
        print(f"---Decoding message {self.message}")
        self.vpn_server.sendall(self.message.decode())
        print("Message sent, waiting for reply from server")

        self.server_reply = conn.recv(1024)
        print(f"---Receving message: {self.server_reply}")
        if not self.server_reply:
            print("!!Disconnect with server")
            conn.close()
            break

def start():
    print("---VPN starts to listen")
    connect_client()
    connect_server()
    connected = True
    while connected:
        handle_client()
        handle_server()


print("---Setting up for VPN")
start()
print("<<VPN is DONE!>>")





### INSTRUCTIONS ###
# The VPN, like the server, must listen for connections from the client on IP address
# VPN_IP and port VPN_port. Then, once a connection is established and a message recieved,
# the VPN must parse the message to obtain the server IP address and port, and, without
# disconnecting from the client, establish a connection with the server the same way the
# client does, send the message from the client to the server, and wait for a reply.
# Upon receiving a reply from the server, it must forward the reply along its connection
# to the client. Then the VPN is free to close both connections and exit.

# The VPN server must additionally print appropriate trace messages and send back to the
# client appropriate error messages.