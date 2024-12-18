# 将字符间的空格（无论是空格还是其他任何字符），都将改为“,”，txt文件中是“中国 美国 英国 日本”
f = 'fname.txt'  # 定义文件名
file = open(f,encoding='utf-8')
t = file.read()   # 打开文件
ls = t.split()   # 将读取的内容分割成单词列表
file.close()     # 关闭文件
print(ls)

# 将字符间的"$"，都将改为“,”，txt文件中是“中国 美国 英国 日本”
f = 'fname.txt'  # 定义文件名
file = open(f,encoding='utf-8')
t = file.read()   # 打开文件
ls = t.split("$")   # 将读取的内容分割成单词列表
file.close()     # 关闭文件
print(ls)

ls = ['中国', '美国', '意大利']
with open('fnam.csv', 'w', encoding='utf-8') as f:  # 使用with语句自动管理文件关闭，并指定编码
    for item in ls:
        f.write(item + '\n')  # 直接写入国家名，并在每个国家名后添加换行符

ls = [[1,2],[3,4],[5,6]]
for row in ls:
    for column in row:
        print(column)

import wordcloud
c = wordcloud.WordCloud()
c.generate('wordcloud boy boy boy boy boy boy python')
c.to_file('pywordcloud.png')