# -*- coding: utf-8 -*-
'''
查询仪器信息网专场图片
'''
import oss2
import mssql
import time
auth = oss2.Auth('ya3W80ebpSx4ihkE', 'G44HC54wdOLCtl4m2adZWXOvgQDeoG')
bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'instrumentnetshow')

ms = mssql.MSSQL()
#查询专场的图片
def selzc():
    paperfile="SELECT id,NameID FROM IM_SortClass WHERE IMType LIKE 'C%' AND ISZC=1"
    productlist = ms.ExecQuery(paperfile)
    fileinfo = open('zclistID.txt', 'a')
    for NameID in productlist:
        listimage=NameID[1]


        fileinfo.write(str(NameID[0]) + '\n')
    fileinfo.close()
#去oss比对专场的图片
def chosszc():

    fileinfo = open(r'zclistID.txt', 'r')
    filepic = fileinfo.readlines()
    dir =[]
    for strpic in filepic:
        urlpp= '17img'+strpic
        urlpp=urlpp.strip()
        pinstr = urlpp.split('.')[1]
        if pinstr not in dir:
         dir.append(pinstr)
         print pinstr

        exist = bucket.object_exists(urlpp)

        if exist:
            #print('object exist')
            pass
        else:
            print strpic
    print dir
if __name__=='__main__':
    selzc()