import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen()

while True:
	clientsocket, address = s.accept()
	print(f'connection from {address} established')
	clientsocket.send(bytes('wellcome', 'utf-8'))