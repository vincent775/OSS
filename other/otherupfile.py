# -*- encoding: utf-8 -*-
import sys
import time, os, sys

import oss2

import mssql
ms = mssql.MSSQL()
reload(sys)
sys.setdefaultencoding('utf8')
act= sys.argv[1]
dir= sys.argv[2]
parrm= sys.argv[3]
print dir
print parrm

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'ya3W80ebpSx4ihkE')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'G44HC54wdOLCtl4m2adZWXOvgQDeoG')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'instrumentother')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-beijing.aliyuncs.com')
# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

def upfile(dir):
        localurl=dir.strip()
        line = dir.replace(parrm,act).replace('\\','/')
        pathyun='otherfile/old'+line.strip()
        print localurl
        print pathyun
        result = bucket.put_object_from_file(pathyun, localurl)
        sql = "insert into log.dbo.file_other (oldurl,fileurl,ismod,bucket,intime,filetype) VALUES ('%s','%s',0,'instrumentother','%s','old') " \
              % (localurl.encode("utf8"), pathyun.encode("utf8"), time.strftime("%Y-%m-%d %X", time.localtime()))
        print sql
        ms.ExecNonQuery(sql)




def walk_dir(dir,parrm,topdown=True):
    w = 0
    fileinfo = open('otherList.txt', 'a')
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            try:
                w += 1
                print(os.path.join(name))
                url = os.path.join(root,name)
                print url
                upfile(url)
                fileinfo.write(url+'\n')
            except Exception, e:
                print Exception, ":", e
                f = open('otherlisterror.txt', 'a')
                f.write(url + '\n')
                f.close()
                pass
        # for name in dirs:
        #     print(os.path.join(name))
        #     fileinfo.write(' '+ os.path.join(root,name)+'\n')
    fileinfo.close()
    return w



if __name__=='__main__':

    walk_dir(dir,parrm)