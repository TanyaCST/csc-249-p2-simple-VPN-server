import socket

HOST = "127.0.0.1"  # This is the loopback address
PORT = 65432        # The port used by the server
ADDR = (HOST, PORT)

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

        client.sendall(client_choice.encode('utf-8'))
        print("choice sent, waiting for reply")


        if client_choice == "One":
            # Start 1. Convert your input into number
            s_to_n(client_choice)

            # After the game complete, stop the loop
            connection = False

        elif client_choice == "Two":
            # Start 2. Convert your input to bytes
            s_to_b(client_choice)

            # After the game complete, stop the loop
            connection = False

        else:
            client.sendall(client_choice.encode('utf-8'))
            print("choice sent,quitting...")
            
            # After the game complete, stop the loop
            connection = False

def s_to_n(client_choice):
    # Check whether replies are received
    reply = client.recv(1024).decode('utf-8')
    print("Reply received")

    # Sending our string variable to the server
    letter_input = input(reply)
    client.sendall(letter_input.encode('utf-8'))
    print("Letter sent to the server, waiting for the final response...")

    # Receiving and outputing the response
    response = client.recv(1024).decode('utf-8')
    print(f"Response Received, the result is {response}")
    

def s_to_b(client_choice):
    # Check whether replies are received
    reply = client.recv(1024).decode('utf-8')
    print("Reply received")
    
    # Sending our string variable to the server
    num_input = input(reply)
    client.sendall(num_input.encode('utf-8'))
    print("Num sent to the server, waiting for the final response...")

    # Receiving and outputing the response
    response = client.recv(1024)
    print(f"Response Received, the result is {response}")
    



if __name__ == "__main__":
    print("Connection start.... Try to connect with server...")
    deal_w_server()
    print("test client is done, exiting...")