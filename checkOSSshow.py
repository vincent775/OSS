# -*- coding: utf-8 -*-
'''
网展检测 本地upload的数量数目与oss 2017年2月14日09:31:43 之前上传数据对比 存在修改ismod = 1
'''
import oss2
import sys,mssql
reload(sys)
sys.setdefaultencoding("utf-8")
parrm= sys.argv[1]
parrmTwo= sys.argv[2]

ms =mssql.MSSQL()
auth = oss2.Auth('ya3W80ebpSx4ihkE', 'G44HC54wdOLCtl4m2adZWXOvgQDeoG')
bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'instrumentnetshow')


selsql="select  id,oldurl from log.dbo.file_show where ismod =0 and filetype ='images'  and id>= %s  and id<=%s" % (parrm,parrmTwo)
#selsql="select  id,oldurl from log.dbo.file_show where ismod =0 and filetype ='files' "

list = ms.ExecQuery(selsql)
ids =''
i=0;
f = open('listcheckshow.txt', 'a')
for id,oldurl in list:
    #print str(id) +'/'+oldurl[9:]
    try:
        url ='17img/'+oldurl[10:].replace('\\','/')
        #print url
        exist = bucket.object_exists(url)
        print exist
        f.write(str(id)+','+str(exist)+','+oldurl + '\n')
        if exist:
            i += 1
            ids += str(id) + ','
            if i >499:
                sql = 'UPDATE log.dbo.file_show  with(rowlock) set ismod = 1 where id in (%s)' % ids[:-1]
                print sql
                ms.ExecNonQuery(sql)
                print sql
                i=0
                ids=''
        #else:
        #    print('object not eixst')
    except Exception, e:
        sql = 'UPDATE log.dbo.file_show  with(rowlock) set ismod = 1 where id in (%s)' % ids[:-1]
        ms.ExecNonQuery(sql)
        i = 0
        ids = ''
        print 'error 0000000000000000000000000000000000000000000000000000000000000000000000'
        pass
if 0<i<500:
    sql33 = 'UPDATE log.dbo.file_show with(rowlock) set ismod = 1 where id in (%s)' % ids[:-1]
    print sql33
    ms.ExecNonQuery(sql33)
f.close()
