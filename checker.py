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
import time


browser = webdriver.Chrome()

browser.get("https://www.google.com/maps/@18.4760628,73.9007086,15z?entry=ttu")
wait = WebDriverWait(browser, 25)
Place = wait.until(EC.presence_of_element_located(
    By.CLASS_NAME, "searchboxinput.searchboxinput.xiQnY"))
Place.send_keys("KJ Somaiya College")
Place.send_keys(Keys.ENTER)
time.sleep(10)
browser.quit()
