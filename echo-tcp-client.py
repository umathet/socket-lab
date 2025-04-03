import socket
import os
import sys

# Server configuration
HOST = 'R3'  # The server's hostname or IP address
PORT = 12346  # The port used by the server

def main():
    # Check if file path is provided as command-line argument
    if len(sys.argv) != 2:
        print("Usage: python tcp_file_transfer_client.py <file_path>")
        return
    
    file_path = sys.argv[1]
    
    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist")
        return
    
    # Get file size
    file_size = os.path.getsize(file_path)
    
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print(f"Connected to server {HOST}:{PORT}")
        
        # Send file size first (as a 10-byte string)
        size_str = f"{file_size:010d}"
        client_socket.sendall(size_str.encode('utf-8'))
        
        # Send the file data
        with open(file_path, 'rb') as f:
            data = f.read()
            client_socket.sendall(data)
        
        print(f"Sent file '{file_path}' ({file_size} bytes)")
        
        # Receive confirmation from server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
        
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
    
