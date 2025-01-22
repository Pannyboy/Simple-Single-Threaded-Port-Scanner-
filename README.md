# Simple Single-Threaded Port Scanner

A beginner-friendly port scanner implemented in Python. It attempts to connect to a range of TCP ports on a target host to determine which ports are open. This project is for **educational purposes only**.

---

## Features

- Scans a target host (IP or domain) over a specified range of ports (default 1–1024).
- Single-threaded implementation to maintain simplicity.
- Customizable timeout to avoid indefinite blocking on unresponsive ports.
- Command-line interface for easy usage.

---

## How It Works

1. The script creates a socket (`socket.AF_INET`, `socket.SOCK_STREAM`) for each port.  
2. It attempts to connect to the target host on that port with a specified timeout (e.g., 0.5 seconds).  
3. If the connection succeeds, we consider the port **open**. Otherwise, it is **closed** or **filtered**.  
4. Results are printed to the console, listing any open ports discovered.

---

## Requirements

- **Python 3.7+** (The standard library `socket` module is used, so no additional packages are strictly necessary.)
- (Optional) If you want to store or display results in a particular way, you can list those dependencies in `requirements.txt`.

Example `requirements.txt`:
