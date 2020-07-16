import os
import time



'''
获得当前文件所在目录
'''
path=os.getcwd()
print(path)


# folder=time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
'''
在当前文件夹生成文件夹，以时间命名
'''
# folder=time.strftime(r"%Y%m%d_%H%M%S",time.localtime())
# os.makedirs(r'%s/%s'%(os.getcwd(),folder))


'''
更改当前工作路径
'''
os.chdir('C:\\Users\\ASUS\\Desktop\\1')
path=os.getcwd()
print(path)



'''
判断一个路径是否存在
'''
path_yesno = os.path.exists('C:\\Users\\ASUS\\Desktop\\1')
print(path_yesno)


'''
获取目录中所有文件及文件夹list
'''
PATH = os.listdir('C:\\Users\\ASUS\\Desktop')
# print(PATH)



'''
创建和删除子目录
'''
# os.makedirs('C:\\Users\\ASUS\\Desktop\\2')
# os.rmdir('C:\\Users\\ASUS\\Desktop\\2')

path=os.getcwd()
print(path)



'''
改文件名
'''
os.rename('123.txt','000.txt')