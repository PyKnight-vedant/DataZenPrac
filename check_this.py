from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
browser = webdriver.Chrome(options=chrome_options)


links = []
for i in tqdm(range(1, 1899)):
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
