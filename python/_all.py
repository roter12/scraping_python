import os
import sys
import datetime
import requests
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup # beautifulsoup4
from urllib.request import urlopen


# Get html content
def get_html_with_selenium(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver.page_source


def get_html_with_request(url):
	response = requests.get(url)
	if response.status_code == 200:
	    html = response.content
	else:
		html = str(response.status_code)
	return html


def get_html_with_urllib(url):
	page = urlopen(url)
	return page.read().decode("utf-8")


# Save as a file
def save_file(text, filename = 'test.tmp'):
	if type(text) != 'str':
		text = str(text)
	file = open(filename, "w", encoding="utf-8")
	file.write(text)
	file.close()


# Read file
def read_file(filename = 'test.tmp'):
    file = open(filename, "r", encoding="utf-8")
    text = file.read()
    file.close()
    return text


# Create the output directory,
output_dir = os.path.join('.',  'output')
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

try:
    output_dir = os.path.join(output_dir, timestamp)
    os.mkdir(output_dir)
except Exception as e:
    print('Error: ' + str(e))
    print('Failed to create output directory. Aborting all sends.')
    sys.exit(1)

# Main entry
idx = 1
while True:
	url = input("Enter url: ")
	url = url.strip()
	if url == '':
		exit(0)

	html = get_html_with_selenium(url)
	filename = os.path.join(output_dir, f"selenium ({idx}).htm")
	save_file(html, filename)
	print(f"Saved : {filename}")

	html = get_html_with_request(url)
	filename = os.path.join(output_dir, f"request ({idx}).htm")
	save_file(html, filename)
	print(f"Saved : {filename}")

	# html = get_html_with_urllib(url)
	# filename = os.path.join(output_dir, f"urllib ({idx}).htm")
	# save_file(html, filename)
	# print(f"Saved : {filename}")

	idx += 1