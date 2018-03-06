#encoding:utf-8 # 支持中文输入
import re
import os
s = os.sep

##获取当前工作目录
root = os.path.abspath('.')
#需要忽略的文件后缀
ignoredTrail = [".py"]
#需要忽略的文件夹
ignoredDirPath   = ["/Users/liyingchun/Downloads/test/Test"]
#原来的前缀
oldPrefix="xxx_" 
#新前缀
newPrefix="yyy_" 

#获取文件名和后缀
def getFileNameAndExt(filename):
 (filepath,tempfilename) = os.path.split(filename);
 (shotname,extension) = os.path.splitext(tempfilename);
 return shotname,extension

#是否是需要根据后缀忽略的文件
def isIgnoredByTrail(filePath):
  file = getFileNameAndExt(filePath)
  for trail in ignoredTrail:
    if file[1] == trail:
      print "忽略文件:" + filePath
      return bool(1)
  return bool(0)
  
#是否根据文件夹路径葫芦
def isIgnoredByDirPath(dirpath):
  for path in ignoredDirPath:
    if dirpath == path:
      print "忽略目录：" + path
      return bool(1)
  return bool(0)

#获取所有文件名
def getAllFiles(path):
 allfile=[]
 for dirpath,dirnames,filenames in os.walk(path):
  
  if isIgnoredByDirPath(dirpath):
    continue
  for dir in dirnames:
   allfile.append(os.path.join(dirpath,dir))
  for name in filenames:
   allfile.append(os.path.join(dirpath, name))
 return allfile

#重命名
def rename(oldName,newName,filePath):
  a = open(filePath,'r') #打开所有文件
  str = a.read()

  str = str.replace(oldName,newName)#将字符串里前面全部替换为后面
  b = open(filePath,'w')
  b.write(str) #再写入
  b.close() #关闭文件
  print "============" + filePath + "finished"


fileList = getAllFiles(root)
for file in fileList:
  if os.path.isfile(file):
    if isIgnoredByTrail(file):
      continue
    rename(oldPrefix,newPrefix,file)


