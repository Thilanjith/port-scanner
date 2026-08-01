# port-scanner
A beginner-friendly Python TCP port scanner that scans ports 1–1024, validates IP addresses, and displays open ports. Built to learn socket programming, networking, and ethical cybersecurity practices.


# 🔍 Port Scanner

> A simple Python TCP port scanner created for cybersecurity learning.

> **Disclaimer:** Only scan systems that you own or have explicit permission to test.

---

# Project Overview

This project is a basic TCP port scanner written in Python. It asks the user for an IP address, scans TCP ports **1–1024**, and reports any open ports.

The project is designed for beginners learning networking, sockets, and defensive cybersecurity concepts.

---

# Features

- Scan TCP ports 1–1024
- User-friendly interface
- IP address validation
- Displays open ports
- Handles invalid input gracefully
- Beginner-friendly code
- Uses Python's built-in socket module
- No third-party dependencies

---

# Requirements

- Python 3.9+
- Windows, Linux, or macOS

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Thilanjith/port-scanner.git
```


# Usage

Run:

```bash
python port_scanner.py
```

Example:

```
Enter IP Address:
192.168.1.10
```

The scanner checks TCP ports from **1** to **1024** and reports any open ports.

---

# Example Output

```
Simple Port Scanner

Enter an IP address:
192.168.1.10

Scanning...

[OPEN] Port 22
[OPEN] Port 80
[OPEN] Port 443

==================================
Open Ports

22
80
443
==================================
```

---

# How Port Scanning Helps Defenders

Port scanning is an important defensive cybersecurity technique because it allows administrators to:

- Discover exposed services
- Identify unnecessary open ports
- Verify firewall configurations
- Reduce the attack surface
- Detect misconfigurations
- Improve overall network security

Regular port scanning helps organizations identify potential weaknesses before attackers do.

---

# Learning Outcomes

By completing this project you will understand:

- TCP/IP networking basics
- IP addressing
- Socket programming
- TCP connections
- Port scanning fundamentals
- Error handling in Python
- Python loops and functions
- Basic cybersecurity reconnaissance
- Ethical scanning practices

---

# Future Improvements

- Scan custom port ranges
- Banner grabbing
- Service detection
- Multi-threaded scanning
- UDP scanning
- Hostname support
- Export results to CSV
- Export results to JSON
- Colored terminal output
- Scan multiple hosts
- Progress indicator
- Timing statistics

---

## Technologies Used

- Python 3
- socket
- ipaddress

---

## Author

HARSHA BANDARA

---

## License

MIT License
