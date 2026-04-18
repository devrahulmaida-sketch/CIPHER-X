"""
🛡️ CIPHER-X Audit Logger
Security audit logging for tracking system events
"""
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class SecurityAuditLogger:
    def __init__(self, log_dir: str = None):
        if log_dir is None:
            base_dir = Path(__file__).resolve().parent.parent
            log_dir = base_dir / "logs"
        else:
            log_dir = Path(log_dir)
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.current_log = self.log_dir / f"audit_{datetime.now().strftime('%Y%m%d')}.json"
    
    def log_event(self, event_type: str, severity: str, description: str, metadata: Dict = None) -> None:
        """Log a security event"""
        event = {
            "timestamp": datetime.now().isoformat(),
            "type": event_type,
            "severity": severity,
            "description": description,
            "metadata": metadata or {}
        }
        try:
            existing = []
            if self.current_log.exists():
                with open(self.current_log, 'r') as f:
                    existing = json.load(f)
            existing.append(event)
            with open(self.current_log, 'w') as f:
                json.dump(existing, f, indent=2)
        except Exception as e:
            print(f"[Audit] Failed to write log: {e}")
    
    def get_recent_events(self, count: int = 10, severity: str = None) -> List[Dict]:
        """Get recent audit events"""
        if not self.current_log.exists():
            return []
        try:
            with open(self.current_log, 'r') as f:
                events = json.load(f)
            if severity:
                events = [e for e in events if e.get('severity') == severity]
            return events[-count:]
        except Exception:
            return []
    
    def get_security_summary(self) -> Dict:
        """Get security summary for today"""
        if not self.current_log.exists():
            return {"total_events": 0, "by_severity": {}}
        try:
            with open(self.current_log, 'r') as f:
                events = json.load(f)
            by_severity = {}
            for event in events:
                sev = event.get('severity', 'unknown')
                by_severity[sev] = by_severity.get(sev, 0) + 1
            return {
                "total_events": len(events),
                "by_severity": by_severity,
                "last_event": events[-1] if events else None
            }
        except Exception:
            return {"total_events": 0, "by_severity": {}}

def log_login_attempt(username: str, success: bool, ip_address: str = None) -> None:
    """Log a login attempt"""
    logger = SecurityAuditLogger()
    logger.log_event(
        event_type="LOGIN_ATTEMPT",
        severity="WARNING" if not success else "INFO",
        description=f"Login {'successful' if success else 'failed'} for user: {username}",
        metadata={"username": username, "success": success, "ip": ip_address}
    )

def log_file_access(file_path: str, action: str) -> None:
    """Log file access"""
    logger = SecurityAuditLogger()
    logger.log_event(
        event_type="FILE_ACCESS",
        severity="INFO",
        description=f"File {action}: {file_path}",
        metadata={"file_path": file_path, "action": action}
    )

def log_network_activity(action: str, details: Dict) -> None:
    """Log network activity"""
    logger = SecurityAuditLogger()
    logger.log_event(
        event_type="NETWORK_ACTIVITY",
        severity="INFO",
        description=f"Network {action}",
        metadata=details
    )

def log_system_change(action: str, target: str, details: Dict = None) -> None:
    """Log system changes"""
    logger = SecurityAuditLogger()
    logger.log_event(
        event_type="SYSTEM_CHANGE",
        severity="WARNING",
        description=f"System {action}: {target}",
        metadata=details or {}
    )
