from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
import asyncio

async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = await sock.accept()
        #echo_handler(client, addr)
        #Thread(target=echo_handler, args=(client, addr)).start()
        #Process(target=echo_handler, args=(client, addr)).start()
        await spawn(echo_client(client, addr))

async def echo_client(client, addr):
    print("Connection from", addr)
    async with client:
        while True:
            data = await client.recv(100_000)
            if not data:
                break
            await client.sendall(data)
    print("Connection closed")

#def run(coro):
#    try:
#        coro.send(None)
#    except StopIteration as e:
#        return e.value


#if __name__ == "__main__":
#    run(echo_server(('', 25000)))
