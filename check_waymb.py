import requests
import json

CLIENT_ID = "modderstore_c18577a3"
CLIENT_SECRET = "850304b9-8f36-4b3d-880f-36ed75514cc7"
ACCOUNT_EMAIL = "modderstore@gmail.com"

url = "https://api.waymb.com/transactions/create"

payload = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "account_email": ACCOUNT_EMAIL,
    "amount": 9.00,
    "method": "mbway",
    "currency": "EUR",
    "payer": {
        "name": "Test Script",
        "document": "123456789",
        "phone": "910000000"
    }
}

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://worten.pt/',
    'Origin': 'https://worten.pt'
}

print(f"Sending payload to {url}...")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
