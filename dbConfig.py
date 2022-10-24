#import mariadb
import mysql.connector 

try:
 	#conn = mariadb.connect(
	conn = mysql.connector.connect(
		user="root",#帳號(上線的話帳號要改掉)
		password="",#密碼
		host="127.0.0.1",#主機
		port=3306,
		database="test"
	)
except: #mariadb.Error as e:
	print("Error connecting to DB")
	exit(1)
cur=conn.cursor()#執行sql檔
