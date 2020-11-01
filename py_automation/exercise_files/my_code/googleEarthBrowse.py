# %%
# Have Selenium use webdriver, and load extra modules to facility async wait functions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url = 'https://www.google.com/earth/'
driver = webdriver.Firefox()
driver.get(url)

# %%
# Institute the wait function
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchEarthButton.click()