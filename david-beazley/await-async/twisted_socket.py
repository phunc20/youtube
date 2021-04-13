from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
#from threading import Thread
#from multiprocessing import Process
from twisted.internet import reactor, protocol

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

def main(port):
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(port, factory)
    reactor.run()

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
