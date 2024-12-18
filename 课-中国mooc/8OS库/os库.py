import os.path  # path：针对系统的路径操作管理
os.path.abspath('file.txt')  # 返回path再当前系统中的绝对路径
os.path.normpath('E://办公文件//file.txt')  # 归一化path的表示形式，统一用\\分割路径
os.path.relpath('E://办公文件//file.txt')  # 返回当前程序与文件之间的相对路径
os.path.dirname('E://办公文件//file.txt')  # 返回path中的目录名称
os.path.basename('E://办公文件//file.txt')  # 返回path中最后的文件名称
os.path.join('E:/','E://办公文件//file.txt')  # 组合path与paths，返回一个路径字符串
os.path.exists('E://办公文件//file.txt')  # 判断path对应文件或目录是否存在，返回True或False
os.path.isfile('E://办公文件//file.txt')  # 判断path所对应是否为已存在的文件，返回True或False
os.path.isdir('E://办公文件//file.txt')  # 判断path所对应是否为已存在的目录，返回True或False
os.path.getatime('E://办公文件//file.txt')  # 返回path对应文件或目录上一次的访问时间
os.path.getmtime('E://办公文件//file.txt')  # 返回path对应文件或目录最近一次的修改时间
os.path.getctime('E://办公文件//file.txt')  # 返回path对应文件或目录的创建时间
os.path.getsize('E://办公文件//file.txt')  # 返回path对应文件的大小，以字节为单位
