# -*- coding: utf-8 -*-
#########################################################################
# File Name: ppmmseg_dict.py
# Author: arkulo
# mail: arkulo@163.com
# Created Time: 2013年09月09日 星期一 14时21分21秒
#########################################################################
#!/usr/bin/python
import MySQLdb as mdb
import chardet
import pdb

con = mdb.connect(host="localhost",user="root",passwd="",db="mydb",port=3307,charset="utf8")
with con:
    hd = con.cursor()
    hd.execute("set names utf8")
    sqlOne = "select name from a_tag"
    hd.execute(sqlOne)
    res = hd.fetchall()
    f = file("words.txt","w")
    for name in res:
        if(""!=name[0]):
            content = "1 %s\r\n" %name[0]
            a = content.encode("utf-8")
#pdb.set_trace()
            f.writelines(a)
    f.close()
    hd.close()

con.close()

