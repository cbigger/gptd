#!/usr/bin/env python3
import socket
import os
import threading

# Path to the Unix domain socket
socket_file_path = "/tmp/my_socket.sock"

# Ensure that the socket file exists
if not os.path.exists(socket_file_path):
    print("The server is not running.")
    exit(1)

# Create a socket object
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

def send_data():
    while True:
        # Get input from the user
        message = input() #"Enter a message to send to the server, or q to quit: ")

        if message == 'q':
            break

        # Send the message to the server
        sock.sendall(message.encode('utf-8'))

def receive_data():
    while True:
        # Receive the response from the server
        data = sock.recv(16)
        if data:
            print(f"{data.decode('utf-8')}", end='', flush=True)
        else:
            break

try:
    # Connect the socket
    sock.connect(socket_file_path)

    # Start threads for sending and receiving data
    send_thread = threading.Thread(target=send_data)
    receive_thread = threading.Thread(target=receive_data)
    send_thread.start()
    receive_thread.start()

    # Wait for both threads to finish
    send_thread.join()
    receive_thread.join()

finally:
    # Close the socket when we're done with it
    print("Closing client...")
    sock.close()
