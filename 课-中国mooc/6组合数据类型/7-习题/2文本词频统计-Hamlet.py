def getText():
    txt = open('hamlet.txt','r').read()
    txt = txt.lower()
    for ch in "#$%&()*+,-./:;<=>?@[\]^_‘{|}~'":
        txt = txt.replace(ch, ' ')
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    # print(word)  # 打印排名前10的单词，但不显示数量
    print('{0:<10}{1:>5}'.format(word,count))