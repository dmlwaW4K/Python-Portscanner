Simple Portscanner
A Python-based port scanner designed to enhance network security by identifying open ports and potential vulnerabilities in devices. This tool also checks host reachability before scanning ports.

Features
Host Reachability Check: Verifies if the target host is reachable using OS-specific ping commands.


Port Scanning: Scans specified ports or all ports (1-65535) to determine if they are open or closed.


Multi-Platform Support: Compatible with both Windows and Unix-based systems.


User Interaction: Simple command-line interface for user inputs.


Detailed Output: Displays host reachability and port status.


Error Handling: Includes exception handling for smooth execution.


Technologies Used

socket for network communication


subprocess for executing system commands


platform for detecting the operating system


How to Use


Clone the Repository:



```git clone https://github.com/dmlwaW4K/Simple-portscanner.git```


```cd Simple-portscanner```


Run the Script:



```python portscanner.py```



Follow the Prompts:

Enter the target host (IP address or domain)
Enter the port number to scan or type 'all' to scan all ports (1-65535)
Example


```Enter the website to scan: example.com
Host example.com is reachable
Enter the port number to scan (or type 'all' for all ports): all
Port 80 on example.com is open
Port 443 on example.com is open
Port 22 on example.com is closed```
```

Code Overview: 


``` highlighting.ping_host(host)```
Checks if the target host is reachable.
Uses subprocess to execute ping commands.
portscanner(host, ports)
Scans specified ports on the target host.
Uses socket to attempt TCP connections and determine port status.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
