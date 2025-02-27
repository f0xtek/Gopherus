#!/bin/bash

python3 -m venv .venv && source .venv/bin/activate || (echo "Unable to create virtual environent. Exiting."; exit 1)
pip install requests

chmod +x gopherus.py
ln -sf "${PWD}/gopherus.py" /usr/local/bin/gopherus
