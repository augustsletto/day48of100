from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# TODO Get the acrticle number from wikipedia home page 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
# driver.maximize_window()

# article_count = driver.find_element(By.XPATH, value='//*[@id="huvudsidaintro"]/tbody/tr/td[2]/a[4]')
# article_count.click()
# print(article_count.text)

fname_search = driver.find_element(By.NAME, value="fName")
fname_search.send_keys("August")

lname_search = driver.find_element(By.NAME, value="lName")
lname_search.send_keys("Sletto")

email_search = driver.find_element(By.NAME, value="email")
email_search.send_keys("augustsletto@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()

driver.close()


