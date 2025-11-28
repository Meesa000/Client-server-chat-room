import socket
import threading

HOST = "127.0.0.1"
PORT = 65000

def server_start():
    
    # create the socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    
    while True:
        server_socket.listen()
        print("Server listening for connections.")

        # when a connection is accepted, it returns connection and adress
        connection, address = server_socket.accept()
        
        #INSERT THREAD HERE
        thread = threading.Thread(target=handle_client, args=(connection,address))
        thread.start()
        
        
    
def handle_client(connection, address):
    
    try:
        client_user = connection.recv(1024)
        client_user = client_user.decode()
        
         
        welcome_msg = f"(Hello {client_user}, you have connected to Asim's chatroom.)"
        connection.send(welcome_msg.encode())
            

        while True:
            
            # issue is connection aborted error every time client types exit whilst recv thread in use
            # recvs any msg from client
            client_msg = connection.recv(1024)
            
            print(client_msg)
            
    except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError) as e:
        print(f"Error: {e}")
    
    finally:
        
        connection.close()
    
server_start()

