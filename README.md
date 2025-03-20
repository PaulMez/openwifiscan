# openwifiscan
openwifiscan - pi



# Wi-Fi Scanner Service for Raspberry Pi

This project sets up a Python-based Wi-Fi scanner that logs open networks around your Raspberry Pi. The service checks for a specific control file (`scan.txt`) and runs the scanner only if the file contains the word "scan". If the file is absent or doesn't contain the word, the service won't run.

## Table of Contents
- [Installation](#installation)
- [Creating the Control File](#creating-the-control-file)
- [Controlling the Service](#controlling-the-service)
- [Checking Status and Logs](#checking-status-and-logs)

## Installation

Make the install script executable:

```bash
chmod +x install_wifi_scanner.sh
