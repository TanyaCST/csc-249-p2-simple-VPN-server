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

vpn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (VPN_IP, VPN_PORT)
vpn.bind(ADDR)

def parse_message(message):
    message = message.decode("utf-8")
    # Parse the application-layer header into the destination SERVER_IP, destination SERVER_PORT,
    # and message to forward to that destination
    raise NotImplementedError("Your job is to fill this function in. Remove this line when you're done.")
    return SERVER_IP, SERVER_PORT, message

def client_vpn_server():
    print(f"<New Connection> {addr} connecting client")
    vpn.listen()
    conn, addr = vpn.accept()

    print("Connection Succeed")
    print("Parsing messages")

    client_msg = conn.recv(1024)
    SERVER_IP, SERVER_PORT, message = parse_message(client_msg)
    # server_msg_decoded = server_msg.decode()
    
    print("VPN received message")
    print("Sending the information to server")
    # Send information to vpn
    print(f"<New Connection> {SERVER_IP, SERVER_PORT} connecting server")
    vpn.connect(SERVER_IP, SERVER_PORT)
    print("Connection Succeed")
    server_msg = message.decode()
    print(f"Connection established, sending message '{message}'")
    vpn.sendall(server_msg)
    print("Message sent, waiting for reply")

    server_reply = conn.recv(1024)
    



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