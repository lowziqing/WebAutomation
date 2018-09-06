from selenium import webdriver
from selenium.webdriver.common.keys import Keys

userName = "matthew3169@gmail.com"
Password = "s9316246c"
Emails = "lowziqing@live.com"
Subject = "Project on Selenium WebDriver"
Message = "Good Evening Zi Qing, If you receive this email it would mean that the automation is executed " \
          "successfully. Thank you <br> Warm Regards, <br> Low Zi Qing"


def elementclick(xpath):
    elem = driver.find_element_by_xpath("" + xpath + "")
    elem.click()


def inputs(xpath, inputs):
    elem = driver.find_element_by_xpath("" + xpath + "")
    elem.send_keys(inputs)


driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
driver.get("https://www.google.com/gmail/")
driver.maximize_window()
driver.implicitly_wait(5)

inputs("//*[@id='identifierId']", userName)
elementclick("//*[@id='identifierNext']/content")
driver.implicitly_wait(5)

inputs("//*[@id='password']/div[1]/div/div[1]/input", Password)
elementclick("//*[@id='passwordNext']/content")
elementclick("//*[@id=':ko']/div/div")
inputs("//*[@id=':q4']", Emails)
inputs("//*[@id=':pm']", Subject)
inputs("//*[@id=':qr']", Message)
elementclick("//*[@id=':pc']")

#testing
