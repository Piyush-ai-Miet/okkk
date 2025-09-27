#!/usr/bin/env python3
"""
CTF Forensics Challenge Solution Script
Challenge: "Only then does slaughter reveal its true form"
"""

import zipfile
import os

def extract_and_analyze():
    """Extract ZIP files and analyze contents"""
    print("=== CTF Forensics Challenge Solver ===")
    print("Challenge: 'Only then does slaughter reveal its true form'\n")
    
    # Extract ZIP files if they exist
    if os.path.exists('chal.zip'):
        with zipfile.ZipFile('chal.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
            print("✓ Extracted chal.zip")
    
    if os.path.exists('lanze.zip'):
        with zipfile.ZipFile('lanze.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
            print("✓ Extracted lanze.zip")
    
    # Read part1.txt
    if os.path.exists('part1.txt'):
        with open('part1.txt', 'r') as f:
            part1 = f.read().strip()
            print(f"\nPart 1 (part1.txt): {part1}")
    else:
        print("❌ part1.txt not found")
        return
    
    # Read and decode part2a.txt
    if os.path.exists('part2a.txt'):
        with open('part2a.txt', 'rb') as f:
            encrypted_data = f.read()
            print(f"Part 2 (part2a.txt) raw bytes: {[hex(b) for b in encrypted_data]}")
            
            # Try XOR decryption with different keys
            print("\nTrying XOR decryption...")
            for key in range(1, 256):
                decoded = ''.join(chr(b ^ key) for b in encrypted_data if 32 <= (b ^ key) <= 126)
                if len(decoded) == len(encrypted_data) and decoded.isprintable():
                    print(f"XOR key {key} (0x{key:02x}): {decoded}")
                    if key == 127:  # The correct key
                        part2 = decoded
                        print(f"✓ Found correct decryption with key {key}: {part2}")
    else:
        print("❌ part2a.txt not found")
        return
    
    # Combine parts to get the flag
    flag = part1 + part2 + '}'
    print(f"\n🏁 Complete Flag: {flag}")
    
    # Verify against expected flag
    expected_flag = "SPL{brok3n_h3arts_and_fragment}"
    if flag == expected_flag:
        print("✅ Flag verification successful!")
    else:
        print(f"❌ Flag mismatch. Expected: {expected_flag}")
    
    return flag

def demonstrate_xor_process():
    """Demonstrate the XOR decryption process step by step"""
    print("\n=== XOR Decryption Process ===")
    encrypted_bytes = [0x1e, 0x11, 0x1b, 0x20, 0x19, 0x0d, 0x1e, 0x18]
    key = 127  # 0x7f
    
    print(f"Encrypted bytes: {[hex(b) for b in encrypted_bytes]}")
    print(f"XOR key: {key} (0x{key:02x})")
    print("\nDecryption process:")
    
    decoded_chars = []
    for i, byte in enumerate(encrypted_bytes):
        decrypted = byte ^ key
        char = chr(decrypted)
        decoded_chars.append(char)
        print(f"  {hex(byte)} ^ 0x{key:02x} = {hex(decrypted)} ('{char}')")
    
    decoded_text = ''.join(decoded_chars)
    print(f"\nDecoded text: '{decoded_text}'")

if __name__ == "__main__":
    flag = extract_and_analyze()
    demonstrate_xor_process()
    print(f"\n🎯 Final Answer: {flag}")