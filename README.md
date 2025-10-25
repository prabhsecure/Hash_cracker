# Hash_Cracker

Introducing A Lightweight Hashcracker — a Python tool by prabh secure to identify and crack common hash types (MD5, SHA1, SHA256, SHA512) using a wordlist. Designed for educational and research use in cybersecurity and digital forensics.

---

# Features
- ✅ Detects hash type automatically (based on length)  
- ✅ Supports MD5, SHA1, SHA256, and SHA512  
- ✅ Cracks hashes using a given wordlist  
- ✅ Clean and simple CLI interface  

---

## Prerequisites

To use HashCracker, ensure you have the following installed:

- Python: Version 3.7 or higher
- Pip: The Python package installer

---

## 🚀 Installation

Clone this repository:
```bash
https://github.com/prabhsecure/Hash_cracker.git
cd hash_cracker
chmod +x hash_cracker.py
python3 hash_cracker.py

```

---

## ⚡ Usage

Basic command:

python3 hashcracker.py
Enter the hash: <hash>
Enter the path to the wordlist file: </path/to/wordlist>

Example:

```bash
python3 hashcracker.py
Enter the hash: 5d41402abc4b2a76b9719d911017c592
Enter the path to the wordlist file: /usr/share/wordlists/rockyou.txt
```

Output:

```
[*] Detected hash type: MD5
[*] Starting crack with wordlist: /usr/share/wordlists/rockyou.txt
[+] Hash cracked! Plaintext: hello
```

---

## 🛡️ Disclaimer

This tool is intended **for educational and research purposes only.**
Do not use it on systems without **explicit permission.**
The author is not responsible for any misuse.

---


