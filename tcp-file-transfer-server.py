import socketserver
import os

class FileTransferTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Client connected. Receiving file...")
        
        # Receive filename (assuming it's the first part of the data)
        filename_bytes = self.request.recv(1024)
        # Find the end of the filename (null byte)
        null_byte_pos = filename_bytes.find(b'\0')
        
        if null_byte_pos != -1:
            filename = filename_bytes[:null_byte_pos].decode('utf-8')
            # Start receiving file content (initial content might be in the same packet)
            file_content = filename_bytes[null_byte_pos+1:]
            
            print(f"Receiving file: {filename}")
            
            # Continue receiving file content
            while True:
                data = self.request.recv(4096)
                if not data:
                    break
                file_content += data
            
            # Save the file
            with open(filename, 'wb') as f:
                f.write(file_content)
            
            print(f"File received and saved as '{filename}'")
            
            # Send confirmation to client
            self.request.sendall(f"File '{filename}' received successfully!".encode('utf-8'))
        else:
            print("Invalid file transfer format")
            self.request.sendall("Invalid file transfer format".encode('utf-8'))

if __name__ == "__main__":
    # Set up the server
    HOST, PORT = "0.0.0.0", 5001
    
    # Create the server
    server = socketserver.TCPServer((HOST, PORT), FileTransferTCPHandler)
    
    print(f"File transfer server started on {HOST}:{PORT}")
    print("Waiting for client...")
    
    # Start the server
    server.serve_forever()
