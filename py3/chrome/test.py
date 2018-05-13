from selenium import webdriver

options = webdriver.chrome.options.Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://httpstat.us/200")

if "200 OK" in driver.page_source:
    print('Selenium successfully opened with Chrome (under the Xvfb display) and navigated to "https://httpstat.us/200", you\'re all set!')
