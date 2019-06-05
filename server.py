import socket


def op(matrix):
	return (matrix[0] * (matrix[4] * matrix[8] - matrix[7] * matrix[5]) -
			matrix[1] * (matrix[3] * matrix[8] - matrix[6] * matrix[5]) +
			matrix[2] * (matrix[3] * matrix[7] - matrix[6] * matrix[4]))


new_matrix = []
sock = socket.socket()
sock.bind(('', 5000))
sock.listen()
connection, addr = sock.accept()
matrix = [int(x) for x in connection.recv(128).decode() if x.isdigit()]
connection.send(str((op(matrix))).encode())