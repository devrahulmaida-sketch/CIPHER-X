"""
🛡️ CIPHER-X Port Scanner
Basic port scanning for network reconnaissance (educational purposes)
"""
import socket
from typing import List, Dict
from datetime import datetime

COMMON_PORTS = {
    20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
    8080: "HTTP Proxy", 8443: "HTTPS Alt"
}

def scan_port(host: str, port: int, timeout: float = 1.0) -> Dict:
    """Scan a single port"""
    result = {
        "port": port,
        "host": host,
        "open": False,
        "service": COMMON_PORTS.get(port, "Unknown"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        conn_result = sock.connect_ex((host, port))
        result["open"] = conn_result == 0
        sock.close()
    except (socket.timeout, socket.error, OSError):
        result["open"] = False
    return result

def scan_common_ports(host: str = "127.0.0.1") -> List[Dict]:
    """Scan common ports on a host"""
    results = []
    for port in COMMON_PORTS.keys():
        result = scan_port(host, port)
        if result["open"]:
            results.append(result)
    return results

def scan_port_range(host: str, start: int, end: int, timeout: float = 0.5) -> List[Dict]:
    """Scan a range of ports"""
    results = []
    for port in range(start, min(end + 1, 10000)):
        result = scan_port(host, port, timeout)
        if result["open"]:
            results.append(result)
    return results

def quick_scan(host: str = "127.0.0.1") -> Dict:
    """Perform a quick scan of important ports"""
    important_ports = [21, 22, 23, 25, 80, 443, 445, 3389, 5900, 8080]
    open_ports = []
    for port in important_ports:
        result = scan_port(host, port, timeout=0.3)
        if result["open"]:
            open_ports.append(result)
    return {
        "host": host,
        "scanned_ports": len(important_ports),
        "open_ports": open_ports,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
