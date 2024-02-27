# https://www.edureka.co/blog/web-scraping-with-python/

# Use requests for get html

import requests
from bs4 import BeautifulSoup # beautifulsoup4
import pandas as pd

# Get html content
url = 'https://www.edureka.co/blog/web-scraping-with-python/'
response = requests.get(url)
if response.status_code == 200:
    html = response.content
else:
    print("Failed to fetch the website.")
    exit()

soup = BeautifulSoup(html, "html.parser")
for f in soup.findAll('div', attrs={'class':'container'}):
    print(f.text)
    
    
#     headers = {
#     'authority': 'www.kith.com',
#     'cache-control': 'max-age=0',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
#     'sec-fetch-dest': 'document',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'accept-language': 'en-US,en;q=0.9',
# }

# session = requests.session()

# response = session.get("https://kith.com/collections/mens-footwear", headers=headers)