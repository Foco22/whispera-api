import sys
import requests

# Check if an argument was provided
if len(sys.argv) < 2:
    print("Usage: python test.py <hostname_or_ip>")
    sys.exit(1)

hostname_or_ip = sys.argv[1]
url = 'http://localhost:8000/start'
response = requests.get(url)

print(response.text)
