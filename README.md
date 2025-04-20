# PORT-SACANNER-
Features:  
Scan single or multiple ports on a target IP/domain
Shows open ports with optional banner grabbing
CLI tool, perfect for practice & demos
Clean, no external library dependencies

# 🔎 Basic Port Scanner

A lightweight Python-based port scanner that checks for open ports on a given IP or domain. Includes optional banner grabbing to identify running services.

---

## ⚙️ Features

- Scans TCP ports in a user-defined range
- Detects open ports and attempts banner grabbing
- Fast and simple — perfect nmap-lite clone for learning
- CLI-based usage

---

## 🛠️ Technologies Used

- Python 3
- socket library
- datetime (for scan timing)

---

## 🚀 Usage

```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
python port_scanner.py
