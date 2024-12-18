import jieba
f = open('沉默的羔羊.txt',encoding='utf-8')
ls = jieba.lcut(f.read())
d = {}
for w in ls:
    if len(w) >= 2:
        d[w] = d.get(w, 0) + 1
maxc = 0
maxw = ""
for k in d:
    if d[k] > maxc:
        maxc = d[k]
        maxw = k
    elif d[k] == maxc and k > maxw:
        maxw = k
print(maxw,maxc)
f.close()