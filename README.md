# 🌐 IP-CheckerBeta

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Beta-orange.svg)

**IP-CheckerBeta** is a colorful Python-based tool that allows you to check and validate IP addresses, view network information (LAN & Public IP), get geolocation details of an IP, and even scan open ports on a target.  
It’s designed to be lightweight, interactive, and easy to use directly from the terminal.

---

## ✨ Features
- 🎨 Colorful and banner-style terminal interface (pyfiglet + termcolor).  
- 🌐 Show all LAN IP addresses from available network interfaces.  
- 🔎 Fetch your current Public IP address.  
- ✅ Validate whether a given IP is valid (IPv4/IPv6).  
- 🌍 Get geolocation details of an IP address (country, city, ISP, coordinates, etc.).  
- 📡 Show default gateway information.  
- 🔐 Scan open ports on a given target IP.  
- 🖥️ Cross-platform (Linux, Windows, macOS).  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BJS611/IP-Checker.git
   cd IP-Checker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the program from your terminal:
```bash
python3 ip.py
```

You will see an interactive menu like this:
```
1) Show LAN IP (Interfaces)
2) Show Public IP
3) Validate IP Address
4) Get IP Details
5) Show Default Gateway
6) Scan Ports on IP
0) Exit
```

Choose an option and follow the instructions.  

Example:  
- Selecting **1** will display your LAN interface IPs.  
- Selecting **4** will prompt you to enter an IP address and return geolocation details.  
- Selecting **6** will let you scan open ports on a target IP.  

---

## 📦 Requirements

- Python 3.7+  
- The following Python packages (included in `requirements.txt`):  
  - requests  
  - netifaces  
  - pyfiglet  
  - termcolor  
  - colorama  

Install them with:
```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author
- GitHub: [BJS611](https://github.com/BJS611)  

---

## ⚠️ Disclaimer
This tool is made for **educational and network diagnostic purposes only**.  
Do not use it to scan or track IP addresses without proper authorization.
