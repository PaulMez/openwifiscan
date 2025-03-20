#!/bin/bash

# Install necessary packages
sudo apt update
sudo apt install -y python3 python3-pip
sudo pip3 install pywifi

# Create script directory
mkdir -p ~/wifi_scanner
cp wifi_scanner.py ~/wifi_scanner/wifi_scanner.py

# Create a systemd service file
cat <<EOL | sudo tee /etc/systemd/system/wifi_scanner.service
[Unit]
Description=Wi-Fi Scanner Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/wifi_scanner/wifi_scanner.py
WorkingDirectory=/home/pi/wifi_scanner
StandardOutput=file:/home/pi/wifi_scanner/log_output.txt
StandardError=file:/home/pi/wifi_scanner/log_error.txt
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Enable the service to run on startup
sudo systemctl enable wifi_scanner.service