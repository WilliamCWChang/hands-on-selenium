# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
driver.get('http://www.google.com')
driver.find_element(By.ID, 'lst-ib').send_keys("XDDDD")
driver.find_element(By.ID, 'lst-ib').send_keys(Keys.ENTER)

locator = (By.ID, 'resultStats')

try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
    print(driver.find_element(By.ID, 'resultStats').text)
finally:
    driver.close()