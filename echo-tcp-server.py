import socket

# Server configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345      # Port to listen on

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set socket option to reuse address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the address
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on {HOST}:{PORT}")
    
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected by {client_address}")
        
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {data}")
            
            # Check if secret code is in the data
            if "SECRET" in data:
                # Extract all digits from the string
                digits = [char for char in data if char.isdigit()]
                digit_count = len(digits)
                
                # Prepare response with digits and count
                response = f"Digits in your string: {''.join(digits)}\nTotal digits: {digit_count}"
            else:
                response = "Secret code not found."
            
            # Send the response back to the client
            client_socket.sendall(response.encode('utf-8'))
            print(f"Sent: {response}")
            
        finally:
            # Close the connection
            client_socket.close()
            print("Connection closed")

if __name__ == "__main__":
    main()
