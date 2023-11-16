#!/bin/bash

# Detect package manager and install Python
if command -v apt-get > /dev/null; then
    sudo apt-get update
    sudo apt-get install python3
elif command -v yum > /dev/null; then
    sudo yum update
    sudo yum install python3
elif command -v pacman > /dev/null; then
    sudo pacman -Syu
    sudo pacman -S python3
fi

# Install pip and Python packages
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install requests pystyle urllib3

# Add Python to the PATH environment variable if necessary
# This step depends on the specific Linux distribution and Python installation

# Run Python script
cd data && python3 GuinnessViewBot.py
