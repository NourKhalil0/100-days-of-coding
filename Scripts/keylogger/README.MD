# Python Keylogger 
![]()

## Description

This project shows how to build a simple keylogger using Python and the pynput library.  
The script logs every key pressed and saves it to a text file (keylogger.txt).  
It is made for educational use only to learn how keylogging works in a safe test environment.

---

## Functionality

The script does the following:

1. **Start Logging**  
   - Begins listening for key presses when the script runs.

2. **Record Keystrokes**  
   - All key presses are written to a file called `keylogger.txt`.

3. **Handles Special Keys**  
   - Special keys like Enter, Shift, etc. are handled correctly.

4. **Cross platform**  
   - Works on macOS, Windows, and Linux (with permissions).

---

## Requirements

- Python 3.x
- pynput library

To install pynput, run:
````bash
  pip install pynput
````
___

---

## ⚠️ Disclaimer

This script captures keyboard input and should **only** be used for:
- Personal learning
- Ethical hacking labs
- Virtual machine testing

> **Note**: Never use this script on systems you do not own or have permission to test.
Using it illegally can result in legal action.

---

## How to Use

1. On macOS:  
   - Go to System Settings → Privacy & Security → Input Monitoring  
   - Allow access to Terminal or your Python IDE

2. Run the script:
````bash 
python3 keylogger.py 
````


