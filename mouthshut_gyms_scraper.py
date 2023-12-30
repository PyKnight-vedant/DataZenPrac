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
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
browser = webdriver.Chrome(options=chrome_options)
df = pd.DataFrame()
df["Name"] = ""
df["Sector"] = "Gyms"
df["City"] = ""
df["Address"] = ""
df["Phone"] = ""
df["Email"] = ""
df["Lat-Long"] = ""
'''
links = []
for i in range(1, 175):
    url = f"https://www.mouthshut.com/Gyms-and-Fitness-Centres-ProID-925758-page-{i}"
    browser.get(url)
    cards = browser.find_elements(By.CLASS_NAME, "card-body")
    for card in cards:
        link = card.find_element(
            By.TAG_NAME, "a").get_attribute("href")
        print(link)
        links.append(link)

file_path = "gym_links.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write each element to the file
    for link in links:
        file.write(link + "\n")
'''


# Specify the file path
file_path = "gym_links.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    # Read lines from the file and create a list
    links = file.readlines()

# Strip newline characters from each line
links = [link.strip() for link in links]

# Display the list
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
        df.loc[c, "Name"] = title
        df.loc[c, "Sector"] = "Gym"
        info = WebDriverWait(browser, 3).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "info-div"))
        )
        df.loc[c, "Address"] = info[0].text
        print("Address: ", info[0].text)
        if len(info) > 1:
            df.loc[c, "Phone"] = info[1].text
            print("Phone: ", info[1].text)
        print()

    except:
        continue
    finally:
        print("============================================================")
        df.to_csv("Final_Gyms.csv")
