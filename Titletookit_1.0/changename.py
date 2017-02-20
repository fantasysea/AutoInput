# -*- coding:utf-8 -*-

import os;
def rename():
    path='D:\\pl\\alibaba\\mainpics';
    for parent, dirnames, filenames in os.walk(path):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:  # 输出文件信息
            print "parent is:" + parent
            print "filename is:" + filename
            print "filename 0-8 is " + filename[0:8]
            print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            os.renames(os.path.join(parent, filename),
                               os.path.join(parent, filename.replace(filename[0:8], filename[0:8]+'SW')))

if __name__ == '__main__':
    rename()