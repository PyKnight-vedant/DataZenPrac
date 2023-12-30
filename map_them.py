from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd
import numpy as np
import webbrowser
import concurrent.futures
import time
import multiprocessing
from maps_scraper import scraper

Category = input("Enter the category/sector: ")
City = input("Enter the city name: ")
keyword = Category+" in "+City
urls = []
url = "https://www.google.com/maps/@18.4760628,73.9007086,15z?entry=ttu"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
wait = WebDriverWait(browser, 3)
Place = browser.find_element(
    By.CLASS_NAME, "searchboxinput.searchboxinput.xiQnY")
Place.send_keys(keyword)
Place.send_keys(Keys.ENTER)


title, address, phone_no, lat_long = scraper(url)

print("Title: "+title)
print("Address: "+address)
print("Phone Number: "+phone_no)
print("Latitude & Longitude: " + lat_long)
