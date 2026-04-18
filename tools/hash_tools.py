"""
🛡️ CIPHER-X Hash Tools
Hashing utilities for data integrity and security learning
"""
import hashlib
import hmac
from typing import Dict, Optional

def hash_md5(data: str) -> str:
    """Generate MD5 hash"""
    return hashlib.md5(data.encode()).hexdigest()

def hash_sha256(data: str) -> str:
    """Generate SHA-256 hash"""
    return hashlib.sha256(data.encode()).hexdigest()

def hash_sha512(data: str) -> str:
    """Generate SHA-512 hash"""
    return hashlib.sha512(data.encode()).hexdigest()

def hash_bcrypt(data: str) -> str:
    """Generate bcrypt hash (requires bcrypt library)"""
    try:
        import bcrypt
        return bcrypt.hashpw(data.encode(), bcrypt.gensalt()).decode()
    except ImportError:
        return hash_sha256(data)

def verify_hash(data: str, expected_hash: str, algorithm: str = "sha256") -> bool:
    """Verify data against a hash"""
    hash_funcs = {
        "md5": hash_md5,
        "sha256": hash_sha256,
        "sha512": hash_sha512
    }
    hash_func = hash_funcs.get(algorithm.lower(), hash_sha256)
    return hmac.compare_digest(hash_func(data), expected_hash.lower())

def generate_hmac(data: str, key: str, algorithm: str = "sha256") -> str:
    """Generate HMAC for message authentication"""
    if algorithm == "sha256":
        return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()
    elif algorithm == "sha512":
        return hmac.new(key.encode(), data.encode(), hashlib.sha512).hexdigest()
    return hmac.new(key.encode(), data.encode(), hashlib.md5).hexdigest()

def quick_hash(data: str) -> Dict:
    """Get multiple hashes of data"""
    return {
        "md5": hash_md5(data),
        "sha256": hash_sha256(data),
        "sha512": hash_sha512(data)
    }
