"""
🛡️ CIPHER-X Security Monitor
Network and system monitoring for cybersecurity awareness
"""
import socket
import psutil
import platform
from datetime import datetime
from typing import Dict, List

def get_system_info() -> Dict:
    """Get comprehensive system information"""
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "hostname": socket.gethostname(),
        "ip_address": get_local_ip(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
        "boot_time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    }

def get_local_ip() -> str:
    """Get local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def get_active_connections() -> List[Dict]:
    """Get all active network connections"""
    connections = []
    try:
        for conn in psutil.net_connections(kind="inet"):
            connections.append({
                "protocol": conn.type.name if hasattr(conn.type, "name") else str(conn.type),
                "local_addr": f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A",
                "remote_addr": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A",
                "status": conn.status,
                "pid": conn.pid
            })
    except (psutil.AccessDenied, PermissionError):
        return [{"error": "Access denied - run as administrator"}]
    return connections[:50]

def get_listening_ports() -> List[Dict]:
    """Get all listening ports"""
    ports = []
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == "LISTEN":
            ports.append({
                "port": conn.laddr.port,
                "address": conn.laddr.ip,
                "protocol": "TCP" if conn.type == socket.SOCK_STREAM else "UDP",
                "pid": conn.pid,
                "process": get_process_name(conn.pid)
            })
    return ports

def get_process_name(pid: int) -> str:
    """Get process name from PID"""
    try:
        return psutil.Process(pid).name()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return "Unknown"

def get_suspicious_processes() -> List[Dict]:
    """Detect potentially suspicious processes"""
    suspicious = []
    high_risk_ports = {22, 23, 25, 445, 3389, 5900, 8080, 8888}
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == "LISTEN" and conn.laddr.port in high_risk_ports:
            try:
                process = psutil.Process(conn.pid)
                suspicious.append({
                    "port": conn.laddr.port,
                    "process": process.name(),
                    "pid": conn.pid,
                    "cpu_percent": process.cpu_percent(),
                    "memory_mb": process.memory_info().rss / 1024 / 1024
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    return suspicious

def quick_security_scan() -> Dict:
    """Perform a quick security assessment"""
    system_info = get_system_info()
    suspicious = get_suspicious_processes()
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "system": system_info,
        "suspicious_ports": suspicious,
        "security_score": calculate_security_score(suspicious)
    }

def calculate_security_score(suspicious: List[Dict]) -> int:
    """Calculate security score (0-100)"""
    score = 100
    score -= len(suspicious) * 10
    return max(0, min(100, score))

def network_status() -> Dict:
    """Get network status"""
    net_io = psutil.net_io_counters()
    return {
        "bytes_sent": net_io.bytes_sent,
        "bytes_recv": net_io.bytes_recv,
        "packets_sent": net_io.packets_sent,
        "packets_recv": net_io.packets_recv
    }
