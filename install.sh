#!/bin/bash

# Install Python and pip if they aren't already installed
command -v python3 &>/dev/null || { echo >&2 "Python 3 is not installed.  Aborting."; exit 1; }
command -v pip3 &>/dev/null || { echo >&2 "pip for Python 3 is not installed.  Aborting."; exit 1; }

# Install any necessary Python packages
pip3 install nltk scikit-learn

# Move the script, text file and json to /usr/local/bin
sudo cp linuxsearch.py /usr/local/bin/linuxsearch
sudo cp linuxmanual.py /usr/local/bin/linuxmanual
sudo cp commands.txt /usr/local/bin/commands.txt
sudo cp commands.json /usr/local/bin/commands.json
sudo cp commands2.txt /usr/local/bin/commands2.txt

# Make the script executable
sudo chmod +x /usr/local/bin/manual
sudo chmod +x /usr/local/bin/search
echo "Installation completed. You can now run the scripts in the terminal. Type 'manual' For a menu-based manual, or 'search' and then a description of the command you're looking for, or the command itself."
