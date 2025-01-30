import socket  
import hashlib 
import requests 
import httplib2  # For advanced HTTP requests

# Socket communication setup
HOST = '127.0.0.1'  # Server address
PORT = 65432        # Server port

# The message to send
message = "Hello, this is a secure message!"

# Calculate the hash of the message
message_hash = hashlib.sha256(message.encode()).hexdigest()
print(f"Message: {message}")
print(f"Calculated hash: {message_hash}")

# Create a socket object and connect to the server
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to the server.")

    # Send the message and hash to the server
    client_socket.sendall(message.encode())  
    client_socket.sendall(message_hash.encode()) 

    # Receive the server's response
    response = client_socket.recv(1024).decode() 
    print(f"Server response: {response}")

except ConnectionError as e:
    print(f"Connection error: {e}")

finally:
    # Close the socket
    client_socket.close()
    print("Client closed.")

# After completing the socket communication part, make HTTP requests

# Using requests library for demonstration
print("\nMaking an HTTP request with requests library...")
try:
    http_response = requests.get('https://httpbin.org/get')
    print(f"HTTP Response status code (requests): {http_response.status_code}")
    print(f"HTTP Response content (requests): {http_response.text}")
except requests.RequestException as e:
    print(f"Error with requests library: {e}")

# Using httplib2 for advanced HTTP requests
print("\nMaking an HTTP request with httplib2 library...")
try:
    http = httplib2.Http()
    response, content = http.request('https://httpbin.org/get', 'GET')
    print(f"HTTP Response status code (httplib2): {response.status}")
    print(f"HTTP Response content (httplib2): {content.decode('utf-8')}")
except Exception as e:
    print(f"Error with httplib2 library: {e}")
