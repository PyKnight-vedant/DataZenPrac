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
from tqdm import tqdm
df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv", index_col=[0])
l = []
for i in range(1, len(df)+1):
    l.append(i)
df.index = l

print(df[["Name", "Address", "Lat-Long"]])
print(df["Lat-Long"].notnull().sum())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
browser = webdriver.Chrome(options=chrome_options)


def scraper(i):
    # Obtain the Google Map URL
    if df.loc[i, "Email"] is np.NaN:
        df.loc[i, "Email"] = ""
    base_url = "https://www.google.com/search?q="
# "https://www.google.com/maps/place/Indian+Institute+Of+Technology%E2%80%93Madras+(IIT%E2%80%93Madras)/@12.9914929,80.2311104,17z/data=!3m1!4b1!4m6!3m5!1s0x3a5267f29aa9a61f:0x24ef264085e6a094!8m2!3d12.9914929!4d80.2336907!16zL20vMGd5eHdk?entry=ttu"]
# Open the Google Map URL
    org_name = str(df.loc[i, "Name"]+" " +
                   df.loc[i, "City"]+" "+df.loc[i, "Sector"] + " email").replace(" ", "+")
    url = base_url+org_name
    browser.get(url)
    print("\n", i, "---------", df.loc[i, "Name"],
          "---------", df.loc[i, "Lat-Long"])
    current_url = browser.current_url
    print("Current URL:", current_url)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    time.sleep(0.2)
    text = browser.page_source
    matches = re.findall(email_pattern, text)

    print(matches)
    s = ""
    for match in matches:
        match += ","
        if match != 'empty-light@2x.png,' and match != 'empty-dark@2x.png,':
            s += match
    print(s)
    df.loc[i, "Email"] = s
    time.sleep(0.2)
    df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv")


try:
    for no in tqdm(range(19410, 19600)):
        try:
            if df.loc[no, "Email"] is np.NaN:
                scraper(no)

        except KeyboardInterrupt:
            exit()

        except:
            continue

finally:
    print(f"Done at {no}")
    browser.quit()
    print(f"Email count: ")
    print(df.Email.notnull().sum())
    webbrowser.open(
        r"https://open.spotify.com/track/4pNNkkPGAb8GN2sh7XhiZO?si=1cbb16c6c93f48b9")
