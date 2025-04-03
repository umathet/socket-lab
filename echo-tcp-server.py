import socketserver
import re

class EchoTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Receive data from client
        data = self.request.recv(1024).strip().decode('utf-8')
        print(f"Received: {data}")
        
        # Check if SECRET is in the message
        if "SECRET" in data:
            # Extract all digits from the message
            digits = re.findall(r'\d', data)
            digit_count = len(digits)
            
            # Format response with digits and count
            response = f"Secret code found! Digits: {' '.join(digits)}\nTotal digits: {digit_count}"
        else:
            response = "Secret code not found."
        
        # Send response back to client
        self.request.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    # Set up the server
    HOST, PORT = "0.0.0.0", 5000
    
    # Create the server
    server = socketserver.TCPServer((HOST, PORT), EchoTCPHandler)
    
    print(f"Server started on {HOST}:{PORT}")
    print("Waiting for client...")
    
    # Start the server
    server.serve_forever()
