# -*- coding: utf-8 -*-
'''
1.200服务器E:\upload\  文件数全部写进sqlserver

os.walk(path),遍历path，返回一个对象，
他的每个部分都是一个三元组,
('目录x'，[目录x下的目录list]，目录x下面的文件)
'''
import os,time,sys
import mssql
parrm= sys.argv[1]
print parrm

ms = mssql.MSSQL()
def walk_dir(dir,parrm,topdown=True):
    w = 0
    fileinfo = open('listQuan.txt', 'a')
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            try:
                w += 1
                print(os.path.join(name))
                url = os.path.join(root,name)
                sql ="insert into log.dbo.file_show (oldurl,fileurl,ismod,bucket,intime,filetype) VALUES ('%s','%s',0,'instrumentnetshow','%s','%s') " \
                      % (url.encode("utf8"),url.encode("utf8"),time.strftime("%Y-%m-%d %X", time.localtime()),parrm)
                print sql
                ms.ExecNonQuery(sql)
                fileinfo.write(url+'\n')
            except Exception, e:
                print Exception, ":", e
                f = open('listerrorimage.txt', 'a')
                f.write(sql + '\n')
                f.close()
                pass
        # for name in dirs:
        #     print(os.path.join(name))
        #     fileinfo.write(' '+ os.path.join(root,name)+'\n')
    fileinfo.close()
    return w
#dir = raw_input('please input the path:')

if __name__=='__main__':
    dir = 'E:\upload\%s' % parrm
    walk_dir(dir,parrm)
