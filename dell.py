import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

products = []
with open("products.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        products.append(row)

print("List of prodducts:")
for product in products:
    print(product)

options = webdriver.ChromeOptions()
options.debugger_address="127.0.0.1:9222"


driver = webdriver.Chrome(options=options)

for product in products:
    print(f"Downloading - {product}")
    driver.get("https://www.dell.com/support/home/pl-pl/products/")

    time.sleep(3)

    spam_btn = driver.find_element(By.ID, "btnBreadCrumpAllProductsClose")
    spam_btn.click()

    time.sleep(3)

    search_input = driver.find_element(By.NAME, "homemfe-dropdown-name")
    search_input.send_keys(product)
    time.sleep(3)
    search_input.send_keys(Keys.RETURN)

    time.sleep(3)

    sys_config = driver.find_element(By.ID, "quicklink-sysconfig")
    sys_config.click()

    time.sleep(3)

    curr_conf_exp = driver.find_element(By.ID, "current-config-export")
    curr_conf_exp.click()
