# -*- coding: utf-8 -*-
#########################################################################
# File Name: ceshi.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python
import MySQLdb as mdb
from pymmseg import mmseg
import re
import chardet

con = mdb.connect(host="localhost",user="root",passwd="",db="mydb",port=3307,charset="utf8")
with con:
    try:
        hd = con.cursor()
        hd.execute("set names utf8")
        sqlOne = "select id,content,source_link from a_article"
        hd.execute(sqlOne)
        res = hd.fetchall()
        for info in res:
            #replace href value
            r = re.compile("<(|/)a(|.*?)>")
            test = r.sub("",info[1])
            #replace img src
            r = re.compile("<img.*?(>|\\>)")
            test = r.sub("",test)
            #replace html class or id
            r = re.compile("\s(id|style)=.*?>")
            test = r.sub(">",test)
            #remove other html tag
            r = re.compile("<(|/)span>")
            test = r.sub("",test)
            r = re.compile("gt")
            test = r.sub("",test)
            #remove insert_area
            test = "".join(test.split())
            r = re.compile("<divclass=\"insert_area\">.*?</div>")
            test = r.sub("",test)
            #empty html tag
            r = re.compile("<(div|p|ul|li){1}></\\1>")
            test = r.sub("",test)
            #replace html class or id
            r = re.compile("class=.*?>")
            test = r.sub(">",test)
        
            testa = mdb.escape_string(test.encode("utf8"))
            sqlThree = "update a_article set content='%s' where id=%d" %(testa,info[0])
            hd.execute(sqlThree)
            #remove all html tag for extract keywords
            r = re.compile("<[^>]+>",re.S)
            tmpTest = r.sub("",test)
            mmseg.dict_load_defaults()
            algor = mmseg.Algorithm(tmpTest)
            words = {}
            for tok in algor:
                if(len(tok.text)>=2):
                    #print '%s [%d..%d]' %(tok.text,tok.start,tok.end)
                    if(not tok.text in words.keys()):
                        words[tok.text] = 1
                    else:
                        words[tok.text] = words[tok.text]+1
            for key in words.keys():
                if(words[key]>=2):
                    #print "%s:\t%d" %(key,words[key])
                    sqlTwo = "insert into a_article_crawl_attr(article_id,tag,freq,source_link) values(%d,'%s','%s','%s')" %(info[0],key,words[key],info[2])
                    hd.execute(sqlTwo)
            print "%d:\t%d" %(info[0],((len(words)+1)/3))
    except mdb.Error,e:
        print "Mysql Error %d: %s" %(e.args[0],e.args[1])
