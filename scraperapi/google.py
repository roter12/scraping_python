import requests

payload = {
   'api_key': '80665dfa245c7555fb4da5a9031db0e1',
   'country': 'us',
   'query': 'top scraping api'
}

response = requests.get(
   'https://api.scraperapi.com/structured/google/search', params=payload)
print(response.text)