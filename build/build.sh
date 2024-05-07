#!/bin/bash

# Set dir
cd "$(dirname "$0")"

# Define
appName="ChatRPG"

# Clean
rm -rf out

# Build
mkdir out
cd out
pyinstaller --onefile -n $appName --log-level ERROR --add-data=../../.env:. --add-data=../../assets/*:assets/ ../../src/mainUI.py