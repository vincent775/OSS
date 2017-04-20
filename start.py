# -*- coding: utf-8 -*-
'''
本程序是检测bbs，paper两个栏目每天的OSS和本地2.15数据库数量对比。
格式如：Python start.py   20170211
weiyt
'''
import oss2
from itertools import islice
import mssql
import sys,time
reload(sys)
sys.setdefaultencoding("utf-8")
parrm= sys.argv[1]
print parrm
if parrm!='' or parrm!='null':
    times = parrm
else:
    times = time.strftime('%Y%m%d')
    times = str(int(times) - 1)

x=0;y=0;z=0
auth = oss2.Auth('ya3W80ebpSx4ihkE', 'G44HC54wdOLCtl4m2adZWXOvgQDeoG')
bucket = oss2.Bucket(auth, 'oss-cn-shanghai.aliyuncs.com', 'instrumentbbs')
bucket2 = oss2.Bucket(auth, 'oss-cn-shanghai.aliyuncs.com', 'instrumentfile')

#print len(islice(oss2.ObjectIterator(bucket), 10))
# for b in islice(oss2.ObjectIterator(bucket), 1000):
#     print(b.key)
bbsfile = "select count(0) from ss_attachment where ExtName not in ('jpg','png','gif','bmp','jpeg','peg') and CONVERT(varchar(10), intime, 112) ='%s' " % times
bbsimg = "select count(0) from ss_attachment where ExtName in ('jpg','png','gif','bmp','jpeg','peg') and CONVERT(varchar(10), intime, 112) ='%s' " % times
bbssql="select count(*)  from ss_attachment where  CONVERT(varchar(10), intime, 112) ='%s'" % times
paperfile="select count(*)  from PaperAttachment where  CONVERT(varchar(10), intime, 112) ='%s'" % times

ms = mssql.MSSQL()

#bbs 文件
for obj in oss2.ObjectIterator(bucket, prefix='bbsfiles/files/2017/02/'+times,delimiter='/'):
     #print(obj.key)
     x+=1
print u"bbs文件：\n  oss %d ,本地 %d " % (x,ms.ExecQuery(bbsfile)[0][0])
#bbs 图片
for obj in oss2.ObjectIterator(bucket, prefix='bbsfiles/images/2017/02/'+times,delimiter='/'):
     #print(obj.key)
     y+=1
print u"bbs图片：\n  oss %d ,本地 %d " % (y,ms.ExecQuery(bbsimg)[0][0])

#bbs全部
print u"bbs全部：\n  oss %d ,本地 %d " % (x+y,ms.ExecQuery(bbssql)[0][0])
#paper 文件
for obj in oss2.ObjectIterator(bucket2, prefix='paperfiles/2017/02/'+times,delimiter='/'):
     #print(obj.key)
     z+=1
print u"paper文件：\n  oss %d ,本地 %d " % (z,ms.ExecQuery(paperfile)[0][0])