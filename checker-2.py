
import os
import time
import pandas as pd
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

driver = webdriver.Chrome()

# driver.get method() will navigate to a page given by the URL address
driver.get(
    "https://www.justdial.com/Delhi/Ceiling-Tile-Dealers-Armstrong/nct-11271379")


def strings_to_num(argument):

    switcher = {
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0',
        'yz': '1',
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    }
    return switcher.get(argument, "nothing")


storeDetails = driver.find_elements(By.CLASS_NAME, 'store-details')

nameList = []
addressList = []
numbersList = []

for i in range(len(storeDetails)):

    name = storeDetails[i].find_elements(By.CLASS_NAME, 'lng_cont_name').text
    address = storeDetails[i].find_elements(By.CLASS_NAME, 'cont_sw_addr').text
    contactList = storeDetails[i].find_elements(By.CLASS_NAME, 'mobilesv')

    myList = []

    for j in range(len(contactList)):

        myString = contactList[j].get_attribute('class').split("-")[1]

        myList.append(strings_to_num(myString))

    nameList.append(name)
    addressList.append(address)
    numbersList.append("".join(myList))


# intialise data of lists.
data = {'Company Name': nameList,
        'Address': addressList,
        'Phone': numbersList}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# Save Data as .csv
df.to_csv('demo1.csv', mode='a', header=False)
