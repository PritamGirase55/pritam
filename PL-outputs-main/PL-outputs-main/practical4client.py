import socket

# Define the server's address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send a message to the server
message = "Hello, server! How are you?"
client_socket.send(message.encode('utf-8'))

# Receive the response from the server
response = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {response}")

# Close the socket
client_socket.close()
