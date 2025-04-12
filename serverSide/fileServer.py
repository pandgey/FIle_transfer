import socket
import os

HOST = '0.0.0.0'  # this will listen to all the available channels
PORT = 5001       # designated port

def handle_client(conn):  # Fixed function name formatting
    command = conn.recv(1024).decode()
    if command.startswith("SEND"):
        filename = command.split(" ")[1]
        with open(filename, 'wb') as f:  # Fixed open function formatting
            print(f"Retrieving {filename}...>-<")
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
            print(f"Received {filename}.... :D")  # Fixed typo in "Received"
    elif command.startswith("GET"):
        filename = command.split(" ")[1]
        if os.path.exists(filename):
            with open(filename, 'rb') as f:  # Fixed open function formatting
                print(f"Sending {filename}.....>-<")
                conn.sendfile(f)
                print(f"Sent {filename}... :D")
        else:
            conn.send(b"File not found :(")  # Fixed b string formatting
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Fixed SOCK_STREAM (was SOC_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on port {PORT}")
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        handle_client(conn)  # Fixed function name for consistency