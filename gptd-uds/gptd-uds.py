#!/usr/bin/env python3
import socketserver
import threading
import os
from simpleaichat import simpleaichat # import AIChat
from dotenv import load_dotenv
import logging
import codecs

logging.basicConfig(filename='uds_server.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def logout(string):
    print(string)
    logging.info(string)


try:
    config_file = "/etc/gpt.d/.env"
    load_dotenv(dotenv_path=config_file)
except FileNotFoundError:
    logout("Configuration file not found. Please update your configuration in /etc/gpt.d/gptd.conf")
    exit()

gpt_api_key = os.getenv("OPENAI_API_KEY")
ai_text_colour = codecs.decode(os.getenv("AI_TEXT_COLOUR"), 'unicode_escape')
ai_name_colour = codecs.decode(os.getenv("AI_NAME_COLOUR"), 'unicode_escape')
text_reset = codecs.decode(os.getenv("TEXT_RESET"), 'unicode_escape')

'''
ai_text_colour = os.getenv("AI_TEXT_COLOUR") #'\033[34m\033[1m'
ai_name_colour = os.getenv("AI_NAME_COLOUR") #'\033[34m\033[1m\033[47m'
text_reset = os.getenv("TEXT_RESET") #'\033[0m'
'''

class ChatHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).decode('utf-8').strip()
            if data:
                logout(f"Received from {self.client_address}: {data}")
                # Send data to the AIChat instance
                response = f"{ai_name_colour}ChatGPT:{text_reset}{ai_text_colour} "
                print(response)
                response += self.server.chat_instance(data)
                # Send response back to the client
                response += (text_reset + '\n')
                self.request.sendall(response.encode('utf-8'))

            else:
                break


class ThreadedUnixServer(socketserver.ThreadingMixIn, socketserver.UnixStreamServer):
    daemon_threads = True
    allow_reuse_address = True

def run_server(character=None, character_command=None, prime=True, model="gpt-3.5-turbo"):

#    assert gpt_api_key, "An API key was not defined."
    chat_instance = simpleaichat.AIChat(console=False, character=character, character_command=character_command, prime=prime, api_key=gpt_api_key)

    # Create the server, binding to localhost on port 9999
    socket_file_path = "/tmp/my_socket.sock"
    if os.path.exists(socket_file_path):
        os.remove(socket_file_path)
    with ThreadedUnixServer(socket_file_path, ChatHandler) as server:
        server.timeout = 1
        server.chat_instance = chat_instance
        logout("Starting server...")



        try:
            while True:
                server.handle_request()
        except KeyboardInterrupt:
            logout("\nShutting down server...")
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    run_server()
