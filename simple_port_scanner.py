import socket

def scan_port(target_host: str, port: int, timeout: float = 0.5) -> bool:
    """
    Tries to connect to a specified port on a target host.

    :param target_host: The IP address or hostname to scan
    :param port: The port to test
    :param timeout: Connection timeout in seconds
    :return: True if the port is open, False otherwise
    """
    try:
        # Create a socket object with IPv4 and TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set the timeout so the script doesn't hang
        sock.settimeout(timeout)
        # Attempt to connect; if successful, the port is open
        sock.connect((target_host, port))
        # Cleanly close the socket
        sock.close()
        return True
    except (socket.timeout, socket.error):
        return False

def scan_ports_on_host(target_host: str, start_port: int, end_port: int):
    print(f"Scanning host: {target_host}")
    print(f"Port range: {start_port}-{end_port}")
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target_host, port):
            open_ports.append(port)

    if open_ports:
        print(f"Open ports on {target_host}: {open_ports}")
    else:
        print(f"No open ports found in the given range on {target_host}")

import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target host to scan (e.g., 192.168.1.10)")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    # Perform the scan
    scan_ports_on_host(args.host, args.start, args.end)

if __name__ == "__main__":
    main()
