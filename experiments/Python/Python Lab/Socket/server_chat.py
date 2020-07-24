import socket
import select

HEADER_LENGTH = 10
IP = '127.0.0.1'
PORT = 8081

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}


def load_message(client_socket):
    try:
        header = client_socket.recv(HEADER_LENGTH)
        if not len(header):
            return False

        message_length = int(header.decode('utf-8').strip())
        return {'header': header, 'data': client_socket.recv(message_length)}

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(
        sockets_list, [], sockets_list)

    for read_socket in read_sockets:
        if read_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            _message = load_message(client_socket)
            if _message is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = _message

            _log = f"Open connection -- {client_address[0]}:{client_address[1]} - {_message['data'].decode('utf-8')}"
            print(_log)

        else:
            _message = load_message(read_socket)
            if _message is False:
                _log = f"Close connection -- {clients[read_socket]['data'].decode('utf-8')}"
                print(_log)

                sockets_list.remove(read_socket)
                del clients[read_socket]
                continue

            user = clients[read_socket]
            _log = f"New message -- {user['data'].decode('utf-8')}: {_message['data'].decode('utf-8')}"
            print(_log)

            for client in clients:
                if client != read_socket:
                    message = user['header'] + user['data']
                    message += _message['header'] + _message['data']

                    client.send(message)

    for exception_socket in exception_sockets:
        sockets_list.remove(exception_socket)
        del clients[exception_socket]
