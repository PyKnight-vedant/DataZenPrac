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
df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv", index_col=[0])
print(df[["Name", "Address", "Lat-Long"]])
print(df["Lat-Long"].notnull().sum())


def scraper(i):
    try:

        # Obtain the Google Map URL
        url = "https://www.google.com/maps/@18.4760628,73.9007086,15z?entry=ttu"
# "https://www.google.com/maps/place/Indian+Institute+Of+Technology%E2%80%93Madras+(IIT%E2%80%93Madras)/@12.9914929,80.2311104,17z/data=!3m1!4b1!4m6!3m5!1s0x3a5267f29aa9a61f:0x24ef264085e6a094!8m2!3d12.9914929!4d80.2336907!16zL20vMGd5eHdk?entry=ttu"]
# Open the Google Map URL

        print(i, "---------", df.loc[i, "Name"],
              "---------", df.loc[i, "Lat-Long"])
        if df.loc[i, "Lat-Long"] is np.nan:
            browser = webdriver.Chrome()
            browser.get(url)
            wait = WebDriverWait(browser, 25)
            Place = browser.find_element(
                By.CLASS_NAME, "searchboxinput.searchboxinput.xiQnY")
            Place.send_keys(df.loc[i, "Name"]+","+df.loc[i, "City"])
            Place.send_keys(Keys.ENTER)
            time.sleep(7)
            current_url = browser.current_url
            print("Current URL:", current_url)
            url_regex = re.compile("@\d+.\d+,\d+.\d+")
            lat_long = url_regex.findall(current_url)[0][1:]
            df.loc[i, "Lat-Long"] = lat_long
            browser.quit()
    except KeyboardInterrupt:
        print("Scraping stopped")
        exit()


processes = []
if __name__ == "__main__":

    # Create the webdriver object

    try:
        for i in range(1, len(df)+1):
            try:
                scraper(i)
            except:
                continue

    finally:
        print(df[["Name", "Address", "Lat-Long"]])
        df.to_csv(
            r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv")
        print(df["Lat-Long"].notnull().sum())
