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
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
browser = webdriver.Chrome(options=options)

url = "https://www.naukri.com/companies-in-chennai-l183?pageNo=1"

browser.get(url)
names = browser.find_elements(By.CLASS_NAME, "freeTuple")
count = 1
for ele in names:
    print(count, end="===============\n")
    print(ele.text)
    count += 1

browser.quit()
