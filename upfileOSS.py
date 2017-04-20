#encoding:utf8
import sys
import string, os, sys

import oss2

reload(sys)
sys.setdefaultencoding('utf8')

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'ya3W80ebpSx4ihkE')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'G44HC54wdOLCtl4m2adZWXOvgQDeoG')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'instrumentnetshow')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'http://oss-cn-beijing.aliyuncs.com')
# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)


dir="E:\\upload"
f = open(r'imagefile.txt','rb')  #首先先创建一个文件对象
fr = f.readlines()  #用readline()方法读取文件的一行内容
for line in fr:
    print line
    oldurl=line.replace('/',"\\")
    localurl=dir+oldurl.strip()
    pathyun='17img'+line.strip()
    result = bucket.put_object_from_file(pathyun, localurl)
#localurl=r'E:\upload\images\201702\Brand\201721516522.jpg'
#pathyun='17img/images/201702/Brand/201721516522.jpg'
print localurl
print pathyun
result = bucket.put_object_from_file(pathyun, localurl)
print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   # print result
#f.close()