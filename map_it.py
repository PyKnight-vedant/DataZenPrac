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

df = pd.read_csv(
    r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv", index_col=[0])
print(df[["Name", "Address", "Lat-Long"]])
print(df["Lat-Long"].notnull().sum())
# Create the webdriver object
try:
    for i in range(1, len(df)):
        try:
            browser = webdriver.Chrome()

    # Obtain the Google Map URL
            url = "https://www.google.com/maps/@19.0262545,72.863352,15z?entry=ttu"
# "https://www.google.com/maps/place/Indian+Institute+Of+Technology%E2%80%93Madras+(IIT%E2%80%93Madras)/@12.9914929,80.2311104,17z/data=!3m1!4b1!4m6!3m5!1s0x3a5267f29aa9a61f:0x24ef264085e6a094!8m2!3d12.9914929!4d80.2336907!16zL20vMGd5eHdk?entry=ttu"]
# Open the Google Map URL

            print(df.loc[i, "Name"])

            browser.get(url)
            wait = WebDriverWait(browser, 25)
            Place = browser.find_element(
                By.CLASS_NAME, "searchboxinput.searchboxinput.xiQnY")
            Place.send_keys(df.loc[i, "Name"])
            Place.send_keys(Keys.ENTER)


# Initialize variables and declare it 0


# Create a loop for obtaining data from URLs


# browser.get(url[i])

# Obtain the title of that place
            wait = WebDriverWait(browser, 15)

            title = wait.until(EC.presence_of_element_located(
                (By.XPATH,  "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1")))

            print(i, "-", title.text)

            address = browser.find_element(By.CLASS_NAME, "CsEnBe")
            print("\n", address.text)
            df.loc[i, "Address"] = address.text
# Get the current URL
            current_url = browser.current_url
            print("Current URL:", current_url)
            url_regex = re.compile("@\d+.\d+,\d+.\d+")
            lat_long = url_regex.findall(current_url)[0][1:]
            df.loc[i, "Lat-Long"] = lat_long
            browser.quit()

# Close the browser window when done

        except KeyboardInterrupt:
            print("Scraping stopped")
            exit()
        except:
            continue


finally:
    print(df[["Name", "Address", "Lat-Long"]])
    df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (3).csv")
    print(df["Lat-Long"].notnull().sum())
