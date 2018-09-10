
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from SeleniumScript import Credentials
import os

Password = os.environ.get('User_Password')
#Password = Credentials.password()

# userName = "matthew3169@gmail.com
# Emails = "matthew3169@gmail.com"
# Subject = "Project on Selenium WebDriver"
# Message = "Good Evening Zi Qing, If you receive this email it would mean that the automation is executed " \
#           "successfully. Thank you <br> Warm Regards, <br> Low Zi Qing"
#
#
# def inputs(xpath, inputs):
#     elem = driver.find_element_by_xpath(xpath)
#     elem.send_keys(inputs)
#     time.sleep(2)
#     driver.implicitly_wait(2)
#
#
# def tabEnter(number):
#     action = ActionChains(driver)
#     action.send_keys(Keys.TAB * number)
#     action.send_keys(Keys.ENTER)
#     time.sleep(0.2)
#     action.perform()
#     time.sleep(0.5)
#
#
# driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
# actions = ActionChains(driver)
# driver.get("https://www.google.com/gmail/")
# driver.implicitly_wait(10)
#
# inputs("//input[@type='email']", userName)
# tabEnter(3)
#
# inputs("//*[@id='password']/div[1]/div/div[1]/input", Password)
# tabEnter(2)
# time.sleep(20)
# tabEnter(11)
# #elem = driver.find_element_by_xpath("//*[@id=':ko']/div/div | //*[@id=':kn']/div/div")
# #elem.click()
# time.sleep(2)
#
# inputs("//*[@id=':q4']", Emails)
# inputs("//*[@id=':pm']", Subject)
# inputs("//*[@id=':qr']", Message)
# tabEnter(1)
#
#
#
