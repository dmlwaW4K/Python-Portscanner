import socket
import subprocess
import platform
print("""
                _          _   _
  ___ ___   __| | ___  __| | | |__  _   _
 / __/ _ \ / _` |/ _ \/ _` | | '_ \| | | |
| (_| (_) | (_| |  __/ (_| | | |_) | |_| |
 \___\___/ \__,_|\___|\__,_| |_.__/ \__, |
     _           _             __   |___/___  _   _  __
  __| |_ __ ___ | |_      ____ \ \      / / || | | |/ /
 / _` | '_ ` _ \| \ \ /\ / / _` \ \ /\ / /| || |_| ' /
| (_| | | | | | | |\ V  V / (_| |\ V  V / |__   _| . \\
 \__,_|_| |_| |_|_| \_/\_/ \__,_| \_/\_/     |_| |_|\_\\
""")

def ping_host(host):
    # Determine the current operating system
    system = platform.system()
    
    # Define the ping command based on the OS
    if system == "Windows":
        command = ['ping', '-n', '4', host]
    else:
        command = ['ping', '-c', '4', host]
    
    # Execute the ping command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Output the result
    if "unreachable" in result.stdout or "timed out" in result.stdout:
        print(f"Host {host} is not reachable")
        return False
    else:
        print(f"Host {host} is reachable")
        return True

def portscanner(host, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} on {host} is open")
            else:
                print(f"Port {port} on {host} is closed")
        except socket.error as e:
            print(f"Error: {e}")
        finally:
            sock.close()

# Ask user for IP address
host = input("Enter the website to scan: ")

# Ping the host before scanning ports
if ping_host(host):
    # Ask user for port number or 'all'
    port_input = input("Enter the port number to scan (or type 'all' for all ports): ")

    # Determine which ports to scan based on user input
    if port_input.lower() == 'all':
        ports = range(1, 65536)  # Scan all ports from 1 to 65535
    else:
        ports = [int(port_input)]  # Scan the specified port number

    # Call the portscanner function with user input
    portscanner(host, ports)
else:
    print("Cannot proceed with port scanning as the host is not reachable.")
