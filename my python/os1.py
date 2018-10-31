#os模块
import os
#getcwd:获取当前的工作目录
#格式：os.getcwd()
mydir = os.getcwd()
print(mydir)
#chdir:改变当前工作路径
#格式；os.chdir('路径')
mydir = os.chdir('C:/Users/Administrator/Desktop/sound')
print(mydir)
#listdir:获取一个目录中的所有子目录和文件的名称列表
#格式；os.listdir('路径')
name = os.listdir('C:\\Users\\Administrator\\Desktop\\my python')
print(name)