import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
host = "10.97.229.88"
# host = "10.97.229.103"
# host = "127.0.0.1"
port = 9999
client_sock.connect((host, port))
# data = '你好, 来自于：%s\r\n' % host
data = input("输入发送数据： ")
client_sock.send(data.encode('utf-8'))
print('客户端发送:' + data)
msg = client_sock.recv(1024)
print(msg.decode('utf-8'))
client_sock.close()
