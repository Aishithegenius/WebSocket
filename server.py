import socket

# Server setup
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # Bind to the address and port
server_socket.listen()  # Start listening for connections

print(f"Server is listening on {HOST}:{PORT}")

while True:
    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive data from the client
    data = conn.recv(1024).decode()  # First message
    hash_data = conn.recv(1024).decode()  # Second message (hash)

    print(f"Received message: {data}")
    print(f"Received hash: {hash_data}")
    # Send a response
    conn.sendall(b"Message received!")
    conn.close()
