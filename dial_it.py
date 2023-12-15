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
import time


browser = webdriver.Chrome()

# Obtain the Google Map URL
url = "https://www.justdial.com"
# "https://www.google.com/maps/place/Indian+Institute+Of+Technology%E2%80%93Madras+(IIT%E2%80%93Madras)/@12.9914929,80.2311104,17z/data=!3m1!4b1!4m6!3m5!1s0x3a5267f29aa9a61f:0x24ef264085e6a094!8m2!3d12.9914929!4d80.2336907!16zL20vMGd5eHdk?entry=ttu"]
# Open the Google Map URL


browser.get(url)
LOC = browser.find_element(
    By.XPATH, "//html/body/div[1]/div/section/header/div/div[2]/div/div[1]/div[1]/div/input")


LOC.send_keys("Chennai")
LOC.send_keys(Keys.ENTER)
Place = browser.find_element(
    By.XPATH, "/html/body/div[1]/div/section/header/div/div[2]/div/div[2]/label/div[1]/input")
word = '''Colleges in Chennai

'''

Place.send_keys("Colleges in Chennai")
time.sleep(1.5)
Button = browser.find_element(
    By.XPATH, "/html/body/div[1]/div/section/header/div/div[2]/div/div[2]/label/div[2]/div")

time.sleep(45)
# Place.send_keys(Keys.ENTER)


# Initialize variables and declare it 0


# Create a loop for obtaining data from URLs


# browser.get(url[i])

# Obtain the title of that place
browser.quit()
