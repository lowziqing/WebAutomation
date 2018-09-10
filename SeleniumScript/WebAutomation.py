from selenium import webdriver
import pandas as pandas
import numpy as numpy
from selenium.webdriver.common.keys import Keys

# userName = "matthew3169@gmail.com"
# Password = "s9316246c"
# Emails = "lowziqing@live.com"
# Subject = "Project on Selenium WebDriver"
# Message = "Good Evening Zi Qing, If you receive this email it would mean that the automation is executed " \
#           "successfully. Thank you <br> Warm Regards, <br> Low Zi Qing"
#
#
# def elementclick(xpath):
#     elem = driver.find_element_by_xpath("" + xpath + "")
#     elem.click()
#
#
# def inputs(xpath, inputs):
#     elem = driver.find_element_by_xpath("" + xpath + "")
#     elem.send_keys(inputs)
#
#
# driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
# driver.get("https://www.google.com/gmail/")
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# inputs("//*[@id='identifierId']", userName)
# elementclick("//*[@id='identifierNext']/content")
# driver.implicitly_wait(5)
#
# inputs("//*[@id='password']/div[1]/div/div[1]/input", Password)
# elementclick("//*[@id='passwordNext']/content")
# elementclick("//*[@id=':ko']/div/div")
# inputs("//*[@id=':q4']", Emails)
# inputs("//*[@id=':pm']", Subject)
# inputs("//*[@id=':qr']", Message)
# elementclick("//*[@id=':pc']")

# data = numpy.array(['alpha', 'bravo', 'charlie', 'delta'])
# s = pandas.Series(data, index=[1, 2, 3, 4])
# print(s)
# print('\n')
#
# dictdata = {'amy': 0, 'bella': 1, 'christine': 2}
# printdictdata = pandas.Series(dictdata)
# print(printdictdata)

## List consist of ["a","b","c"] - Ordered and changable. [Allow duplicate]
## Tuple = ("a", "b", "c") - Ordered and unchangable. [Allow duplicate]
## set = {"a", "b", "c"} - Unordered and unindexed. [No duplicate]
## Dictionary = {"brand" : "ford", "model" : "Mustang", "year" : 1964"} - Unordered, changeable and indexed. [No duplicate]

#Dataframe created from list
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pandas.DataFrame(data, columns=['Name', 'Age'], dtype=float)
print(df)
print('\n')

#Dataframe created from Dict of Array/List
dataArray = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
printdata = pandas.DataFrame(dataArray, index=['rank1','rank2','rank3','rank4'])
print(printdata)

#listofdictionary
dictdata = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pandas.DataFrame(dictdata, index=['first', 'second'], columns=['a', 'b'])
#df2 different col name will be not printed out.
df2 = pandas.DataFrame(dictdata, index=['first', 'second'], columns=['a', 'diffcolname'])
print(df1)
print(df2)

#https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/

#testing
