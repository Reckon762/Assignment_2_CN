import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(1)
print('Server listening on port 8888')

while True:
    connection, address = server_socket.accept()
    data = connection.recv(1024).decode()
    print(f'Received data from {address}: {data}')

    # Save the message to a file
    with open('messages.txt', 'a') as file:
        file.write(f'Server message received from ({address}): {data}\n')

    connection.close()

