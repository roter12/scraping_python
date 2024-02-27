# https://realpython.com/python-web-scraping-practical-introduction/
import re
from urllib.request import urlopen

url = "https://www.edureka.co/blog/web-scraping-with-python/"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags
print(title)
