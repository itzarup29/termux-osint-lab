#!/bin/bash
echo "[*] Updating Termux packages..."
pkg update && pkg upgrade -y

echo "[*] Installing Python and Git..."
pkg install python git -y

echo "[*] Installing required Python modules..."
pip install requests beautifulsoup4

echo "[*] Setup complete!"
