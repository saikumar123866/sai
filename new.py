import time

from select import select
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_check:
    def test_demoqa(self):
        try:

            driver = webdriver.Chrome()
            wait = WebDriverWait(driver, 10)
            driver.get("https://qavalidation.com/demo-form/")
            driver.maximize_window()
            time.sleep(1)
            actions = ActionChains(driver)
            driver.find_element(By.XPATH, "(//*[@type='text'])[4]").send_keys("Bommena Saikumar")
            time.sleep(1)
            driver.find_element(By.XPATH, "(//*[@type='email'])[1]").send_keys("saikumarbommena827@gmail.com")
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[@type='tel']").send_keys("0987654321")
            time.sleep(1)
            s = driver.find_element(By.XPATH, "//*[@name='g4072-gender']")
            sel = Select(s)
            sel.select_by_visible_text("NA")
            # for i in range(1, 3):
            # actions.send_keys(Keys.DOWN).perform()
            # actions.send_keys(Keys.ENTER).perform()
            time.sleep(1)
            driver.find_element(By.XPATH, "(//*[@type='radio'])[4]").click()
            time.sleep(1)
            driver.find_element(By.ID, "g4072-skills-Automation testing").click()
            time.sleep(1)
            a = driver.find_element(By.XPATH, "//*[@name='g4072-qatools']")
            drop = Select(a)
            drop.select_by_visible_text("Appium")
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[@rows='20']").send_keys("BTech")
            time.sleep(1)
            wait.until(EC.presence_of_element_located(By.XPATH, "(//*[@type='submit'])[4]")).click()
            time.sleep(5)
        except Exception as e:
            print(str(e))
