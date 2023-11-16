#!/bin/bash
which -s brew
if [[ $? != 0 ]] ; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
brew install python
source ~/.bash_profile
export PATH="/usr/local/bin:$PATH"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install requests pystyle urllib3
cd "$(dirname "$0")/data"
python GuinnessViewBot.py
