from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from time import gmtime, strftime, time


g_timeout = 30
g_save_config_timeout = 30

ip = "192.168.111.201"
exec_times = 10


for i in range(exec_times):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1080x1920')
        driver = webdriver.Chrome(
            '.\\chromedriver_win32\\chromedriver', chrome_options=options)
        driver.set_page_load_timeout(g_timeout)
        driver.implicitly_wait(g_timeout)
        driver.get("http://" + ip)

        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("moxa")
        driver.find_element_by_id("Login").click()

        WebDriverWait(driver, g_timeout).until(
            EC.presence_of_element_located((By.ID, "loader"))
        )
        WebDriverWait(driver, g_timeout).until(
            EC.invisibility_of_element_located((By.ID, "loader")))
        # print("loader OK")
        WebDriverWait(driver, g_timeout).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )
        device_name = driver.find_element(By.ID, 'dashboard-deviceName-value')
        # print(device_name.text)

        system_status = driver.find_element(By.ID, 'dashboard-systemStatus-value')
        # print(system_status.text)

        system_page_menu_button = driver.find_element(
            By.XPATH, '//*[@id="menu"]/li[2]/div/span[2]')
        system_page_menu_button.click()

        system_page_server_name = driver.find_element(By.ID, 'ServerName')
        system_page_server_name.clear()
        system_page_server_name.send_keys(strftime("%Y%m%d_%H%M%S", gmtime()))
        sleep(1)

        # Module_button = driver.find_element(By.ID, 'dashboard-moduleInfo')
        # Module_button.click()

        # WebDriverWait(driver, g_save_config_timeout).until(
        #     EC.presence_of_element_located((By.ID, 'dashboard-0-1-DI-1-channelSetStatusControl'))
        # )

        # test_button = driver.find_element(By.ID, 'dashboard-0-1-DI-1-channelSetStatusControl')
        # test_button.click()
        # sleep(5)

        save_and_restart_button = driver.find_element(
            By.XPATH, '//*[@id="nav"]/div/div[3]/ul[1]/li/a[1]')
        save_and_restart_button.click()

        save_and_restart_button_inner = driver.find_element(
            By.XPATH, '//*[@id="inner"]/div/div/div[4]/div/div/button[1]')
        save_and_restart_button_inner.click()

        WebDriverWait(driver, g_save_config_timeout).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="inner"]/div/div/div[3]'), "Save Success.")
        )

        WebDriverWait(driver, g_save_config_timeout).until(
            EC.presence_of_element_located((By.ID, 'Login'))
        )

        print("[Success](" + str(i + 1) + "/" + str(exec_times) + ")")

    except Exception as e:
        filename = strftime("%b%d%Y%H%M%S.png", gmtime())
        print("[Fail   ](" + str(i + 1) + "/" +
              str(exec_times) + ")[" + str(e) + "]" + filename)
        driver.get_screenshot_as_file(filename)
    finally:
        driver.quit()
