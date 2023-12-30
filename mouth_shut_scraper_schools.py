from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import numpy as np

url = "https://www.mouthshut.com/Pune-ICSE-Schools-ProID-925732208"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
cards = browser.find_elements(By.CLASS_NAME, "card-body")
links = []
for card in cards:
    link = card.find_element(
        By.TAG_NAME, "a").get_attribute("href")
    print(link)
    links.append(link)
print(links)
c = 1
for link in links:
    print("============================================================")
    try:
        browser.get(link)
        print(c)
        c += 1
        title = browser.find_element(
            By.XPATH, "/html/body/div[2]/form/div[22]/div/div[12]/div[5]/div/div[1]/div[1]/div/div/h1/a").text
        print(title)
        info = browser.find_elements(By.CLASS_NAME, "info-div")

        for i in info:
            print(i.text)

        print()

    except:
        continue
    finally:
        print("============================================================")
