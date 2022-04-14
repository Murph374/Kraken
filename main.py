import time
import requests
import urllib.parse
import hashlib
import hmac
import base64

with open("keys", "r") as f:
    lines = f.read().splitlines()
    api_key = lines[0]
    api_sec = lines[1]

def get_kraken_signature(urlpath, data, secret):