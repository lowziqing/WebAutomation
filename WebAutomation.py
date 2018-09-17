import marshal
import datetime
from time import sleep
from SeleniumScript import PYCCompiler
from SeleniumScript import SeleniumFunctions
from SeleniumScript import TimeManager
from selenium.webdriver.common.action_chains import ActionChains

# Calling modules from other files
Com = PYCCompiler.Compiler()
SF = SeleniumFunctions.Functions()
TM = TimeManager.TimeManager()
now = datetime.datetime.now()
Com.compileCredentials()

# instantiate object to call PYC file
s = open('SeleniumScript/Credentials.pyc', 'rb')
s.seek(8)
code_object = marshal.load(s)
exec code_object

# variables for Gmail input
Emails = "matthew3169@gmail.com"
Subject = "Project on Automation" + TM.getDateTime()['currentDateTime']
Message = "Good Evening Zi Qing, If you receive this email it would mean that the automation is executed " \
          "successfully. Thank you Warm Regards, Low Zi Qing"
counter = 0

# Calling google chrome and inputting website.
actions = ActionChains(SF.getDriver())
SF.getDriver().get("https://www.google.com/gmail/")
SF.getDriver().implicitly_wait(15)

SF.inputs("//input[@type='email']", Gmail())
SF.tabEnter(3)

SF.inputs("//*[@id='password']/div[1]/div/div[1]/input", Gmail_password())
SF.tabEnter(2)
sleep(20)
SF.tabEnter(11)
sleep(2)

SF.inputs("//*[@id=':q4']", Emails)
SF.inputs("//*[@id=':pm']", Subject)
SF.inputs("//*[@id=':qr']", Message)
SF.tabEnter(1)
SF.newTab("https://outlook.live.com/owa/", 1)

SF.tabEnter(8)
SF.inputs("//input[@type='email']", Hotmail())
SF.tabEnter(2)
SF.inputs("//input[@type='password']", Hotmail_password())
SF.tabEnter(3)
sleep(4)
SF.newTab("https://www.fireeye.com/cyber-map/threat-map.html", 2)

while True:
    SF.getDriver().switch_to.window(SF.getDriver().window_handles[counter])
    sleep(10)
    counter = counter + 1
    if counter > 2:
        counter = 0
    if int(TM.getDateTime()['currentTime']) >= 700 and int(TM.getDateTime()['currentTime']) <= 710:
        website = TM.checkDays(TM.getDateTime()['currentDay'])









