import pymysql.cursors

host = 'localhost'
user = 'root'
password = ''

database = 'skripsi_4'

def conn():
    conn = pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return conn































