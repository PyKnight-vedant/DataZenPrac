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
print(df["Phone"].notnull().sum())


def scraper(i):

    # Obtain the Google Map URL
    url = "https://www.google.com/maps/@18.4760628,73.9007086,15z?entry=ttu"
# "https://www.google.com/maps/place/Indian+Institute+Of+Technology%E2%80%93Madras+(IIT%E2%80%93Madras)/@12.9914929,80.2311104,17z/data=!3m1!4b1!4m6!3m5!1s0x3a5267f29aa9a61f:0x24ef264085e6a094!8m2!3d12.9914929!4d80.2336907!16zL20vMGd5eHdk?entry=ttu"]
# Open the Google Map URL

    print(i, "===================================\n", df.loc[i, :])
    if df.loc[i, "Phone"] is np.nan or df.loc[i, "Address"] is np.nan or df.loc[i, "Lat-Long"] is np.nan:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--incognito')
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url)
        wait = WebDriverWait(browser, 3)
        Place = browser.find_element(
            By.CLASS_NAME, "searchboxinput.searchboxinput.xiQnY")
        Place.send_keys(df.loc[i, "Name"]+","+df.loc[i, "City"])
        Place.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 8)
        title = wait.until(EC.presence_of_element_located(
            (By.XPATH,  "/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1")))

        print(i, "-", title.text)

        address = browser.find_element(By.CLASS_NAME, "CsEnBe")
        print("\n", address.text)
        df.loc[i, "Address"] = address.text

        phone_no = wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "Io6YTe.fontBodyMedium.kR99db")))

        for ele in phone_no:
            phone_regex = re.compile("\d+\s*\d+\s*\d+")
            phone = phone_regex.findall(ele.text)
            if len(phone) > 0:
                if len(phone[0]) >= 10:
                    print(phone[0])
                    break
        df.loc[i, "Phone"] = phone[0]
        # Get the current URL
        time.sleep(3)
        current_url = browser.current_url
        print("Current URL:", current_url)
        url_regex = re.compile("@\d+.\d+,\d+.\d+")
        lat_long = url_regex.findall(current_url)[0][1:]
        df.loc[i, "Lat-Long"] = lat_long
        browser.quit()


if __name__ == "__main__":

    # Create the webdriver object

    try:
        for i in range(12395, 1124, -1):
            try:
                scraper(i)

            except KeyboardInterrupt:
                exit()

            except:
                continue
            # except:
                # print("Some issue occured")
                # continue

    finally:
        print(df[["Name", "Phone", "Address", "Lat-Long"]])
        df.to_csv(
            r"C:\Users\Vedant\Desktop\DataZenPrac\App2Build_Deliverable (4).csv")
        print(df["Phone"].notnull().sum())
        webbrowser.open(
            r"https://open.spotify.com/track/4cjrtfi0I7xLMQvxnICu6U?si=4d87843fb55b4c47")
