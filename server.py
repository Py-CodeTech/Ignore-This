import socket
import threading
from colorama import Fore

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected_clients = []

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen()
            Fore.GREEN
            print(f"Server listening on {self.host}:{self.port}")
            Fore.WHITE

            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"Connected to {client_address}")
                self.connected_clients.append(client_socket)

                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()

        except Exception as e:
            Fore.RED
            print(f"Server error: {e}")
            Fore.WHITE
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket, client_address):
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    self.disconnect_client(client_socket)
                    break

                print(f"Received from {client_address}: {data}")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
        finally:
            self.disconnect_client(client_socket)

    def disconnect_client(self, client_socket):
        if client_socket in self.connected_clients:
            print(f"Connection closed")
            client_socket.close()
            self.connected_clients.remove(client_socket)

    def list_clients(self):
        Fore.BLUE
        print("Connected clients:")
        for index, client_socket in enumerate(self.connected_clients):
            client_address = client_socket.getpeername()
            print(f"{index+1}: {client_address}")
            print("")
            print("")
            Fore.WHITE

    def send_to_client(self, client_index, message):
        if 0 <= client_index < len(self.connected_clients):
            target_socket = self.connected_clients[client_index]
            target_socket.send(message.encode())
        else:
            Fore.RED
            print("Invalid client index")
            Fore.WHITE

    def send_to_all(self, message):
        for client_socket in self.connected_clients.values():
            client_socket.send(message.encode())

def main():
    host = '127.0.0.1'
    port = 12354

    server = Server(host, port)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    while True:
        option = input('''
                       --------------------
                       |Enter option:-    |
                       |                  |
                       |1: List clients   |
                       |2: Send to client |
                       |3: Send to all    |
                       |4: Exit           | 
                       --------------------
                       
                       >>> ''')
        
        if option == '1':
            server.list_clients()
        elif option == '2':
            server.list_clients()
            print("")
            client_index = int(input("Enter client index: ")) - 1
            message = input("Enter message: ")
            server.send_to_client(client_index, message)
        elif option == '3':
            print("")
            message = input("Enter message: ")
            server.send_to_all(message)
        elif option == '4':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()





