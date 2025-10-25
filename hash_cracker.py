#!/usr/bin/env python3
import hashlib
import argparse

def identify_hash(hash_string):
    hash_length = len(hash_string)
    if hash_length == 32:
        return "MD5"
    elif hash_length == 40:
        return "SHA1"
    elif hash_length == 64:
        return "SHA256"
    elif hash_length == 128:
        return "SHA512"
    else:
        return "Unknown"

def crack_hash(hash_string, wordlist, hash_type):
    try:
        with open(wordlist, "r", encoding="latin-1") as f:
            for word in f:
                word = word.strip()
                if hash_type == "MD5":
                    guess = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == "SHA1":
                    guess = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == "SHA256":
                    guess = hashlib.sha256(word.encode()).hexdigest()
                elif hash_type == "SHA512":
                    guess = hashlib.sha512(word.encode()).hexdigest()
                else:
                    return None

                if guess == hash_string:
                    return word
    except FileNotFoundError:
        print("[!] Wordlist file not found!")
        return None

    return None

def banner():
    print(r"""
   _   _           _             ____                _
  | | | | __ _ ___| |__         / ___|_ __ __ _  ___| | _____ _ __
  | |_| |/ _` / __| '_ \       |  |  | '__/ _` |/ __| |/ / _ \ '__|
  |  _  | (_| \__ \ | | |      |  |__| | | (_| | (__|   <  __/ |
  |_| |_|\__,_|___/_| |_|  ___  \____|_|  \__,_|\___|_|\_\___|_|

          Hash Cracker 
         Created by - https://github.com/prabhsecure    """)

def main():
    banner()

    # Ask interactively if no arguments are provided
    parser = argparse.ArgumentParser(description="Hash Identifier & Cracker")
    parser.add_argument("-H", "--hash", help="Hash value to crack")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file")
    args = parser.parse_args()

    # If args not given → ask user
    if not args.hash:
        args.hash = input("Enter the hash: ")
    if not args.wordlist:
        args.wordlist = input("Enter the path to the wordlist file: ")

    hash_type = identify_hash(args.hash)
    print(f"[*] Detected hash type: {hash_type}")

    if hash_type == "Unknown":
        print("[!] Unsupported hash type.")
        return

    print(f"[*] Starting crack with wordlist: {args.wordlist}")
    result = crack_hash(args.hash, args.wordlist, hash_type)

    if result:
        print(f"[+] Hash cracked! Plaintext: {result}")
    else:
        print("[-] No match found in wordlist.")

if __name__ == "__main__":
    main()
