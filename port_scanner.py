# port_scanner.py
# Simple TCP Port Scanner
# Scans ports 1-1024

import socket
import ipaddress

START_PORT = 1
END_PORT = 1024


def validate_ip(ip):
    """Validate IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def scan_ports(ip):
    print(f"\nScanning {ip}...\n")

    open_ports = []

    for port in range(START_PORT, END_PORT + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)

            sock.close()

        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            return

        except socket.gaierror:
            print("Hostname could not be resolved.")
            return

        except Exception:
            # Ignore unexpected errors on individual ports
            continue

    print("\n" + "=" * 40)

    if open_ports:
        print("Open Ports:")
        for port in open_ports:
            print(f" - {port}")
    else:
        print("No open ports found in the scanned range.")

    print("=" * 40)


def main():
    print("Simple Port Scanner")
    print("Scans TCP ports 1-1024")

    while True:
        ip = input("\nEnter an IP address: ").strip()

        if validate_ip(ip):
            break

        print("Invalid IP address. Please try again.")

    scan_ports(ip)


if __name__ == "__main__":
    main()