import socket
import os
import threading
import argparse
import sys

# Path to the Unix domain socket
socket_file_path = "/tmp/gptd.sock"

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Flags and arguments for handling connections to gptd')
    parser.add_argument('-c', '--closed', help='Start a closed context session')
    parser.add_argument('-q', '--quick', help='Close connection after handshake')
    parser.add_argument('-s', '--string', help='Send a string on successful handshake')
    args = parser.parse_args()

    # Ensure that the socket file exists
    if not os.path.exists(socket_file_path):
        print("The server is not running.")
        exit(1)

    # Create a socket object
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def send_data():
        if args.closed:
            sock.send("#personal".encode('utf-8'))

        if args.string:
            # If a string was passed as a command line argument, send it to the server
            sock.sendall(args.string.encode('utf-8'))

        if args.quick:
            sock.shutdown(socket.SHUT_WR)


        else:
            while True:
                # Get input from the user
                message = input()

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
        sys.exit(0) # exit after receiving response

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

if __name__ == "__main__":
    main()

