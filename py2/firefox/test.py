from __future__ import print_function
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://httpstat.us/200")

if "200 OK" in driver.page_source:
    print('Selenium successfully opened with Firefox (under the Xvfb display) and navigated to "https://httpstat.us/200", you\'re all set!')
