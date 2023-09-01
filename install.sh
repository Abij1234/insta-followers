#!/bin/bash
if ! python -c "import requests" &> /dev/null; then
    echo "Installing 'requests'..."
    pip install requests
else
    echo "'requests' is already installed."
fi
if ! python -c "import wget" &> /dev/null; then
    echo "Installing 'wget'..."
    pip install wget
else
    echo "'wget' is already installed."
fi
