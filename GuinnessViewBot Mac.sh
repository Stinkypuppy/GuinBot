#!/bin/bash
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
if ! command -v python3 &> /dev/null
then
    echo "Python not found. Installing Python..."
    brew install python3
fi
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
cd "$(dirname "$0")/data"
python3 GuinnessViewBot.py
