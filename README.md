### **gptd**
A systemd daemonization of the cli implementation of https://github.com/minimaxir/simpleaichat and the openai API. 
The current alpha gptd runs a tcp/ip server which forwards all incoming data to a single continuous ChatGPT conversation, providing a shared context for system software. Can be further configured with any OpenAI API available models (default: gpt-3.5-turb).

This project includes the Python script(s) required for the continuous chat TCP/IP server, a systemd service file for running the service as a daemon on Debian-based Linux systems, and a .deb.

You can run the python script directly in a terminal for debugging client interactions. STDERR is logged via python.  



Getting Started

These instructions will get you a copy of the project up and running on your local machine.
Prerequisites

    Python 3.7+
    Any Linux distribution should work, .deb is for debian-based distros obviously
    Conda or virtual environment (recommended for managing Python dependencies)
    An OpenAI API key (Note: keep your key secure and don't expose it publicly)

A python requirements.txt file is included
Please note that this software **requires pydantic version 1.10.7**.

Installing

Method 1
Clone this repository to your local machine:

`git clone https://github.com/cbigger/gptd.git`

Install the python dependancies:

`pip install -r requirements.txt`

