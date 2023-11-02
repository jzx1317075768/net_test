import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('UDP服务器等待接收...')
while True:
    data, addr = s.recvfrom(1024)
    print('接收来自于(%s:%s):' % addr + data.decode('utf-8'))
    s.sendto(b'UDP Server: %s' % data, addr)

s.close()
