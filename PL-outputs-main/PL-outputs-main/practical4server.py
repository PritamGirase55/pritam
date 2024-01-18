import socket

# Define the server's address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}")

# Accept a connection
client_socket, client_address = server_socket.accept()

# Receive data from the client
data = client_socket.recv(1024).decode('utf-8')
print(f"Received from client: {data}")

# Send a response back to the client
response = "Hello, client! I received your message."
client_socket.send(response.encode('utf-8'))

# Close the sockets
client_socket.close()
server_socket.close()
