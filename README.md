# 🔑 Hash Cracker

A lightweight Python tool to **identify and crack common hash types** (MD5, SHA1, SHA256, SHA512) using a wordlist.  
This project is designed for **educational and research purposes** in cybersecurity and digital forensics.

---

## 📌 Features
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
git clone https://github.com/10ayy/hash-cracker.git
cd hash-cracker
chmod +x hashcracker.py
python3 hashcracker.py --help
```

---

## ⚡ Usage

Basic command:
```bash
python3 hashcracker.py -H <hash> -w <wordlist>
```
OR
```bash
python3 hashcracker.py
Enter the hash: <hash>
Enter the path to the wordlist file: </path/to/wordlist>
```

Example:

```bash
python3 hashcracker.py -H 5d41402abc4b2a76b9719d911017c592 -w /usr/share/wordlists/rockyou.txt
```
OR
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

## 📂 Project Structure

```
hash-cracker/
├── hashcracker.py      # main tool
├── requirements.txt    # dependencies
├── README.md           # documentation
└── examples/           # demo screenshots
    ├── demo.png
    └── demo1.png
```

---

## 📸 Demo Screenshot

Here’s an example of the tool in action:

![Hash Cracker Demo](examples/demo.png)
![Hash Cracker Demo](examples/demo1.png)

---

## 🛡️ Disclaimer

This tool is intended **for educational and research purposes only.**
Do not use it on systems without **explicit permission.**
The author is not responsible for any misuse.

---

## 📚 Resources

* [Python Docs](https://docs.python.org/3/library/)
* [HashCat](https://hashcat.net/hashcat/)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

