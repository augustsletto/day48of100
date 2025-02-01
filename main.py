from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")


# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_decimal = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The computer is {price_dollar.text}.{price_decimal.text}")


# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link)




# titles = ["Python devroom", "PyCascades", "Python Barcamp Karlsruhe", "Django Girls Koforidua", "DjangoCongress"]
# dates = ["2025-02-02", "2025-02-08", "2025-02-15", "2025-02-21", "2025-02-22"]





# event_title = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a')
# event_date = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time')
    



# nested = {}

# for i in range(1, 6):
    
        
#     title_fstring = f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a'
#     date_fstring = f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time'
    
#     event_title = driver.find_element(By.XPATH, value=title_fstring).text
#     event_date = driver.find_element(By.XPATH, value=date_fstring).text
    
    
    
#     nested[i] = {"name": event_title, "date":event_date}

# print(nested)



event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in event_times:
    print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
    
for name in event_names:
    print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {"name": event_names[n].text, "date":event_times[n].text}
    
print(events)

# driver.close()
driver.quit()