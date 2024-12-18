n = eval(input('请输入：'))
for i in range(1,n+1,2):
    print('{1:^{1}}'.format('*'*i,n))