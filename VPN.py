#!/usr/bin/env python3

import socket
import arguments
import argparse
import select

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
        
# A method to handle client
def handle_client(conn, addr):
    print("---Connection created")
    print(f"<New Connection> {addr} connecting client")
    
    print("---Receiving message from client")
    client_msg = conn.recv(1024)
    print(f"VPN received message: {client_msg}")

    print(f"---Parsing messages: {client_msg}")
    SERVER_IP, SERVER_PORT, message = parse_message(client_msg)
    print(f"Server IP: {SERVER_IP}")
    print(f"Server Port: {SERVER_PORT}")
    print(f"Client Message: {message}")
    
    return SERVER_IP, SERVER_PORT, message
        

# A method to send back server's reply to client
def reply_client(conn, server_reply):
    # After receiving server's reply, send the information back to client
    print("---Sending server's reply to client")
    conn.sendall(server_reply)
    print("---Successfully send server's reply")   
    
def handle_server(vpn_server,SERVER_IP,SERVER_PORT,message):
    print("---Estabilishing connection to <<SERVER>>")
    connected = True
    while connected:
        print(f"---Connected to server")
        print(f"<New Connection> {SERVER_IP, SERVER_PORT} connecting server")
        print("---Sending the information to server")

        print(f"---Connection established, sending message '{message}'")
        print(f"---Decoding message {message}")
        vpn_server.sendall(message.encode())
        print("Message sent, waiting for reply from server")

        server_reply = vpn_server.recv(1024)
        print(f"---Receving message: {server_reply}")
        if not server_reply:
            print("!!Disconnect with server")
            vpn_server.close()
            break
        else:
            return server_reply

def start():
    print("---VPN starts to listen")
    # connect_client()
    vpn_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("---Set up ADDR")
    CLIENT_ADDR = (VPN_IP, VPN_PORT)
    print("---Bind ADDR")
    vpn_client.bind(CLIENT_ADDR)
    
    print("---VPN starts to accept connection and address")
    vpn_client.listen()
    print(f"---Listening success on {CLIENT_ADDR}")
    print("---Accepting connection from <<CLIENT>>")
    conn,addr = vpn_client.accept()

    check = 0

    connected = True
    while connected:
        if check >= 1:
            conn.setblocking(0)
            ready = select.select([conn], [], [], 15)
            if ready[0]:
                data = conn.recv(1024)
                if(data == b''):
                    break
            else:
                break



        SERVER_IP, SERVER_PORT, message = handle_client(conn,addr)

        if(SERVER_IP == "Error") and (SERVER_PORT == "Error") and (message == "Error"):
            connected == False
        else:
            vpn_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("---Set up ADDR")
            ADDR = (SERVER_IP, int(SERVER_PORT))
            print("---Connect to ADDR")
            vpn_server.connect(ADDR)

            server_reply = handle_server(vpn_server, SERVER_IP, SERVER_PORT, message)
            reply_client(conn, server_reply)
        check += 1

            
            
            

    print("<<VPN is DONE!>>")
    print("---Close the connection to server")
    vpn_server.close()
    print("---Close the connection to client")
    conn.close()
    print("<<EXIT>>")


print("---Setting up for VPN")
start()



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