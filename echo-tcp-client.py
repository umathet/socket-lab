import socket
import sys

def main():
    # Hardcoded server IP (R3)
    HOST = "10.10.11.2"  # No input() needed
    PORT = 5000
    
    # Get message from command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 echo_tcp_client.py <message>")
        sys.exit(1)
    message = ' '.join(sys.argv[1:])  # Join all args into one string
    
    # Create socket and connect
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((HOST, PORT))
        except Exception as e:
            print(f"Connection failed: {e}")
            sys.exit(1)
        
        # Send message and print output
        sock.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")  # Match example's "Sent:" line
        
        # Receive response
        response = sock.recv(1024).decode('utf-8')
        print(f"Received: {response}")

if __name__ == "__main__":
    main()
