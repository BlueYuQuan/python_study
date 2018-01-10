# -*- coding: utf-8 -*-
import os  # 引入文件操作库
import shutil #执行文件的复制移动包
"""
#遍历文件夹下所有文件和文件夹
#如果是空文件夹则删除
#如果不是空文件夹，则将文件夹下的所有文件移动到顶层文件夹下，并删除该文件夹
#如果是文件，如果文件为空，则删除
#如果文件不为空，则移动到顶层文件夹下
"""

def deldir(path,topPath):
    """
    清理空文件夹和空文件
    param path: 文件路径，检查此文件路径下的子文件
    param topPath:顶层文件夹
    """

    print ('*'*30)
    try:
        files = os.listdir(path)  # 获取路径下的子文件(夹)列表
        #print (files)
        for file in files:
            #print ('遍历路径：'+os.fspath(path +'/'+ file))
            if os.path.isdir(os.fspath(path+'/'+file)):  # 如果是文件夹
                #print (file+'是文件夹')
                if not os.listdir(os.fspath(path+'/'+file)):  # 如果子文件为空
                    #print (file+'是空文件夹,即将执行删除操作')
                    os.rmdir(os.fspath(path+'/'+file))  # 删除这个空文件夹
                    
                else:
                    #print (file+'不是空文件夹')
                    deldir(os.fspath(path+'/'+file),topPath) # 遍历子文件
                    if not os.listdir(os.fspath(path+'/'+file)):  # 如果子文件为空
                        print (file+'是空文件夹,即将执行删除操作')
                        os.rmdir(os.fspath(path+'/'+file))  # 删除这个空文件夹
                        
            elif os.path.isfile(os.fspath(path+'/'+file)):  # 如果是文件
                print(file+'是文件')
                if os.path.getsize(os.fspath(path+'/'+file)) == 0:  # 文件大小为0
                    print(file+'是空文件，即将执行删除操作！')
                    os.remove(os.fspath(path+'/'+file))# 删除这个文件
                else:
                    try:
                        #os.rename(file.name(),file.name()+"jpg")
                        #print(file+'不是空文件，即将执行移动到top操作！')
                        shutil.move(os.fspath(path+'/'+file),topPath)
                    except shutil.Error:
                        print('文件重名！即将执行重命名操作')
                   
        #return
    except FileNotFoundError:
        print ("文件夹路径错误")


if __name__ == "__main__":  # 执行本文件则执行下述代码
    path = input("Please input the files path:")  # 输入路径
    deldir(path,path)
    #print(dirnumofdeld)
    #print(filenumofdeld)




'''
print (os.path.basename(file)) #当前文件（夹）名
print (os.path.dirname(file))
print(os.path.realpath(file))    # 当前文件的路径
print(os.path.dirname(os.path.realpath(file)))  # 从当前文件路径中获取目录（不包括该文件）
print(os.path.basename(os.path.realpath(file))) # 从当前文件路径中获取文件名（单纯的文件名）


结果：
新建文件夹 (2)

E:\studysoft2\Python\Python36\code\新建文件夹 (2)
E:\studysoft2\Python\Python36\code
新建文件夹 (2)
'''
