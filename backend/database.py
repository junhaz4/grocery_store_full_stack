import datetime
import pymysql

def get_sql_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='dbuserdbuser',
                                 database='grocery_store',
                                 autocommit=True)
    return connection
