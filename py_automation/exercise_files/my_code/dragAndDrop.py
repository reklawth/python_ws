# %%
# Have Selenium use webdriver, basically a web browser for it to interact with the web
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox() # Initialize the webdriver using Firefox
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

# %%
# Find elements using xpath
WashingtonSource = driver.find_element_by_xpath('//*[@id="box3"]')
USDestination = driver.find_element_by_xpath('//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(WashingtonSource, USDestination).perform()

# %%
# Find Rome, Italy elements using xpath
RomeSource = driver.find_element_by_xpath('//*[@id="box6"]')
ItalyDestination = driver.find_element_by_xpath('//*[@id="box106"]')
actions = ActionChains(driver)
actions.drag_and_drop(RomeSource, ItalyDestination).perform()

# %%
# Find Oslo, Norway elements using xpath
OsloSource = driver.find_element_by_xpath('//*[@id="box1"]')
NorwayDestination = driver.find_element_by_xpath('//*[@id="box101"]')
actions = ActionChains(driver)
actions.drag_and_drop(OsloSource, NorwayDestination).perform()

# %%
