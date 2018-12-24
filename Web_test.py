from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep


def element_should_invisible(self, locator):
    try:
        WebDriverWait(self.driver, g_web_timout).until(
            EC.invisibility_of_element_located(locator)
        )
    except Exception:
        self.driver.get_screenshot_as_file(self.image_path +
                                           strftime("%Y%m%d-%H%M%S",
                                                    gmtime()) + ".png")
        self.driver.quit()
        raise AssertionError(self.__class__.__name__,
                             sys._getframe().f_code.co_name)


def element_should_exist(self, locator):
    try:
        WebDriverWait(self.driver, g_web_timout).until(
            EC.presence_of_element_located(locator)
        )
    except Exception:
        self.driver.get_screenshot_as_file(self.image_path +
                                           strftime("%Y%m%d-%H%M%S",
                                                    gmtime()) + ".png")
        self.driver.quit()
        raise AssertionError(self.__class__.__name__,
                             sys._getframe().f_code.co_name)


for i in range(10000000):
    try:
        driver = webdriver.Chrome('C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver')
        driver.get("http://192.168.111.201")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("moxa")
        sleep(1)
        driver.find_element_by_id("Login").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loader"))
        )
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "loader")))
        # print("loader OK")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )
        text = driver.find_element(By.XPATH, '//*[@id="dashboard"]/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/span')
        print("message = " + text.text)
        sleep(1)

        print("OK")
    except Exception as e:
        print("Timeout!!!!")
    finally:
        driver.quit()
