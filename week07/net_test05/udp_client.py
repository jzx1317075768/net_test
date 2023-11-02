import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tom', b'Sarah']:
    print('发送数据:' + data.decode('utf-8'))
    s.sendto(data, ('127.0.0.1', 9999))
    # s.sendto(data, ('10.97.229.103', 9999))

    msg, addr = s.recvfrom(1024)

    print(msg.decode('utf-8'))
s.close()
