

## Send request using `curl`
On one terminal, run
```bash
node http_server.js
```

On another, run
```bash
~/.../engineer-man/node-js/10-http ❯❯❯ curl http://127.0.0.1:9090
~/.../engineer-man/node-js/10-http ❯❯❯ curl http://127.0.0.1:9090 --data 'Hi, MyLifeAlexandre!'
Hi, MyLifeAlexandre!~/.../engineer-man/node-js/10-http ❯❯❯ curl http://127.0.0.1:9090 --data "double quotes work?"
Hidouble quotes work?~/.../engineer-man/node-js/10-http ❯❯❯
```

At this point, if you stop the nodejs process from the first terminal emulator, then if you run the same
requests from the second terminal, you'd get
```bash
~/.../engineer-man/node-js/10-http ❯❯❯ curl http://127.0.0.1:9090 --data "Hidouble quotes work?"
curl: (7) Failed to connect to 127.0.0.1 port 9090: Connection refused
~/.../engineer-man/node-js/10-http ❯❯❯ curl http://127.0.0.1:9090
curl: (7) Failed to connect to 127.0.0.1 port 9090: Connection refused
~/.../engineer-man/node-js/10-http ❯❯❯
```

## Send request using the file `http_client.js`
Do the same as previously, but this time in the second terminal run
```bash
~/.../engineer-man/node-js/10-http ❯❯❯ node http_client.js
brian
~/.../engineer-man/node-js/10-http ❯❯❯
```

Identically, stop the nodejs process in the first terminal to observe the second one
```bash
~/.../engineer-man/node-js/10-http ❯❯❯ node http_client.js
node:events:356
      throw er; // Unhandled 'error' event
      ^

Error: connect ECONNREFUSED 127.0.0.1:9090
    at TCPConnectWrap.afterConnect [as oncomplete] (node:net:1139:16)
Emitted 'error' event on ClientRequest instance at:
    at Socket.socketErrorListener (node:_http_client:462:9)
    at Socket.emit (node:events:379:20)
    at emitErrorNT (node:internal/streams/destroy:188:8)
    at emitErrorCloseNT (node:internal/streams/destroy:153:3)
    at processTicksAndRejections (node:internal/process/task_queues:81:21) {
  errno: -111,
  code: 'ECONNREFUSED',
  syscall: 'connect',
  address: '127.0.0.1',
  port: 9090
}
~/.../engineer-man/node-js/10-http ❯❯❯
```
