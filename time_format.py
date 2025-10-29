'''
Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
'''
# here some date and time changes are used to shows that
import datetime
input_date=list(map(int,input().split("-")))
date=datetime.datetime(2012,input_date[1],input_date[2])
print(date.strftime("%d-%m-%Y"))
