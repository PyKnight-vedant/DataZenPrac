from selenium import webdriver
from selenium.webdriver.common.by import By

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
from tqdm import tqdm
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
browser = webdriver.Chrome(options=chrome_options)



links = []
for i in range(1, 1899):
    url = f"https://www.mouthshut.com/Restaurants-ProID-169-page-{i}"
    print(f"Scraping {url}")
    browser.get(url)
    cards = browser.find_elements(By.CLASS_NAME, "card-body")
    for card in cards:
        link = card.find_element(
            By.TAG_NAME, "a").get_attribute("href")
        print(link)
        links.append(link)

file_path = "links.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write each element to the file
    for link in links:
        file.write(link + "\n")

'''
df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\Final_Companies.csv", index_col=0)

df["Sector"] = "Companies(Private)"
# Specify the file path
file_path = "links.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    # Read lines from the file and create a list
    links = file.readlines()

# Strip newline characters from each line
links = [link.strip() for link in links]

# Display the list
print(links)

l = len(links)


for c in tqdm(range(20009, 30000)):
    print("============================================================")

    link = links[c-1]
    # print(link)
    try:
        browser.get(link)
        print(c)
        c += 1
        title = browser.find_element(
            By.XPATH, "/html/body/div[2]/form/div[22]/div/div[12]/div[5]/div/div[1]/div[1]/div/div/h1/a").text
        print(title)
        df.loc[c, "Name"] = title
        df.loc[c, "Sector"] = "Companies(Private)"
        info = WebDriverWait(browser, 3).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "info-div"))
        )
        df.loc[c, "Address"] = info[0].text
        # print("Address: ", info[0].text)
        if len(info) > 1:
            df.loc[c, "Phone"] = info[1].text
            # print("Phone: ", info[1].text)
        print()

    except KeyboardInterrupt:
        exit()

    except:
        continue
    finally:
        print("============================================================")
        df.to_csv("Final_Companies.csv")
        print(f"Restart from number {c}")'''

