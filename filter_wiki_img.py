#########################################################################
# File Name: filter_wiki_img.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python
import MySQLdb as mdb

con = mdb.connect(host="localhost",user="root",passwd="",db="mydb",port=3307)
with con:
    try:
        hd = con.cursor()
        sqlOne = "select    "    
