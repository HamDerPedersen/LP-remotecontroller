# LP Remote Controller

LP Remote Controller is a simple Python-based tool for remote controlling another device via a web interface. Using this tool, the user can perform actions such as shutting down, rebooting, opening URLs, and files on the remote device.

## Features

- **Shutdown**: Option to shut down the remote device.
- **Reboot**: Option to reboot the remote device.
- **Open URL**: Open a given URL in the default web browser on the remote device.
- **Open File**: Open a given file on the remote device.

## Usage

1. Run `remote.py` on the remote device.
2. Open a web browser and navigate to the specified IP address and port.
3. Perform the desired actions using the buttons on the web interface.

## Requirements

- Python 3.x
- Flask
- Webbrowser (standard library)
- OS: Windows

## Installation

1. Clone this repository to the remote device.
2. Install Flask by running `pip install Flask` in the terminal.
3. Start the tool by running `python remote.py` in the terminal.

## Notes

- Ensure to allow access to the required ports in any firewall settings.
- Exercise caution when using the remote control features as they may affect the device's operation.
