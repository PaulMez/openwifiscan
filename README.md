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
```

Run the install script:

```bash
./install_wifi_scanner.sh
```

## Creating the Control File

To Remove
```bash
rm ~/scan.txt
```

To Create
```bash
echo 'scan' > ~/scan.txt
```

## Checking Status and Logs

You can check the status of the service by running:
```bash
systemctl status wifi_scanner.service
```

You can also look at the output and error logs in the specified files:
```bash
cat ~/wifi_scanner/log_output.txt
cat ~/wifi_scanner/log_error.txt
```