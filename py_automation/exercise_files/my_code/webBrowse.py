# %%
# Have Selenium use webdriver, basically a web browser for it to interact with the web
from selenium import webdriver
driver = webdriver.Firefox() # Initialize the webdriver using Firefox
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# %%
# Find element to input our Hello World message
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
# Interact with element by passing a string to it
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

# %%
# Interact with Two input field section of webpage
aMessageField = driver.find_element_by_xpath('//*[@id="sum1"]')
bMessageField = driver.find_element_by_xpath('//*[@id="sum2"]')
# Pass integers to both elements
aMessageField.send_keys('8')
bMessageField.send_keys('4')
totalMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
totalMessageButton.click()

# %%
