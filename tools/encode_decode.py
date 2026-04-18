"""
🛡️ CIPHER-X Encoding/Decoding Tools
Encode/Decode utilities for security learning
"""
import base64
import codecs
from typing import Dict, Optional

def encode_base64(data: str) -> str:
    """Encode string to Base64"""
    return base64.b64encode(data.encode()).decode()

def decode_base64(data: str) -> Optional[str]:
    """Decode Base64 string"""
    try:
        return base64.b64decode(data.encode()).decode()
    except Exception:
        return None

def encode_hex(data: str) -> str:
    """Encode string to Hexadecimal"""
    return data.encode().hex()

def decode_hex(data: str) -> Optional[str]:
    """Decode Hexadecimal string"""
    try:
        return bytes.fromhex(data).decode()
    except Exception:
        return None

def encode_rot13(data: str) -> str:
    """Encode string using ROT13"""
    return codecs.encode(data, 'rot_13')

def encode_caesar(data: str, shift: int = 3) -> str:
    """Encode string using Caesar cipher"""
    result = []
    for char in data:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift_amount + shift) % 26 + shift_amount))
        else:
            result.append(char)
    return ''.join(result)

def decode_caesar(data: str, shift: int = 3) -> str:
    """Decode Caesar cipher"""
    return encode_caesar(data, -shift)

def quick_encode(data: str) -> Dict:
    """Get multiple encodings of data"""
    return {
        "base64": encode_base64(data),
        "hex": encode_hex(data),
        "rot13": encode_rot13(data),
        "caesar": encode_caesar(data)
    }

def quick_decode(data: str, encoding_type: str = "base64") -> Optional[str]:
    """Decode encoded string"""
    decoders = {
        "base64": decode_base64,
        "hex": decode_hex,
        "rot13": lambda d: codecs.decode(d, 'rot_13'),
        "caesar": lambda d: decode_caesar(d)
    }
    decoder = decoders.get(encoding_type.lower())
    return decoder(data) if decoder else None
