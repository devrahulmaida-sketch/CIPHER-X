"""
🛡️ CIPHER-X Password Generator
Generate secure passwords for security awareness
"""
import random
import string
from typing import Dict, List

def generate_password(length: int = 16, include_special: bool = True) -> str:
    """Generate a secure random password"""
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_passphrase(word_count: int = 4, separator: str = "-") -> str:
    """Generate a memorable passphrase"""
    words = [
        "cyber", "shield", "vault", "cipher", "secure", "defend", "protect",
        "guard", "fortress", "binary", "firewall", "token", "encrypt", "decode",
        "quantum", "neural", "vector", "matrix", "shadow", "stealth"
    ]
    return separator.join(random.choice(words) for _ in range(word_count))

def check_password_strength(password: str) -> Dict:
    """Check password strength"""
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    elif len(password) >= 12:
        score += 2
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    strength = {1: "Weak", 2: "Fair", 3: "Good", 4: "Strong", 5: "Very Strong"}.get(score, "Weak")
    
    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

def suggest_improvements(password: str) -> List[str]:
    """Suggest improvements for password"""
    suggestions = []
    if len(password) < 12:
        suggestions.append("Use at least 12 characters")
    if password.isalnum():
        suggestions.append("Add special characters (!@#$%)")
    if password.isalpha():
        suggestions.append("Add numbers")
    common = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in common:
        suggestions.append("Avoid common passwords")
    return suggestions
