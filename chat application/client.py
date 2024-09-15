import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))
end = False
while not end:
    client_socket.send(input("Message: ").encode('utf-8'))
    msg = client_socket.recv(1024).decode('utf-8')
    if msg =='quit':
        end = True
    else:
        print(f"Server: {msg}")

client_socket.close()


