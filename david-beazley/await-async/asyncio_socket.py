from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
#from threading import Thread
#from multiprocessing import Process
#from twisted.internet import reactor, protocol
import asyncio

class EchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def connection_lost(self, exc):
        self.transport = None

    def data_received(self, data):
        self.transport.write(data)

def main(port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(EchoProtocol, "", port)
    srv = loop.run_until_complete(coro)
    loop.run_forever()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        #echo_handler(client, addr)
        #Thread(target=echo_handler, args=(client, addr)).start()
        Process(target=echo_handler, args=(client, addr)).start()

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
