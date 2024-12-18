def getText():  # 定义一个函数
    txt = open('hamlet.txt', 'r').read()  # 变量赋值给txt，打开并阅读hamlet.txt文件
    txt = txt.lower()  # 阅读时文件字母为小写
    for ch in '@"#%&()*+,-./:;<=>?@[\\]^_‘{|}~':  # 遍历这些特殊符号
        txt = txt.replace(ch," ")  # 将特殊符号改为空格
    return txt  # 返回txt
# 上面的部分是定义一个getText的函数
hamletTxt = getText()  # 将桑面这个定义函数复制给hamletTxt
words = hamletTxt.split()  # 将分割后的列表赋值给words
counts = {}  # 创建一个空字典
for word in words:  # 遍历words，用word表示遍历的每一步
    counts[word] = counts.get(word,0) + 1  # 定义一个键值对，用于检查字典中单词出现的次数
items = list (counts.items())  # 使用items函数，将键和值以列表的形式表示，并赋值给items
items.sort(key=lambda x:x[1],reverse=True)  # 排序列表的结果
for i in range(10):  # 遍历1~10
    word,count = items[i]  # 将遍历的结果赋值给word,count，因为有两个结果，word是前面的，count是后面的
    print("{0:<10}{1:>5}".format(word,count))  # 按格式打印结果