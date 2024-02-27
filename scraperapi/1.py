import requests

payload = { 'api_key': '80665dfa245c7555fb4da5a9031db0e1', 'url': 'https://www.avast.com/random-password-generator#pc' }
r = requests.get('https://api.scraperapi.com/', params=payload)
print(r.text)