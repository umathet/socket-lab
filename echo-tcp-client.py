import socket
import sys

def main():
    # Server information
    HOST = input("Enter server IP: ")
    PORT = 5000
    
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
        
        while True:
            # Get message from user
            message = input("Enter message (or 'exit' to quit): ")
            
            if message.lower() == 'exit':
                print("Closing connection...")
                break
            
            # Send data to server
            sock.sendall(message.encode('utf-8'))
            
            # Receive response from server
            response = sock.recv(1024).decode('utf-8')
            print(f"\nServer response:\n{response}\n")

if __name__ == "__main__":
    main()
