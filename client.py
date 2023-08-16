import socket

# Define the server's host and port
HOST = '127.0.0.1'
PORT = 12354

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

try:
    while True:
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

        if response == "EXIT-1":
            break

except KeyboardInterrupt:
    print("Client terminated by user.")

finally:
    client_socket.close()
