import socket
import sys

serverIP = "server IP"
port = 5001

def sendFile(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((serverIP, port))
        s.sendall(f"Sending {filename}".encode())
        with open(filename, 'rb') as f:
            data = f.read()
            s.sendall(data)
        
        print(f"Sent file: {filename} :D")

def getFile(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((serverIP, port))
        s.sendall(f"Getting {filename}".encode())
        with open(f"downloading {filename}", 'wb') as f:
            while True:
                data = s.recv(4096)
                if not data:
                    break
                f.write(data)
        
        print(f"Downloaded file as downloaded_{filename}")

if len(sys.argv) != 3:
    print("Usage: fileClient.py [either send or get] filename")
    sys.exit(1)

cmd, filename = sys.argv[1], sys.argv[2]
if cmd == "send":
    sendFile(filename)
elif cmd == "get":
    sendFile(filename)
else:
    print("You typed command wrongly :(")