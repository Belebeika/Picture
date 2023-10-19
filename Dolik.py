import socket
import io
from PIL import Image

while True:
    command = input('Введите "ABOBA": ')
    if command == 'ABOBA':
        temp_image_path = r'<Путь к файлу>'
        with open(temp_image_path, 'rb') as file:
            data = file.read()
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('id', 53210))
        client_sock.sendall(data)
        client_sock.close()
    else:
        break