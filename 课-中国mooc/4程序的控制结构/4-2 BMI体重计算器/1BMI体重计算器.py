height, weight = eval(input('请输入身高米与体重公斤（请用逗号隔开）：'))
bmi = weight / pow(height ,2)
print('你的BMI是：{0:*^20.2f}'.format(bmi))
cha, nat = '',''
if bmi < 18.5:
    cha, nat = '偏瘦', '偏瘦'
elif 18.5 <= bmi < 24:
    cha, nat = '正好', '正好'
elif 24 <= bmi < 25:
    cha, nat = '偏胖', '正好'
elif 25 <= bmi < 28:
    cha, nat = '偏胖', '偏胖'
elif 28 <= bmi < 30:
    cha, nat = '偏胖', '肥胖'
else:
    cha, nat = '肥胖', '肥胖'
print('BMI标准：在国内{0},在国际{1}'.format(cha, nat))