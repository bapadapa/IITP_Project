#%%
!pip install cx_Oracle
# %%
from typing import Counter
import cx_Oracle

# %%
CONN_INFO = {
        'NAME': 'XEPDB1',
        'USER': 'iitp',
        'PASSWORD': 'iitp',
        'HOST': '172.16.30.241',
        'PORT': '11521',
}
CONN_STR = '{USER}/{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**CONN_INFO)
conn = cx_Oracle.connect(CONN_STR)
cursor = conn.cursor()


#%%
cursor.execute("SELECT * FROM USER_OBJECTS WHERE OBJECT_TYPE='TABLE'")