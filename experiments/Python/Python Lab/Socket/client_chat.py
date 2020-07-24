import socket
import select
import errno
import sys

HEADER_LENGTH = 10
IP = '127.0.0.1'
PORT = 8081

username = input('Username:')
username = username.encode('utf-8')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username_header = f"{len(username) :< {HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    new_message = input(f"{username} > ")
    if new_message:
        new_message = new_message.encode('utf-8')
        message_header = f"{len(new_message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(username_header + new_message)

    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('No connection')
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f"{username} > {message}")

    except IOError as exception:
        if exception.errno != errno.EAGAIN and exception.errno != errno.EWOULDBLOCK:
            sys.exit()
        continue

    except Exception as exception:
        print('Error: ', str(exception))
        sys.exit()
