import cx_Oracle
import os
import pandas as pd

LOCATION = r"D:\workspace\instantclient_19_10"
os.environ["PATH"] = LOCATION +";" + os.environ["PATH"]
os.putenv('NLS_LANG',".UTF8")

connect = cx_Oracle.connect("hr","hr","172.16.8.75:11521/xepdb1")
cursor = connect.cursor()

cursor.execute("select * from employees")
# for i in cursor:
#     print(i)

row = cursor
colname = cursor.description
col = []
for i in colname:
    col.append(i[0])
emp = pd.DataFrame(row,columns=col)
print(emp)

