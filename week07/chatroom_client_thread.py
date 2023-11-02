import socket
import threading


def listen(sock):
    while True:
        try:
            msg = sock.recv(1024)
            print(msg.decode('utf-8'))
        except socket.error:
            print("聊天服务器已关闭")
            break


def speak(sock):
    while True:
        try:
            msg = input()
            sock.send(msg.encode('utf-8'))
        except socket.error:
            print("聊天服务器已关闭")
            break


if __name__ == '__main__':
    client_sock = socket.socket()
    # host = socket.gethostname()
    host = "10.97.229.103"
    client_sock.connect((host, 9900))
    t1 = threading.Thread(target=listen, args=(client_sock,))
    t1.start()
    t2 = threading.Thread(target=speak, args=(client_sock,))
    t2.start()
