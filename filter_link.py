#########################################################################
# File Name: filter_link.py
# Author: arkulo
# mail: arkulo@163.com
#########################################################################
#!/usr/bin/python
import MySQLdb as mdb
import re
import os
import shutil
#import pdb

con = mdb.connect(host="localhost",user="root",passwd="",db="mydb",port=3307)
with con:
    try:
        hd = con.cursor()
        sqlOne = "select a.id,a.content,b.url,b.path from a_article a left join a_article_image b on (a.id=b.article_id)"
        hd.execute(sqlOne)
        result = hd.fetchall()
        for res in result:
            #special word link where in content
            r = re.compile("href=\".*?\"")
            noLink = r.sub("href=\"http://www.labihua.cn\"",res[1])
            #remove all img tag
            if(None!=res[3]):      
                imgName = res[3].split("/")
                dirs = imgName[1][0]
                q = re.compile("<img.*?(>|\\>)")
                ct = q.sub("",noLink)
                #add img which crawled
                p = re.compile("><")
                resCt = p.sub("><p class='art_img'><img src='/article/"+dirs+"/"+imgName[1]+"'></p><",ct,1)
                #print resCt+"\n"
                #move img to new dritory
                imgTmpPath = "/home/arkulo/root/python-file/test/scrapy-test/kakakula/testone/testone/downloaded-image/full/"+imgName[1]
                path = "/home/arkulo/root/python-file/test/article/"+dirs+"/"+imgName[1]
                #pdb.set_trace()
                shutil.copyfile(imgTmpPath,path)
                noLink = resCt
            #update content which in mysql
            noLink = mdb.escape_string(noLink)        
            sqlTwo = "update a_article set content='%s' where id = %d" %(noLink,res[0])
            hd.execute(sqlTwo)
            print res[0]
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" %(e.args[0],e.args[1])








