# https://www.edureka.co/blog/web-scraping-with-python/

# Interact With HTML Forms

import mechanicalsoup # MechanicalSoup

browser = mechanicalsoup.StatefulBrowser()
url = 'http://localhost/bsms_ci/index.php/admin/index'
browser.open(url)

# Fill in the form fields
form = browser.select_form()  # Select the form on the webpage
form['username'] = 'root'  # Replace 'username' with the name attribute of the username input field
form['password'] = 'root'  # Replace 'password' with the name attribute of the password input field

# Submit the form
resp = browser.submit_selected()

page = browser.page
messages = page.find("div", class_="sidebar-header d-flex align-items-center")
if messages:
    print(messages.text)