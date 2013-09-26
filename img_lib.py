#########################################################################
# File Name: ceshia.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python
import pycurl
import StringIO
import re
import MySQLdb as mdb
import sys
from urllib import quote
from pymmseg import mmseg
import pdb

con = mdb.connect(host="localhost",user="root",passwd="",db="mydb",port=3307)
with con:
    try:
        hd = con.cursor()
        hd.execute("set names utf8")
        sqlOne = "select title_en,id from a_img_lib where data_process=0"
        hd.execute(sqlOne)
        res = hd.fetchall()
        for r in res:
            search = quote(r[0])
            url = "http://translate.google.com.hk/translate_a/t?client=t&sl=en&tl=zh-CN&hl=zh-CN&sc=2&ie=UTF-8&oe=UTF-8&pc=1&oc=1&otf=1&ssel=0&tsel=0&q=%s" %(search)
            crl = pycurl.Curl()
            crl.setopt(pycurl.VERBOSE,1)
            crl.setopt(pycurl.FOLLOWLOCATION,1)
            crl.setopt(pycurl.MAXREDIRS,5)
            crl.fp = StringIO.StringIO()
            crl.setopt(pycurl.URL,url)
            crl.setopt(crl.WRITEFUNCTION,crl.fp.write)
            crl.perform()
            result = crl.fp.getvalue()
            
            rs = re.compile("\".*?\"")
            match = rs.search(result)
            title_cn = match.group()
            
            mmseg.dict_load_defaults()
            algor = mmseg.Algorithm(title_cn)
            for tok in algor:
                if(len(tok.text)>3):
                    #print "%s %s\n" %(tok.text,len(tok.text))
                    tag = mdb.escape_string(tok.text)
                    sqlTag = "select id from a_tag where name = '%s'" %tag
                    hd.execute(sqlTag)
                    tag_id = hd.fetchone()
#pdb.set_trace()
                    if(None!=tag_id): 
                        sqlTwo = "insert into a_img_tag_relation values(null,%d,%d,'%s',%d)" %(r[1],tag_id[0],tag,0)
                        hd.execute(sqlTwo)
            titleCnFormat = mdb.escape_string(title_cn)
            sqlThree = "update a_img_lib set title_cn='%s',data_process=1 where id=%d limit 1" %(titleCnFormat,r[1])
            hd.execute(sqlThree)

    except mdb.Error,e:
        print "Mysql error %d: %s" %(e.args[0],e.args[1])

