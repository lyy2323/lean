import jieba
a = jieba.lcut('中华人民共和国是一个伟大的国家')  # 精确模式，返回一个列表类型的分词结果
b = jieba.lcut('中华人民共和国是一个伟大的国家',cut_all=True)  # 全模式，发牛一个列表类型的分词结果，存在冗余
c = jieba.lcut_for_search('中华人民共和国是一个伟大的国家')  # 全模式，返回一个列表类型的分词结果，存在冗余
print(a)
print(b)
print(c)
