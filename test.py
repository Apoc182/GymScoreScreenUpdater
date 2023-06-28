from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to a page
driver.get("https://flights.google.com")
input()
driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div/button/div[3]").click()
driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/ul/li[1]/div/div/span[3]/button/div[3]").click()

# Do something (e.g., a search query, login, etc.)

# Quit the browser
driver.quit()
