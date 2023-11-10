import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.0.0.4', 8888))  # Assuming server IP is 10.0.0.4
message = 'Hello from the client'
client_socket.send(message.encode())
client_socket.close()

# Save the message to a file
with open('messages.txt', 'a') as file:
    file.write(f'Client: {message}\n')
