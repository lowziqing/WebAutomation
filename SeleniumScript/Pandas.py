## Pandas

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

# #Dataframe created from list
# data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
# df = pandas.DataFrame(data, columns=['Name', 'Age'], dtype=float)
# print(df)
# print('\n')
#
# #Dataframe created from Dict of Array/List
# dataArray = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
# printdata = pandas.DataFrame(dataArray, index=['rank1','rank2','rank3','rank4'])
# print(printdata)
#
# #listofdictionary
# dictdata = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df1 = pandas.DataFrame(dictdata, index=['first', 'second'], columns=['a', 'b'])
# #df2 different col name will be not printed out.
# df2 = pandas.DataFrame(dictdata, index=['first', 'second'], columns=['a', 'diffcolname'])
# print(df1)
# print(df2)

#https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/
#testing

#sender, email body, URL, file hash, subject, final tag.

# exceldata = pandas.read_csv('C:/Users/LowZiQing/PycharmProjects/Test1/CSV/enrollments.csv', names=[
#                                                          'account_key',
#                                                          'status',
#                                                          'join_date',
#                                                          'cancel_date',
#                                                          'days_to_cancel',
#                                                          'is_canceled'])
#
# splunkdata = pandas.read_csv('C:/Users/LowZiQing/PycharmProjects/Test1/CSV/splunkdata.csv', names=[
#                                                          'sender',
#                                                          'email_body',
#                                                          'URL',
#                                                          'file_hash',
#                                                          'subject',
#                                                          'final_tag'])
#
# print(exceldata)
# print(splunkdata.replace
