import os
os.system('C:\\Windows\\System32\\calc.exe')  # 打开系统中的程序,计算机
os.chdir('D:')  # 修改当前程序操作的路径
os.getcwd()  # 返回程序的当前路径
os.getlogin()  # 获得当前系统登录用户名称
os.cpu_count()  # 获得当前系统的CPU数量
os.urandom(10)  # 获得10个（或n个）字节长度的随机字符串，通常用于加解密运算