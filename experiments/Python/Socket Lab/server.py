import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# hostname + port
server_socket.bind((socket.gethostname(), 8081))

server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    print(address)
    print('- Connection from: ' + address[0])
    client_socket.send(bytes('Hello client!', 'utf-8'))

    while True:
        time.sleep(3)
        message = f"Time is: {time.time()}"
        message = f"{len(message):<{10}}" + message
        client_socket.send(bytes(message, 'utf-8'))
