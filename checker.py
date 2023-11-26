
# importing the modules
from selenium import webdriver
from selenium.webdriver.common.by import By


# using webdriver for chrome browser
driver = webdriver.Chrome()
url = ["https://www.google.com/maps/@19.0262545,72.863352,15z?entry=ttu"]
# using target url
driver.get(url[0])

# printing the content of entire page
print(driver.find_element(By.XPATH, "/html/body"))

# closing the driver
driver.close()
