import socket
import arguments
import argparse

# Run 'python3 client.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and print the response')
parser.add_argument('--server_IP', help='IP address at which the server is hosted', **arguments.ip_addr_arg)
parser.add_argument('--server_port', help='Port number at which the server is hosted', **arguments.server_port_arg)
parser.add_argument('--VPN_IP', help='IP address at which the VPN is hosted', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which the VPN is hosted', **arguments.vpn_port_arg)
parser.add_argument('--message', default=['Hello, world'], nargs='+', help='The message to send to the server', metavar='MESSAGE')
args = parser.parse_args()

SERVER_IP = args.server_IP  # The server's IP address
SERVER_PORT = args.server_port  # The port used by the server
VPN_IP = args.VPN_IP  # The server's IP address
VPN_PORT = args.VPN_port  # The port used by the server
MSG = ' '.join(args.message) # The message to send to the server
ADDR = VPN_IP,VPN_PORT

def encode_message(message):
    # Add an application-layer header to the message that the VPN can use to forward it
    return str(SERVER_IP) + "#" + str(SERVER_PORT) + "#" + message

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def deal_w_server():
    print("Successfully connect to the server")

    # Telling client what is their first input
    print("Starting number-letter conversion game :)))")

    connection = True

    while connection:
        print("There are two games.")
        print("1. Convert your input into number.")
        print("2. Convert your input to bytes.")
        client_choice = input("Please enter One or Two:")
        client_choice_sent = encode_message(client_choice)

        client.sendall(client_choice_sent.encode('utf-8'))
        print("choice sent, waiting for reply")


        if client_choice == "One":
            # Start 1. Convert your input into number
            s_to_n()

            # After the game complete, stop the loop
            connection = False

        elif client_choice == "Two":
            # Start 2. Convert your input to bytes
            s_to_b()

            # After the game complete, stop the loop
            connection = False

        else:
            client.sendall(client.sendall(encode_message(client_choice).encode('utf-8')))
            print("choice sent,quitting...")
            
            # After the game complete, stop the loop
            connection = False

def s_to_n():
    # Check whether replies are received
    reply = client.recv(1024).decode('utf-8')
    print("Reply received")

    # Sending our string variable to the server
    letter_input = input(reply)
    letter_input = encode_message(letter_input)
    client.sendall(letter_input.encode('utf-8'))
    print("Letter sent to the server, waiting for the final response...")

    # Receiving and outputing the response
    response = client.recv(1024).decode('utf-8')
    print(f"Response Received, the result is {response}")
    

def s_to_b():
    # Check whether replies are received
    reply = client.recv(1024).decode('utf-8')
    print("Reply received")
    
    # Sending our string variable to the server
    num_input = input(reply)
    client.sendall(encode_message(num_input).encode('utf-8'))
    print("Num sent to the server, waiting for the final response...")

    # Receiving and outputing the response
    response = client.recv(1024)
    print(f"Response Received, the result is {response}")
    



if __name__ == "__main__":
    print("Connection start.... Try to connect with server...")
    deal_w_server()
    print("test client is done, exiting...")