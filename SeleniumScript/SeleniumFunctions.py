from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import TimeManager
import WebAutomation
TM = TimeManager.TimeManager()


class Functions:

    def __init__(self):
        self.chrome_option = Options()
        self.chrome_option.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe",
                                       chrome_options=self.chrome_option)

    def inputs(self, xpath, inputs):
        elem = self.driver.find_element_by_xpath(xpath)
        elem.send_keys(inputs)
        self.driver.implicitly_wait(5)

    def tabEnter(self, number):
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB * number)
        action.send_keys(Keys.ENTER)
        action.perform()
        sleep(0.5)

    def newTab(self, website):
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(website)

    def getDriver(self):
        getDriver = self.driver
        return getDriver

    def newBrowser(self, website):
        chrome_option = Options()
        chrome_option.add_argument("--disable-infobars")
        driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe",
                                  chrome_options=chrome_option)
        driver.maximize_window()
        driver.get(website)
        try:
            elem = driver.find_element_by_xpath("/html/body")
            sleep(1)
            elem.send_keys("F")
            sleep(30)
            driver.close()
        except:
            return



