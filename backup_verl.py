
# 压缩成zip文件
from zipfile import *   #@UnusedWildImport
import os
 
my_dir = 'd:/xiaxia/'
myzip = ZipFile('d:/xiaxia.zip', 'w', ZIP_DEFLATED)
for file_name in os.listdir(my_dir):
    file_path = my_dir + file_name
    print(file_path)
    myzip.write(file_path)
myzip.close()
 
print('finished')
 
# 从zip 文件中读取数据
# 直接检查一个zip格式的归档文件中部分或所有的文件，同时还要避免将这些文件展开到磁盘上
my_zip = ZipFile('d:/xiaxia.zip')
for file_name in my_zip.namelist():
    print('File:', file_name, end = ' ')
    file_bytes = my_zip.read(file_name)
    print('has ', len(file_bytes), ' bytes')
 
#该代码片段来自于: http://www.sharejs.com/codes/python/6048
