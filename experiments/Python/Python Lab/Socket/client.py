import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# hostname + port
server_socket.connect((socket.gethostname(), 8081))

while True:
    message = server_socket.recv(1024)
    print(message.decode('utf-8'))
