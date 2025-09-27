# Forensics Challenge Summary

## Challenge Files Analysis

### File Structure
```
okkk/
├── chal.zip (170 bytes) → part1.txt
├── lanze.zip (128 bytes) → part2a.txt
├── part1.txt (18 bytes) → "SPL{brok3n_h3arts_"
└── part2a.txt (8 bytes) → XOR encrypted data
```

### Key Findings
- **part1.txt**: Contains flag prefix `SPL{brok3n_h3arts_`
- **part2a.txt**: Contains 8 bytes XOR-encrypted with key 127 (0x7f)
- **Decrypted data**: `and_frag`
- **Reconstructed flag**: `SPL{brok3n_h3arts_and_frag}`

### XOR Decryption Details
```
Encrypted: [0x1e, 0x11, 0x1b, 0x20, 0x19, 0x0d, 0x1e, 0x18]
XOR Key: 127 (0x7f)
Decrypted: "and_frag"
```

### Challenge Hint
"Only then does slaughter reveal its true form" - likely refers to the XOR decryption process revealing the hidden text.

### Tools Used
- `unzip` - Archive extraction
- `hexdump` - Binary analysis  
- `python3` - XOR brute force
- `strings` - Text extraction

### Flag Verification
- **Recovered from files**: `SPL{brok3n_h3arts_and_frag}`
- **Problem statement**: `SPL{brok3n_h3arts_and_fragment}`
- **Status**: Partial match - files may be incomplete or additional layers exist