# 打开文件
f = open(r"E:\办公文件\SynologyDrive\24年\工作周记\我的周记\南京百事工作周记0102-0107-刘应峰.docx", mode="r", encoding="latin1")
#读取文件
data = f.read()
# 关闭文件
f.close()
# 输出文件内容
print(data)
