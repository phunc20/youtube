#import socket
#from socket import  *
from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_handler(client, addr)

def echo_handler(client, addr):
    print("Connection from", addr)
    while client:
        while True:
            data = client.recv(100_000)
            if not data:
                break
            client.sendall(data)
    print("Connection closed")

echo_server(('', 25000))
