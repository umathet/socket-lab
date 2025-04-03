import socket
import sys
import os

def main():
    # Server information
    HOST = input("Enter server IP: ")
    PORT = 5001
    
    # Get filename from user
    filename = input("Enter file path to transfer: ")
    
    # Check if file exists
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)
    
    # Get file size
    file_size = os.path.getsize(filename)
    
    # Create a socket (TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server
        print(f"Connecting to {HOST}:{PORT}...")
        try:
            sock.connect((HOST, PORT))
            print("Connected!")
        except Exception as e:
            print(f"Connection failed: {e}")
            sys.exit(1)
        
        # Get just the filename without the path
        base_filename = os.path.basename(filename)
        
        # Send filename first, followed by null byte as separator
        sock.sendall(base_filename.encode('utf-8') + b'\0')
        
        # Send file content
        with open(filename, 'rb') as f:
            data = f.read(4096)
            while data:
                sock.sendall(data)
                data = f.read(4096)
        
        print(f"File '{filename}' ({file_size} bytes) sent successfully!")
        
        # Shutdown the sending side of the socket
        sock.shutdown(socket.SHUT_WR)
        
        # Receive confirmation from server
        response = sock.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()
