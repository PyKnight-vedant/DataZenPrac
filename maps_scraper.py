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


def scraper(url):

    # Obtain the Google Map URL
    # url = "https://www.google.com/maps/@18.4760628,73.9007086,15z?entry=ttu"
    # "https://www.google.com/maps/place/Indian+Institute+Of+Technology%E2%80%93Madras+(IIT%E2%80%93Madras)/@12.9914929,80.2311104,17z/data=!3m1!4b1!4m6!3m5!1s0x3a5267f29aa9a61f:0x24ef264085e6a094!8m2!3d12.9914929!4d80.2336907!16zL20vMGd5eHdk?entry=ttu"]
    # Open the Google Map URL

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incognito')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    wait = WebDriverWait(browser, 3)
    time.sleep(3.5)
    current_url = browser.current_url
    # print("Current URL:", current_url)
    url_regex = re.compile("@\d+.\d+,\d+.\d+")
    lat_long = url_regex.findall(current_url)[0][1:]

    title = wait.until(EC.presence_of_element_located(
        (By.XPATH,  "/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1"))).text

    address = browser.find_element(By.CLASS_NAME, "CsEnBe")
    address = address.text

    phone_no = wait.until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "Io6YTe.fontBodyMedium.kR99db")))

    for ele in phone_no:
        phone_regex = re.compile("\d+\s*\d+\s*\d+")
        phone = phone_regex.findall(ele.text)
        if len(phone) > 0:
            if len(phone[0]) >= 10:
                phone_no = phone[0]
                # print(phone[0])
                break

    browser.quit()
    return title, address, phone_no, lat_long
