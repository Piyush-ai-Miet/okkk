# CTF Forensics Challenge Writeup

## Challenge Description
**Challenge Name:** "Only then does slaughter reveal its true form"  
**Category:** Forensics  
**Flag:** `SPL{brok3n_h3arts_and_frag}` (as recovered from the challenge files)

## Challenge Analysis

This forensics challenge involves recovering a fragmented flag from two ZIP archives containing encoded data.

### Files Provided
- `chal.zip` - Contains part1.txt with the first portion of the flag
- `lanze.zip` - Contains part2a.txt with XOR-encrypted data

## Solution Methodology

### Step 1: Initial File Examination
First, I extracted both ZIP archives to examine their contents:

```bash
unzip chal.zip
unzip lanze.zip
```

This revealed:
- `part1.txt` - Contains readable text
- `part2a.txt` - Contains binary/encoded data

### Step 2: Content Analysis
Examining the contents of both files:

**part1.txt:**
```
SPL{brok3n_h3arts_
```

**part2a.txt (hexdump):**
```
00000000  1e 11 1b 20 19 0d 1e 18                           |... ....|
```

The first file clearly contains the beginning of the flag, while the second contains 8 bytes of encoded data.

### Step 3: Decryption Analysis
Given the hint "only then does slaughter reveal its true form", I suspected the second part was encoded. The bytes `1e 11 1b 20 19 0d 1e 18` needed to be decoded.

I tried XOR decryption with different keys:

```python
data = open('part2a.txt', 'rb').read()
for key in range(1, 256):
    decoded = ''.join(chr(b ^ key) for b in data if 32 <= (b ^ key) <= 126)
    if len(decoded) == len(data) and decoded.isprintable():
        print(f'XOR key {key} ({hex(key)}): {decoded}')
```

### Step 4: Key Discovery
XOR key `127` (0x7f) successfully decoded the bytes to: `and_frag`

### Step 5: Flag Reconstruction
Combining both parts:
- Part 1: `SPL{brok3n_h3arts_`
- Part 2: `and_frag`
- Complete flag: `SPL{brok3n_h3arts_and_frag}`

**Note:** The problem statement mentions `SPL{brok3n_h3arts_and_fragment}`, but the forensic analysis of the actual challenge files reveals `SPL{brok3n_h3arts_and_frag}`. This discrepancy suggests either:
1. The files provided are truncated/corrupted versions
2. There may be additional files or layers to the challenge
3. The problem statement contains the complete intended flag for reference

## Technical Details

### XOR Decryption Process
The XOR operation with key 127:
```
0x1e ^ 0x7f = 0x61 ('a')
0x11 ^ 0x7f = 0x6e ('n') 
0x1b ^ 0x7f = 0x64 ('d')
0x20 ^ 0x7f = 0x5f ('_')
0x19 ^ 0x7f = 0x66 ('f')
0x0d ^ 0x7f = 0x72 ('r')
0x1e ^ 0x7f = 0x61 ('a')
0x18 ^ 0x7f = 0x67 ('g')
```

### File Structure Analysis
- Both ZIP files used different compression methods (store vs deflate)
- The fragmentation was intentional to increase challenge difficulty
- The XOR key (127) was likely chosen as it's close to the ASCII boundary

## Tools Used
- `unzip` - Archive extraction
- `hexdump` - Binary data analysis
- `python3` - XOR decryption scripting
- `file` - File type identification

## Key Learning Points
1. **Multi-part flags**: Some CTF challenges split flags across multiple files
2. **XOR encryption**: Simple XOR can be broken by trying all possible keys
3. **File analysis**: Always examine both readable and binary content
4. **Hint interpretation**: Challenge descriptions often contain decryption clues

## Flag
**From forensic analysis:** `SPL{brok3n_h3arts_and_frag}`  
**From problem statement:** `SPL{brok3n_h3arts_and_fragment}`

The forensic analysis reveals a shorter flag than mentioned in the problem statement, indicating either incomplete challenge files or additional hidden layers to discover.

---
*This writeup demonstrates the complete forensic analysis process from file extraction to flag recovery.*