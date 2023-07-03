#!/usr/bin/env python3
import socket
import os

# Path to the Unix domain socket
socket_file_path = "/tmp/my_socket.sock"

# Ensure that the socket file exists
if not os.path.exists(socket_file_path):
    print("The server is not running.")
    exit(1)

# Create a socket object
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    # Connect the socket
    sock.connect(socket_file_path)

    while True:
        # Get input from the user
        message = input("Enter a message to send to the server, or q to quit: ")

        if message == 'q':
            break

        # Send the message to the server
        sock.sendall(message.encode('utf-8'))

        # Receive the response from the server
        data = sock.recv(1024)
        print(f"{data.decode('ascii')}")

finally:
    # Close the socket when we're done with it
    print("Closing client...")
    sock.close()
