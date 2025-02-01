from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from prettyprinter import pprint

# TODO Get the article number from Wikipedia home page

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# consent_button = driver.find_element(By.CSS_SELECTOR, value='.fc-cta-consent')
# english_button = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')


cookie = driver.find_element(By.ID, value="cookie")


store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")

store_items.pop()
item_names = []
item_prices = []

for item_name in store_items:
    item_names.append(item_name.text.split(" - ")[0])
    
for item_price in store_items:
    item_prices.append(item_price.text.split(" - ")[1])

# print(item_names)
# print(item_prices)

store_dict = {}
for n in range(len(item_names)):
    store_dict[n] = {item_names[n]:item_prices[n]}
    
pprint(store_dict)



# while True:
#     cookie.click()








driver.close()