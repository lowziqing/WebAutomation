from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_argument("--disable-infobars")
driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe", chrome_options=chrome_option)
class Functions:

    def inputs(self, xpath, inputs):
        elem = driver.find_element_by_xpath(xpath)
        elem.send_keys(inputs)
        sleep(5)
        driver.implicitly_wait(5)

    def tabEnter(self, number):
        action = ActionChains(driver)
        action.send_keys(Keys.TAB * number)
        action.send_keys(Keys.ENTER)
        sleep(0.2)
        action.perform()
        sleep(0.5)

    def newTab(self, website, tabNumber):
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[tabNumber])
        driver.get(website)

    def getDriver(self):
        getDriver = driver
        return getDriver

    def newBrowser(self, website):
        chrome_option = Options()
        chrome_option.add_argument("--disable-infobars")
        driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe", chrome_options=chrome_option)
        driver.get(website)


