import socket

HOST = "127.0.0.1"  # This is the loopback address
PORT = 65432        # The port used by the server
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Ask clients which 
def choice(conn, addr):
    print(f"<New Connection> {addr} connecting")

    print("Starting number-letter conversion game :)))")

    choice_input = conn.recv(1024)
    choice_input = choice_input.decode('utf-8')

    
    if choice_input == "One":
        print("Client choose to convert string to numbers")
        str_to_num(conn)
        

    elif choice_input == "Two":
        print("Client choose to convert from string to bytes")
        str_to_bytes(conn)
        

    else:
        print("This client doesn't want to response.")

        print("Connection Off")
        conn.close()

    
        

# The method to perform the conversion between string input to an integer
def str_to_num(conn):
    instruction = "Please enter a word you want to play with:"
    conn.sendall(instruction.encode('utf-8'))

    connection = True
    while connection:
        # Receiving user input
        letter_byte = conn.recv(1024)
        print(f"Starting to convert string to numbers")

        print("Convert letters from <byte> to <string>")
        letter = letter_byte.decode('utf-8')

        print("Convert letters from <string> into <a list of characters>")
        letter_list = list(letter)


        print("Convert <a list of characters> into <number>")
        # Use loop to loop through the list of characters
        # Convert each of them into number and add the numbers
        sum = 0
        index = 0
        while index < len(letter_list):
            sum += ord(letter_list[index])
            index += 1
            
        # Convert num into string
        num = str(sum)

        # Send the num_byte back to client
        print("[SEND THE NUMBER BACK TO CLIENT...]")
        conn.sendall(num.encode('utf-8'))
        connection = False

        



# Converting 
def str_to_bytes(conn):
    instruction = "Please enter a word you want to play with:"
    conn.sendall(instruction.encode('utf-8'))

    connection = True
    while connection:
        # Receiving user input
        str_byte = conn.recv(1024)
        print(f"Starting to convert strings to bytes")

        # Convert byte letters into string letters
        print("Convert number from <byte> to <string>")
        str_new = str_byte.decode('utf-8')

        # Convert string back to byte
        print("Convert string to <byte>")
        str_output = str_new.encode('utf-8')

        # Encode the string and send the byte back to the client
        print("[SEND THE LETTER BACK TO CLIENT...]")
        conn.sendall(str_output)
        
        connection = False



# Enable the socket and start connecting with clients
def start():
    server.listen()
    start_status = True
    while start_status:
        conn, addr = server.accept()
        choice(conn, addr)
        start_status = False



print("server <starting>")
start()    
print("server is <done>")
server.close()