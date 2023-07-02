# gptd
A systemd daemonization of the openai API. 
An AI chat daemon, providing an interface for interactive chats with any OpenAI API available models (default: GPT-3.5-turbo).

This project includes the Python scripts required for the chat service, a TCP/IP server for client interaction, and a systemd service file for running the service as a daemon on Debian-based Linux systems.
Getting Started

These instructions will get you a copy of the project up and running on your local machine.
Prerequisites

    Python 3.7+
    Debian 11 or similar Linux distribution
    Conda environment (recommended for managing Python dependencies)
    An OpenAI API key (Note: keep your key secure and don't expose it publicly)

Installing

Clone this repository to your local machine
