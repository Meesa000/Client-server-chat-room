import socket
import threading

HOST = "127.0.0.1"
PORT = 65000


def client():
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    # receives msg from server on connection
    client_startup(client_socket)
    
    
    while True:
        try:
            thread = threading.Thread(target=handle_msg, args=(client_socket,))
            thread.start()
            
        except Exception as e:
            print(f"Exception: {e}")
    
    
    
def client_startup(client_socket):
    
    print("What is your name?: ")
    username = input()
    client_socket.send(username.encode())
    
    server_welcome_msg = client_socket.recv(1024)
    server_welcome_msg = server_welcome_msg.decode()
    
    print(server_welcome_msg)
    
    
    
def handle_msg(client_socket):
    
    while True:
                
        msg = input()
        try:
            if msg == "exit":
                client_socket.close()
                break
            else:
                client_socket.send(msg.encode())
                msg = input()
        except OSError as e:
            print(f"Error from client side: {e}")
            


    
client()