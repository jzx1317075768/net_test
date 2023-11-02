import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
serv_sock.bind((host, port))
serv_sock.listen(5)  # 最大连接数为5

print('TCP服务器等待连接...')
while True:
    client_sock, addr = serv_sock.accept()
    print("连接地址：%s" % str(addr))
    while True:
        data = client_sock.recv(1024)
        if not data or data.decode("utf-8"):
            print("客户端断开")
            break
        print(data.decode('utf-8'))
        msg = '欢迎！来自于: %s\r\n' % host
        client_sock.send(msg.encode('utf-8'))
    client_sock.close()

serv_sock.close()
