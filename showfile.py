# -*- coding: utf-8 -*-
'''
网展检测 本地upload的数量数目与oss 2017年2月14日09:31:43 之前上传数据对比
'''
import oss2
import py200
import sys,time
reload(sys)
sys.setdefaultencoding("utf-8")
#parrm= sys.argv[1]

x=0;y=0;z=0
auth = oss2.Auth('ya3W80ebpSx4ihkE', 'G44HC54wdOLCtl4m2adZWXOvgQDeoG')
bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'instrumentnetshow')
#files
for obj in oss2.ObjectIterator(bucket, prefix='17img/files'):
    print(obj.key);
    x += 1
print u"files文件：\n  oss %d ,本地 %d " % (x, 0)
#images
for obj in oss2.ObjectIterator(bucket, prefix='17img/images'):
    # print(obj.key)
    y += 1
print u"images文件：\n  oss %d ,本地 %d " % (y, py200.walk_dir(r'E:\upload\images'))
#old
for obj in oss2.ObjectIterator(bucket, prefix='17img/old'):
    # print(obj.key)
    z += 1
print u"old文件：\n  oss %d ,本地 %d " % (z, py200.walk_dir(r'E:\upload\old'))