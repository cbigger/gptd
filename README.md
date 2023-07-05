# **gptd**

### <u>Overview</u>
#### A Systemd AI Daemon

The current vesrions open a unix domain socket server which forwards all incoming data to a configured model, providing a shared context, continuous chat, or private context, or one-shot command line STDIN and STDOUT use. Can be further configured with any OpenAI API available models (default: gpt-3.5-turb; huggingface integration coming soon!).

There are currently two versions, v1.1 and v1.0. The former has done away with simpleaichat as a loadin/chat handler, and instead uses a tiny custom loader. The latter is kept for backwards compabitability and use with future simpleaichat development.

This project repo includes:
   - a .deb for easy install on debian-based systems
   - an installable command-line client with various arguments
   - python script(s) for the client and server for debugging and cli quick-use
   - all the source code
If you want the most stable files, use a versioned directory. It's best to use only scripts from the same version to be safe. 
**THE FILEPATHS IN THESE INSTRUCTIONS USE GENERIC, NON-VERSIONED DIRECTORY NAMES. Edit as needed.**

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
### Run the basic python console server

Clone this repository to your local machine:

`git clone https://github.com/cbigger/gptd.git`

`cd gptd/`


Install the python dependancies:

`pip install -r gptd/usr/local/lib/gpt.d/requirements.txt`


Add your API key to the configuration file located in the /src directory, and

Run the server:

`python src/gptd-uds.py`
Run the client:
`python src/gptd-uds-client.py`
<br />
<br />

### Install the gptd daemon from the .deb

Clone the repository like in the previous paragraph, or download from the versions tab. 
The .deb file is created with and has been tested on an up-to-date debian 11 bullseye system, but should work on any modern debian distro. 
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

    [Service]

    Restart=always

<br />
<br />

### Manual .deb or systemd installation

You can edit the files under DEBIAN to customimize your .deb creation. the DEBIAN/postinst file creates the configuration file and the systemd unit file, making it a great place for pre-configuration. Once you're happy, package the files with

`dpkg-deb --build gptd`
and install with
`sudo dpkg -i /path/to/your/gptd.deb`

You can also create your own unit and configuration files manually. Follow the packaging instructions in gptd/DEBIAN/postinst, and place everything in the proper directories according to that file. Then enable/start the service and you are good to go!
<br />
<br />
<br />
### Interacting with the server

It's a simple unix domain socket server. You send it stuff, it sends stuff back. You can connect to the gptd.sock programmatically, use the gptd-uds-client.py script, or install the client cli.

To do the latter, navigate to src/client (or usr/local/lib/gpt.d/client if you are in a build directory) and type `pip install .` You should enter into a newline with a blinking cursor.
Type something and hit enter to start chatting!

gptd is meant to be used as a tool for further terminal and desktop environment features to hook on to. I, and hopefully others, plan to release further software for AI integration that builds off gptd. Stay tuned!


### Features to come:

   - v1 has a lot of QoL on the way, and further customization. v1.1 is likely to be DBus and desktop env integration
   - Other AI model platforms (especially local llms which accel at coding), either as simpleaichat develops or we do\
   - Broadcast channels, again DBus program interface
   - Unix Domain Sockets implementation  **DONE**\
   - Distro-independent daemon install?\
