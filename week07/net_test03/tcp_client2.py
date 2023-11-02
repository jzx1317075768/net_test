import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_sock.connect(('127.0.0.1', 9999))
client_sock.connect(('10.97.229.103', 9999))

print(client_sock.recv(1024).decode('utf-8'))   # 接收欢迎消息
while True:
    data = input('输入待发送的信息:')
    client_sock.send(data.encode('utf-8'))
    msg = client_sock.recv(1024)
    if not msg or msg.decode('utf-8') == '':
        print('断开连接')
        break
    print(msg.decode('utf-8'))
client_sock.close()
