from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from prettyprinter import pprint

# TODO Get the article number from Wikipedia home page


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")


#Remove last item
# store_items.pop()

timeout = time.time() + 5
five_min = time.time() + 300

while True:
    cookie.click()
    
    if time.time() > timeout:
            
        store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")

        item_names = []
        item_prices = []
        store_item_names = []
        store_item_prices = []


        for item_name in store_items:
            item_names.append(item_name.text.split(" - ")[0])
            
        for item_price in store_items:
            item_prices.append(item_price.text.split(" - ")[1])


        for n in range(len(item_names)):
            store_item_names.append(item_names[n])
            store_item_str = (item_prices[n]).replace(",", "")
            store_item_prices.append(int(store_item_str))


        # for n in range(len(store_item_names)):
        #     store_dict = {store_item_prices[n]:store_item_names[n]}

        store_dict = dict(zip(store_item_prices, store_item_names))

        affordable_item_price = []

        saved_money = driver.find_element(By.ID, value="money").text
        saved_money = int(saved_money.replace(",", ""))


        for price in store_item_prices:
            if price < saved_money:
                affordable_item_price.append(price)


        most_expensive_item_affordable = store_dict[affordable_item_price[-1]].replace(" ", "")
        buy_item_id = f"buy{most_expensive_item_affordable}"
        purchase = driver.find_element(By.ID, value=buy_item_id)

        purchase.click()

        timeout = time.time() + 5



    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break