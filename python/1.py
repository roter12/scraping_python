# https://www.edureka.co/blog/web-scraping-with-python/

# Use webdriver for get html

from selenium import webdriver
from bs4 import BeautifulSoup # beautifulsoup4
import pandas as pd

# Get html content
url = 'https://www.bestrandoms.com/random-address-in-de?quantity=6'
driver = webdriver.Chrome() # "/usr/lib/chromium-browser/chromedriver"
driver.get(url)
html = driver.page_source

# Parse html content
street = []
city = []
phone = []
soup = BeautifulSoup(html, "html.parser")
for f in soup.findAll('li', attrs={'class':'col-sm-6'}): # soup.select('a.e1dscegp1')
    i = f.findAll('span')
    if (len(i) != 7):
        continue
    street.append(i[0].b.next_sibling.text.strip())
    city.append(i[1].b.next_sibling.text.strip())
    phone.append(i[3].b.next_sibling.text.strip())

# Save parsed value
df = pd.DataFrame({'Street': street, 'City': city, 'Phone': phone}) 
# df.to_csv('1-out.csv', index=False, encoding='utf-8')
print(df)




# https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-2/

# from selenium import webdriver
# from bs4 import BeautifulSoup
 
# option = webdriver.ChromeOptions()
# # I use the following options as my machine is a window subsystem linux. 
# # I recommend to use the headless option at least, out of the 3
# option.add_argument('--headless')
# option.add_argument('--no-sandbox')
# option.add_argument('--disable-dev-sh-usage')
# # Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
# driver = webdriver.Chrome('YOUR-PATH-TO-CHROMEDRIVER', options=option)

# driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
# soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup. Notice driver.page_source instead of page.content
 
# links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
# first10 = links[:10] # Keep only the first 10 anchors
# for anchor in first10:
#     print(anchor.text) # Display the innerText of each anchor


# first_link = driver.find_elements_by_css_selector('table tbody tr td.titleColumn a')[0]
# first_link.click()

# driver.save_screenshot(‘screenshot-file-name.png’)

# How to Extract Dynamically Loaded Content
#  WebDriverWait(driver, 5).until(EC.visibility_of_elemen


# 1. Time your requests
# 2. Error handling