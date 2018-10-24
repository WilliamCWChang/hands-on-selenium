from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com")
driver.find_element_by_id("email").send_keys("iwtfagp")
driver.find_element_by_id("pass").send_keys("asc09ixo")
driver.find_element_by_id("loginbutton").click()
driver.get("https://www.facebook.com/groups/277524959024108/photos/")
photos = driver.find_elements_by_class_name("uiMediaThumbLarge")
# photos = driver.find_elements_by_xpath("//div[@class='uiMediaThumb uiScrollableThumb uiMediaThumbLarge']")
images = []
for photo in photos:
	images.append(photo.get_attribute("href"))
# print(images)
driver.implicitly_wait(2) # seconds


for image in images:
	num = image.find("ifg")-1
	url = image[:num] + '&theater' + image[num:]
	driver.get(url)

	wait = WebDriverWait(driver, 10)
	wait.until(EC.presence_of_element_located((By.CLASS_NAME , 'spotlight')))	

	# while driver.find_element_by_class_name("spotlight").get_attribute("aria-busy")  is True:
	# 	# sleep(0.5)
	# 	pass

	# check = True


	# while check:
	# 	print(driver.find_element_by_class_name("spotlight"))
	# 	data = driver.find_element_by_class_name("spotlight").get_attribute("src")
	# 	if data == "https://www.facebook.com/rsrc.php/v3/y4/r/-PAXP-deijE.gif":
	# 		check = True
	# 	elif data == "https://www.facebook.com/rsrc.php/v3/ym/r/ApyI70_PuhE.gif":
	# 		check = True
	# 	else:
	# 		check = False


	print(driver.find_element_by_class_name("spotlight").get_attribute("src"))
	# print("![](" + image_url.get_attribute("href") +")" ) 
	# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()