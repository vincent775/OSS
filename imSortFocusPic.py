# -*- coding: utf-8 -*-
import mssql

ms = mssql.MSSQL()

sql ="SELECT Subject_ID, Subject_Img   FROM   dbo.News_Subject WHERE Subject_Img LIKE '%news/spic%' ORDER  BY InTime DESC"
relist = ms.ExecQuery(sql)
print len(relist)
for Subject_ID,Subject_Img in relist:
    print Subject_ID
    print Subject_Img
    Subject_Img=Subject_Img.replace('sp','Sp')
    print Subject_Img
    sqlup ="UPDATE News_Subject SET Subject_Img ='%s'  WHERE Subject_ID = %s" % (Subject_Img,Subject_ID)
    ms.ExecNonQuery(sqlup)