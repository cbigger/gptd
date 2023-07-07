import time 
import socket
import os
import threading
import argparse
import sys

# Path to the Unix domain socket
socket_file_path = "/tmp/gptd.sock"

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Flags and arguments for handling connections to gptd\n')
    parser.add_argument('-q', '--quick', action='store_true', help='Close connection immediately. Can use to pipe strings (-s) or files (-f) or for testing server availability\n')
    parser.add_argument('-s', '--string', help='Send a string on connecting to server\n')
    parser.add_argument('-f', '--file', type=str, help='Send contents of a file on connecting to server. Use with -q\n')
    parser.add_argument('-d', '--delay', type=int, default=0, help="Delay in seconds before sending the string or file to the server\n")
    parser.add_argument('-n', '--nocontext', type=int, default=0, help="DEFAULT:Don't create a conversation. Send each message to a fresh chat\n")
    parser.add_argument('-c', '--closed', help='Start a closed context session\n')
    parser.add_argument('-C', '--Common', help='Start a session with the common context\n')



    args = parser.parse_args()

    # Ensure that the socket file exists
    if not os.path.exists(socket_file_path):
        print("The server is not running.")
        exit(1)

    # Create a socket object
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def send_data():
        time.sleep(args.delay)
        if args.file:
            # If a file was specified, send its contents to the server
            with open(args.file, 'r') as file:
                sock.sendall(file.read().encode('utf-8'))

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


