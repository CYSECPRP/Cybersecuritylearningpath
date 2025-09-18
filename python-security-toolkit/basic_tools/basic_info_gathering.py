Your First Security Programming Language!
Python Installation & Setup:
bash# On Kali (already installed, but verify)
python3 --version
pip3 --version

# Install additional security libraries
sudo pip3 install requests beautifulsoup4 scapy

# Create your Python security toolkit directory
mkdir ~/python-security-toolkit
cd ~/python-security-toolkit
Python Basics with Security Focus:
Lesson 1: Variables & Input/Output
python#!/usr/bin/env python3
# File: basic_info_gathering.py

print("=== Basic Information Gathering Tool ===")

# Variables - storing data
target_ip = input("Enter target IP address: ")
scan_type = input("Enter scan type (basic/advanced): ")
analyst_name = input("Enter your analyst name: ")

# String manipulation
target_ip = target_ip.strip()  # Remove whitespace
scan_type = scan_type.lower()  # Convert to lowercase

# Output formatting
print(f"\n--- Scan Report ---")
print(f"Analyst: {analyst_name}")
print(f"Target: {target_ip}")
print(f"Scan Type: {scan_type.upper()}")
print(f"Timestamp: {__import__('datetime').datetime.now()}")
Lesson 2: Data Types & Lists
python#!/usr/bin/env python3
# File: port_list_manager.py

# Common ports for security scanning
common_ports = [22, 23, 53, 80, 110, 443, 993, 995]
web_ports = [80, 443, 8080, 8443]
admin_ports = [22, 23, 3389, 5900]

# List operations
print("Common ports to scan:")
for port in common_ports:
    print(f"Port {port}")

# Adding new ports
new_port = int(input("\nAdd a custom port: "))
common_ports.append(new_port)
print(f"Updated port list: {common_ports}")

# Checking if port exists
check_port = int(input("Check if port exists: "))
if check_port in common_ports:
    print(f"✅ Port {check_port} is in our scan list")
else:
    print(f"❌ Port {check_port} not found")
Practice Exercise:
Create password_checker_v1.py:
python#!/usr/bin/env python3
# Your first security tool!

password = input("Enter password to check: ")
length = len(password)

print(f"\n=== Password Analysis ===")
print(f"Length: {length} characters")

# Basic checks
if length >= 12:
    print("✅ Length: Strong")
elif length >= 8:
    print("⚠️ Length: Moderate") 
else:
    print("❌ Length: Weak")

# Check for numbers
has_numbers = any(char.isdigit() for char in password)
print(f"Contains numbers: {'✅' if has_numbers else '❌'}")

# Check for uppercase
has_upper = any(char.isupper() for char in password)
print(f"Contains uppercase: {'✅' if has_upper else '❌'}")
