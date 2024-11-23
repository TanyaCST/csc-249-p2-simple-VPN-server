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


def parse_message(msg_input):
    msg = msg_input.decode("utf-8")
    # Parse the application-layer header into the destination SERVER_IP, destination SERVER_PORT,
    # and message to forward to that destination
    SERVER_IP, SERVER_PORT, message = msg.split("#")
    return SERVER_IP, SERVER_PORT, message
        
print("VPN starting: ||Preparing||")

# Connect to client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as vpn:
    # Opening VPN socket and start to listen
    VPN_PORT = int(VPN_PORT)
    vpn.bind((VPN_IP, VPN_PORT))
    vpn.listen()
    print("---VPN Listening for connection---")

    # Accepting client connection and client address
    conn_c, addr_c = vpn.accept()

    with conn_c:
        print("Connection Succeed: {addr_c}")

        while True:
            # Receiving message from client
            msg = conn_c.recv(1024);

            # If there is no message sent
            if not msg:
                conn_c.sendAll("Error!!! NO MESSAGE")
                print("!!!Error!!! NO MESSAGE")
                break

            print("Message Received - Start to Parse Message")
            # We will parse server information based on message received from client
            SERVER_IP, SERVER_PORT, message = parse_message(msg)
            print("Message Parsed")

            SERVER_ADDR = {SERVER_IP,int(SERVER_PORT)}

            print("Connect to server...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as vpn_s:
                try:
                    vpn_s.connect(SERVER_ADDR)
                    print("Connection Success --- forwarding message")

                    # Forward messages in specific form
                    vpn_s.sendall(bytes(message), "utf-8")
                    print("Message sent. Waiting for reply...")

                    response = vpn_s.recv(1024).decode("utf-8")
                    if not response:
                        print("No response received from server...")
                        conn_c.sendall(bytes("Error!!!No Response From Server"))
                        break
                    else:
                        print("Response is Valid")
                        print("Sending Server Response Back to Client...")
                        conn_c.sendall(response, "utf-8")

                    if not conn_c.recv(1024) and not vpn_s.recv(1024):
                        print("VPN is DONE!")
                        break
                except Exception as e:
                    print("!!! Connection to Server Fail")
                    conn_c.sendall(b"Error!!! Fail to Connect the Server")




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