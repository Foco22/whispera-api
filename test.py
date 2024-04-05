import sys
import requests

# Check if an argument was provided
if len(sys.argv) < 2:
    print("Usage: python test.py <hostname_or_ip>")
    sys.exit(1)

hostname_or_ip = sys.argv[1]
url = 'http://{}:8000/api/whisper'.format(hostname_or_ip)

files = {'files': ('audio.mp3', open('audio.mp3', 'rb'), 'audio/mpeg')}

response = requests.post(url, files=files)

print(response.text)
