# 🛡️ CIPHER-X

### Your Personal Digital Guardian — Advanced AI Assistant with Cybersecurity Toolkit

[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Stars](https://img.shields.io/github/stars/devrahulmaida-sketch/CIPHER-X?style=for-the-badge)](https://github.com/devrahulmaida-sketch/CIPHER-X/stargazers)
[![Forks](https://img.shields.io/github/forks/devrahulmaida-sketch/CIPHER-X?style=for-the-badge)](https://github.com/devrahulmaida-sketch/CIPHER-X/network/members)

---

## 🤖 What is CIPHER-X?

**CIPHER-X** is an advanced voice-driven AI assistant with an integrated cybersecurity toolkit. Like a digital guardian, it hears, understands, responds, and executes tasks across your system — while providing security tools for ethical hacking and cybersecurity learning.

> *"In a world of digital threats, CIPHER-X is your first line of defense."*

---

## ✨ Features

### 🗣️ Voice AI Assistant (Powered by Gemini)
| Feature | Description |
|---------|-------------|
| **Real-time Voice Interaction** | Natural conversation with instant response |
| **System Control** | Launch apps, manage files, execute commands |
| **Visual Awareness** | Screen and webcam understanding |
| **Persistent Memory** | Learns preferences across sessions |

### 🛡️ Cybersecurity Toolkit
| Tool | Description |
|------|-------------|
| **Security Monitor** | System info, network connections, port monitoring |
| **Port Scanner** | Scan local ports for security assessment |
| **Audit Logger** | Track system events and security incidents |
| **Password Generator** | Generate secure passwords |
| **Hash Tools** | MD5, SHA256, SHA512 hashing utilities |
| **Encode/Decode** | Base64, Hex, Caesar, ROT13 encoding |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/devrahulmaida-sketch/CIPHER-X.git
cd CIPHER-X

# Install dependencies
pip install -r requirements.txt
playwright install

# Launch CIPHER-X
python main.py
```

---

## 📁 Project Structure

```
CIPHER-X/
├── security/              # Cybersecurity modules
│   ├── __init__.py
│   ├── security_monitor.py   # System & network monitoring
│   ├── port_scanner.py       # Port scanning utilities
│   └── audit_logger.py       # Security event logging
├── tools/                 # Security tools
│   ├── __init__.py
│   ├── password_gen.py       # Password generation & strength
│   ├── hash_tools.py        # Hashing utilities
│   └── encode_decode.py     # Encoding/decoding tools
├── actions/               # AI assistant actions
├── agent/                 # AI agent modules
├── memory/                # Memory management
├── core/                  # Core AI prompts
├── main.py                # Main entry point
└── ui.py                  # User interface
```

---

## 🛠️ Cybersecurity Tools Usage

```python
# Security Monitor
from security import get_system_info, quick_security_scan
sys_info = get_system_info()
print(sys_info)

# Port Scanner
from security import quick_scan
result = quick_scan("127.0.0.1")
print(result)

# Password Generator
from tools import generate_password, check_password_strength
password = generate_password(16)
strength = check_password_strength(password)

# Hash Tools
from tools import hash_sha256, verify_hash
hashed = hash_sha256("mypassword")
is_valid = verify_hash("mypassword", hashed)
```

---

## 📋 Requirements

| Requirement | Details |
|------------|---------|
| OS | Windows 10/11 |
| Python | 3.11 or 3.12 |
| Microphone | Required for voice features |
| API Key | Free [Gemini API Key](https://aistudio.google.com/apikey) |

---

## ⚠️ License & Ethics

Licensed under **MIT License**

⚠️ **FOR EDUCATIONAL AND ETHICAL USE ONLY** ⚠️

This software includes cybersecurity tools for learning and ethical security testing purposes only. Unauthorized scanning or testing of systems you do not own or have explicit permission to test is illegal and prohibited.

---

## 👨‍💻 Author

**Rahul Maida** - [@devrahulmaida-sketch](https://github.com/devrahulmaida-sketch)

- 11th Grade Student | JEE Aspirant | Future White Hat Hacker

---

## 🙏 Acknowledgments

Based on [Mark-XXXV](https://github.com/FatihMakes/Mark-XXXV) by [@FatihMakes](https://github.com/FatihMakes) - The original JARVIS-style AI assistant

---

⭐ **Star this repository** if you find it useful!

*"The quieter you become, the more you can hear."* 🕵️‍♂️
