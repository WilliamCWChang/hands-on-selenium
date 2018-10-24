from selenium import webdriver
from time import sleep
import os


if os.name == 'nt':
    driver = webdriver.Chrome()
else:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1080x1920')
    driver = webdriver.Chrome(chrome_options=options)


ip = "127.0.0.1:8000"
driver.get("http://" + ip)
# driver.get("http://127.0.0.1:8000/?/systemSetting")

# text_field = driver.find_element_by_xpath(
    # '//*[@id="Configuration"]/div/div/div/table/tbody/tr[1]/td[2]/div/button')
text_field = driver.find_element_by_id('45MR-1600-0-AliasName')
print(text_field.get_attribute("type"))

# text_field.send_keys("hello")
# sleep(20)
# text_field.clear()
driver.close()
