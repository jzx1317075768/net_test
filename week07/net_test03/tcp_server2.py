import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind(('127.0.0.1', 9999))
serv_sock.listen(5)  # 最大连接数为5

print('TCP服务器等待连接...')
while True:
    client_sock, addr = serv_sock.accept()
    print("连接地址：%s" % str(addr))
    client_sock.send('欢迎！\r\n'.encode('utf-8'))
    while True:
        data = client_sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            print('客户端断开连接')
            break
        print('接收的信息：' + data.decode('utf-8'))
        msg = "TCP服务器返回：%s" % data.decode('utf-8')
        client_sock.send(msg.encode('utf-8'))
    client_sock.close()

serv_sock.close()
