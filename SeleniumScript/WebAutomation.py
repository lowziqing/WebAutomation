import os
import marshal
import time
import datetime
from SeleniumScript import PasswordEncodeManager
from SeleniumScript import Credentials
from SeleniumScript import PYCCompiler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

now = datetime.datetime.now()
currentDateTime = now.strftime("%Y-%m-%d %H:%M")


PYCCompiler.compileCredentials()
print('getting credentials')
print(PYCCompiler.getCredentials())

# Password1 = os.getenv("User_Password")
# Password2 = password()
# encodedPassword = PasswordEncodeManager.password()
# Password3 = PasswordEncodeManager.passwordDecoder(encodedPassword)
#
# print(Password1)
# print(Password2)
# print(Password3)

# userName = "matthew3169@gmail.com"
# Emails = "matthew3169@gmail.com"
# Subject = "Project on Automation" + currentDateTime
# Message = "Good Evening Zi Qing, If you receive this email it would mean that the automation is executed " \
#           "successfully. Thank you Warm Regards, Low Zi Qing"
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
# inputs("//*[@id='password']/div[1]/div/div[1]/input", password())
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
