# script to open and close browser

import selenium
from selenium import webdriver
browser=webdriver.Firefox()
browser.get("http://google.com")
browser.close()
