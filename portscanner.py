import socket
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
host = input("Enter the IP address to scan: ")

# Ask user for port number or 'all'
port_input = input("Enter the port number to scan (or type 'all' for all ports): ")

# Determine which ports to scan based on user input
if port_input.lower() == 'all':
    ports = range(1, 65536)  # Scan all ports from 1 to 65535
else:
    ports = [int(port_input)]  # Scan the specified port number

# Call the portscanner function with user input
portscanner(host, ports)
