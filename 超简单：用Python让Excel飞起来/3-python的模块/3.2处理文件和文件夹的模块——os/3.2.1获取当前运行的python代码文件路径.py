"""
getcwd()函数
不接受任何实参，可获取当前运行的python文件的绝对路径
getcwd 是英文短语 "get current working directory"（获取当前工作目录路径）的缩写。
"""
import os
path = os.getcwd()
print(path)

"""
listdir()
实参是路径或路径的变量，可将实参路径下的文件和文件夹显示在列表中
listdir是"list directory“（列出目录）的缩写，
"""
import os
path = "E:\办公文件\SynologyDrive\桌面-临时\跟线辅导表\分月"
file_list = os.listdir(path)
print(file_list)

"""
splitext()
实参是文件名，可分离改文件的文件名和扩展名
splitext是“split extension”（分离扩展）的缩写
由于其在os模块的path子模块中，所以使用时需要前面加.path.splitext()
"""
import os
path = "报备客户.xlsx"
separate = os.path.splitext(path)
print(separate)

"""
rename(src, dst)
src是重命名前的文件或文件夹名，dst是新的命名
该函数不仅用于修改文件名，也可以修改文件路径（移动到新的位置）
如果重命名文件夹，只能重命名最后一级的文件夹
"""
import os
oldname = "报备客户.xlsx"  # 原文件名
newname = "报备客户.xlsx"  # 新的名字
os.rename(oldname, newname)