# 文件打开模式：
# 1、默认文本形式，只读模式、默认值
f = open('测试.txt', encoding='utf-8')
content = f.read()
print(content)
f.close()

# 文本形式、只读模式、同默认值（如上面的，就默认为这种）
f = open('测试.txt', 'rt', encoding='utf-8')
content = f.read()
print(content)
f.close()

# 文本形式覆盖写模式
f = open('测试.txt', 'w', encoding='utf-8')
content = f.write('we are big,我是对的')
print(content)
f.close()

# 文本形式、追加写模式+读取文件
with open('测试.txt', 'a+', encoding='utf-8') as f:
    content = f.write('are you ok? 你好吗？\n')
print(content)
f.close()

#其他打开形式：
# 文本形式，创建新模式：f = open('f.txt', 'x')
# 二进制模型是，只读模式：f = open('f.txt', 'b')
# 二进制形式，覆盖写模式：f = open('f.txt', 'wb')