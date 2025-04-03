import socket
import sys

# Server configuration
HOST = 'R3'  # The server's hostname or IP address
PORT = 12345  # The port used by the server

def main():
    # Check if message is provided as command-line argument
    if len(sys.argv) != 2:
        print("Usage: python echo_tcp_client.py <message>")
        return
    
    message = sys.argv[1]
    
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print(f"Connected to server {HOST}:{PORT}")
        
        # Send message to server
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")
        
        # Receive response from server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {response}")
        
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
