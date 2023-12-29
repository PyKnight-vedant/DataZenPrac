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
from maps_scraper import scraper

title, address, phone_no, lat_long = scraper(
    "https://www.google.com/maps/place/Azim+Premji+University/data=!4m7!3m6!1s0x3bae6ca333d66cbb:0x2d04fd24fb931c3b!8m2!3d12.8452628!4d77.7768752!16s%2Fm%2F0jzspd0!19sChIJu2zWM6NsrjsROxyT-yT9BC0?authuser=0&hl=en&rclk=1")

print("Title: "+title)
print("Address: "+address)
print("Phone Number: "+phone_no)
