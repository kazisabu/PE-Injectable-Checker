PE Injectable Checker
PE Injectable Checker is a Python-based static scanner that identifies Windows PE (.exe) files which are likely suitable for shellcode injection or payload stubbing. It performs a non-invasive analysis to help red teamers, malware analysts, and researchers detect potential injection targets with:
```
❌ No digital signature
❌ Not packed (low entropy)
✅ Presence of executable code caves
```
🔍 What It Does
For each .exe in a given directory, it checks:
Digital signature: Skips signed binaries to avoid AV triggers
Entropy levels: Flags packed or encrypted binaries
Code caves: Finds executable regions of null bytes ideal for shell injection
If all conditions match, the PE is marked as Injectable.

pip install pefile
pip install lief

  $ ```python3 PE_Injectable_checker.py```

Enter folder path with EXE files: /path/to/exe/folder

⚠️ Disclaimer
This tool is provided for educational, research, and red teaming purposes only. Use responsibly and never deploy on systems you do not own or have explicit permission to test.
