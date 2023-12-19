# import required modules
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

# get URL
page = requests.get(
    "https://en.wikipedia.org/wiki/Category:Companies_based_in_Chennai")

# scrape webpage
soup = BeautifulSoup(page.content, 'lxml')

list(soup.children)

# find all occurrence of p in HTML
# includes HTML tags
# print(soup.find_all('ul'))


# return only text
# does not include HTML tags
df = pd.DataFrame(columns=["Names"])
res1 = soup.find_all("li")
c = 1

for ele in res1:
    if c >= 58 and c <= 197:
        print(c, end="--")
        df.loc[c-57, "Names"] = ele.text
        print(ele.text)
    c += 1
df.to_csv(r"C:\Users\Vedant\Desktop\DataZenPrac\Private_Company.csv")
