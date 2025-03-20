import time
import datetime
import os
from pywifi import PyWiFi, const, Profile

LOG_FILE = "wifi_log.txt"

def scan_for_open_wifi():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)  # Wait for scan results
    results = iface.scan_results()
    
    open_networks = []
    for network in results:
        if network.akid != '':
            continue  # Skip if it has a password
        open_networks.append(network.ssid)
    
    return open_networks

def connect_to_wifi(network_name):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    
    # Disconnect if connected to any network
    iface.disconnect()
    time.sleep(1)  # Wait for disconnection
    
    # Create a new profile for the open wifi
    profile = Profile()
    profile.ssid = network_name
    profile.auth = const.AUTH_ALG_OPEN
    profile.akid = ''
    iface.remove_all_networks()
    iface.add_network(profile)
    
    iface.connect(iface.add_network(profile))
    time.sleep(5)  # Wait for connection to establish

    # Check if connected
    if iface.status() == const.IFACE_CONNECTED:
        return True
    return False

def ping_google():
    response = os.system("ping -c 1 google.com > /dev/null 2>&1")
    return response == 0

def log_connection(network_name, ping_result):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: Found open network '{network_name}', ping success: {ping_result}\n")

def main():
    # Check for the control file
    if not os.path.isfile('scan.txt') or 'scan' not in open('scan.txt').read():
        print("Control file not found or does not contain 'scan'. Exiting.")
        return

    while True:
        open_networks = scan_for_open_wifi()
        for network in open_networks:
            print(f"Found open network: {network}")
            if connect_to_wifi(network):
                ping_result = ping_google()
                log_connection(network, ping_result)
                print(f"Successful connection to '{network}', ping success: {ping_result}")
            else:
                print(f"Failed to connect to {network}")

        time.sleep(30)  # Delay before the next scan

if __name__ == "__main__":
    main()