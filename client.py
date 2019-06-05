import socket


sock = socket.socket()
sock.connect(('127.0.0.1', 5000))
matrix = []
for i in range(0,3):
	matrix.append(input(f'Введите {i+1}-ю строку: '))


sock.send(str(matrix).encode())
print((sock.recv(128).decode()))