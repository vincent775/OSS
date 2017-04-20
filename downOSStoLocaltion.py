# -*- coding: utf-8 -*-
#下载oss文件到本地

import oss2
import shutil
import os
import threading,thread
from time import ctime,sleep
prefix = True;

auth = oss2.Auth('ya3W80ebpSx4ihkE', 'G44HC54wdOLCtl4m2adZWXOvgQDeoG')
bucketshow = oss2.Bucket(auth, 'oss-cn-beijing-internal.aliyuncs.com', 'instrumentnetshow')
bucketbbs = oss2.Bucket(auth, 'oss-cn-shanghai-internal.aliyuncs.com', 'instrumentbbs')
bucketpaper = oss2.Bucket(auth, 'oss-cn-shanghai-internal.aliyuncs.com', 'instrumentfile')

def managershow(q):
    x=0
    y=0
    for obj in oss2.ObjectIterator(bucketshow,prefix='17img'):
        try:
            filename=obj.key;
            if is_prefix(filename):  # 文件夹
                #print('directory: ' + filename)
                #判断文文件夹是否存在
                #print os.path.isdir('/data/oss/'+filename);
                if(os.path.isdir('/data/oss/'+filename)):
                    pass
                else:
                   os.mkdir('/data/oss/'+filename)
            else:  # 文件
                #print('file: ' + obj.key)
                fileurl= filename.replace(filename.split('/').pop(), '')
                fileurllocal = '/data/oss/' + fileurl;
                filenamelocal = '/data/oss/' + filename;
                #print filenamelocal
                #判断文件是否存在
                if not os.path.exists(fileurllocal):  ##目录存在，返回为真
                    os.makedirs(fileurllocal)
                    #print u"create prefix"
                if not os.path.isfile(filenamelocal):
                    x+=1
                    #print u"/////download"
                    bucketshow.get_object_to_file(filename, filenamelocal)
                else:
                    y+=1
                    #print u"pass"
        except:
            pass
    print "show : download-%s ,pass-%s" % (str(x),str(y))
def managerpaper(q):
    x = 0
    y = 0
    for obj in oss2.ObjectIterator(bucketpaper, prefix='paperfiles'):
        try:
            filename = obj.key;
            if is_prefix(filename):  # 文件夹
                #print('directory: ' + filename)
                # 判断文文件夹是否存在
                #print os.path.isdir('/data/oss/' + filename);
                if (os.path.isdir('/data/oss/' + filename)):
                    pass
                else:
                    os.mkdir('/data/oss/' + filename)
            else:  # 文件
                # print('file: ' + obj.key)
                fileurl = filename.replace(filename.split('/').pop(), '')
                fileurllocal = '/data/oss/' + fileurl;
                filenamelocal = '/data/oss/' + filename;
                #print filenamelocal
                # 判断文件是否存在
                if not os.path.exists(fileurllocal):  ##目录存在，返回为真
                    os.makedirs(fileurllocal)
                    #print u"create prefix"
                if not os.path.isfile(filenamelocal):
                    x+=1
                    #print u"/////download"
                    bucketpaper.get_object_to_file(filename, filenamelocal)
                else:
                    y+=1
                    #print u"pass"
        except:
            pass
    print "paper : download-%s ,pass-%s" % (str(x), str(y))
def managerbbs(q):
    x = 0
    y = 0
    for obj in oss2.ObjectIterator(bucketbbs, prefix='bbsfiles'):
        try:
            filename = obj.key;
            if is_prefix(filename):  # 文件夹
                #print('directory: ' + filename)
                # 判断文文件夹是否存在
                #print os.path.isdir('/data/oss/' + filename);
                if (os.path.isdir('/data/oss/' + filename)):
                    pass
                else:
                    os.mkdir('/data/oss/' + filename)
            else:  # 文件
                # print('file: ' + obj.key)
                fileurl = filename.replace(filename.split('/').pop(), '')
                fileurllocal = '/data/oss/' + fileurl;
                filenamelocal = '/data/oss/' + filename;
                #print filenamelocal
                # 判断文件是否存在
                if not os.path.exists(fileurllocal):  ##目录存在，返回为真
                    os.makedirs(fileurllocal)
                    #print u"create prefix"
                if not os.path.isfile(filenamelocal):
                    x+=1
                    #print u"/////download"
                    bucketbbs.get_object_to_file(filename, filenamelocal)
                else:
                    y+=1
                    #print u"pass"
        except:
           pass
    print "bbs : download-%s ,pass-%s" % (str(x), str(y))
 #判断是不是文件夹
def is_prefix(str):
   if(str[-1]=='/'):
      prefix = True;
   else:
      prefix = False;
   return prefix;



if __name__ == "__main__":
    try:
        print "Start time %s" % ctime()
        threads = []
        t1 = threading.Thread(target=managershow, args=(1,))
        threads.append(t1)
        t2 = threading.Thread(target=managerbbs, args=(2,))
        threads.append(t2)
        t3 = threading.Thread(target=managerpaper, args=(3,))
        threads.append(t3)
        for t in threads:
            t.setDaemon(True)
            t.start()
        for t in threads:
            t.join()
        print "End time %s" % ctime()
        print "-------------------------"

       #managershow()
       #managerbbs()
       #managerpaper()
    except:
        threads.exit()
        print "Error: unable to start thread"

