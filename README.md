# **gptd**
### Overview
A systemd daemonization of the cli implementation of https://github.com/minimaxir/simpleaichat and the openai API. 

The current gptd runs a tcp/ip server which forwards all incoming data to a single continuous ChatGPT conversation, providing a shared context for system software. Can be further configured with any OpenAI API available models (default: gpt-3.5-turb).

This project includes the Python script(s) required for the continuous chat TCP/IP server, a systemd service file for running the service as a daemon on Debian-based Linux systems, a .deb, and standalone server and configuration files under gptd/src.

You can run the python script directly in a terminal for debugging client interactions. STDERR is logged via python.  

<br />
<br />
<br />

### Getting Started

These instructions will get you a copy of the project up and running on your local machine.

Prerequisites

    Python 3.7+
    Any Linux distribution should work, .deb is for debian-based distros obviously
    Conda or virtual environment (recommended for managing Python dependencies)
    An OpenAI API key (Note: keep your key secure and don't expose it publicly)

A python requirements.txt file is included

Please note that this software **requires pydantic version 1.10.7**.
<br />
<br />
<br />
### Install the basic python console server

Clone this repository to your local machine:

`git clone https://github.com/cbigger/gptd.git`

`cd gptd/`


Install the python dependancies:

`pip install -r gptd/usr/local/lib/gpt.d/requirements.txt`


Add your API key to the configuration file located in the /src directory, and

Run the server:

`python src/gptd.py`
<br />
<br />
<br />
### Install the gptd daemon from the .deb

Clone the repository like in the previous paragraph, or download from the versions tab. 
The .deb file is created with and has been tested on an up-to-date debian 11 buster system, but should work on any modern debian distro. 
You can use it to install gptd from within the containing directory with the following command:

`sudo dpkg -i ./gptd.deb` 

Installing this way will not start or enable the gptd service. It will create the service with default file locations per gptd/DEBIAN/postinst:

    INSTALL_DIR="/usr/local/lib/gpt.d"
    SERVICE_FILE="/lib/systemd/system/gptd.service"
    CONFIGURATION_DIR="/etc/gpt.d"

You can start the service with the following command:

`sudo systemctl start gptd`

If you want it spin up at starttime, use this:

`sudo systemctl enable gptd`

**IF THE SERVICE FAILS** it is most likely because you started the service before adding your api key to the .env. You can edit the file after install at /etc/gpt.d/.env, or make the directory and .env file prior to installing with the .deb.  
The service will not restart if it fails, and must be started manually. You can change this by editing the service file:
```
[Service]
...
Restart=always
```

<br />
<br />
<br />

### Manual .deb or systemd installation

You can edit the files under DEBIAN to customize your install directories
