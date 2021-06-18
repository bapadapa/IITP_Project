import cx_Oracle
import os
import pandas as pd
import numpy as np

LOCATION = r"D:\workspace\instantclient_19_10"
os.environ["PATH"] = LOCATION +";" + os.environ["PATH"]
os.putenv('NLS_LANG',".UTF8")

connect = cx_Oracle.connect("hr","hr","172.16.8.75:11521/xepdb1")
cursor = connect.cursor()

# HOSDJANGO_LOCINFO
loc = pd.read_csv('./hospitalData/hospital_LocInfo02.csv')

loc = loc.astype({'hosCode': 'int'})
loc = loc.astype({'Latitude': 'float'})
loc = loc.astype({'longitude': 'float'})
print(loc.shape)

# cursor.executemany("INSERT INTO HOSDJANGO_LOCINFO (LOC_HOSCODE,LOC_HOSNAME,LOC_HOSCLASSNAME,LOC_HOSCITYNAME,LOC_HOSCOUNTYNAME,LOC_ZIPCODE,LOC_HOSADDRESS,LOC_HOSPHONENUMBER,LOC_HOSURL,LOC_HOSESTABLISHMENT,LOC_LATITUDE,LOC_LONGITUDE) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)",loc)     
# cursor.executemany("INSERT INTO HOSDJANGO_LOCINFO (LOC_HOSCODE,LOC_HOSNAME,LOC_HOSCLASSNAME,LOC_HOSCITYNAME,LOC_HOSCOUNTYNAME,LOC_ZIPCODE,LOC_HOSADDRESS,LOC_HOSPHONENUMBER,LOC_HOSURL,LOC_HOSESTABLISHMENT,LOC_LATITUDE,LOC_LONGITUDE) values(:LOC_HOSCODE,:LOC_HOSNAME,:LOC_HOSCLASSNAME,:LOC_HOSCITYNAME,:LOC_HOSCOUNTYNAME,:LOC_ZIPCODE,:LOC_HOSADDRESS,:LOC_HOSPHONENUMBER,:LOC_HOSURL,:LOC_HOSESTABLISHMENT,:LOC_LATITUDE,:LOC_LONGITUDE)",loc)     
# for index, row in loc.iterrows():
#    cursor.execute("INSERT INTO HOSDJANGO_LOCINFO (LOC_HOSCODE,LOC_HOSNAME,LOC_HOSCLASSNAME,LOC_HOSCITYNAME,LOC_HOSCOUNTYNAME,LOC_ZIPCODE,LOC_HOSADDRESS,LOC_HOSPHONENUMBER,LOC_HOSURL,LOC_HOSESTABLISHMENT,LOC_LATITUDE,LOC_LONGITUDE) values(?,?,?,?,?,?,?,?,?,?,?,?)",row.hosCode, row.hosName, row.hosClassName, row.hosCityName,row.hosCountyName, row.zipCode, row.hosAddress, row.hosPhoneNumber, row.hosUrl,row.hosEstablishment, row.Latitude,row.longitude)     
for index, row in loc.iterrows():
   cursor.execute("INSERT INTO HOSDJANGO_LOCINFO (LOC_HOSCODE,LOC_HOSNAME,LOC_HOSCLASSNAME,LOC_HOSCITYNAME,LOC_HOSCOUNTYNAME,LOC_ZIPCODE,LOC_HOSADDRESS,LOC_HOSPHONENUMBER,LOC_HOSURL,LOC_HOSESTABLISHMENT,LOC_LATITUDE,LOC_LONGITUDE) values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)",row.hosCode, row.hosName, row.hosClassName, row.hosCityName,row.hosCountyName, row.zipCode, row.hosAddress, row.hosPhoneNumber, row.hosUrl,row.hosEstablishment, row.Latitude,row.longitude)     


connect.commit()
cursor.close()




