height, weight = eval(input())
bmi = weight / pow(height ,2)
print('BMI数值为：{:.2f}'.format(bmi))
chi, nal = '',''
if bmi < 18.5:
    chi, nal = '偏瘦', '偏瘦'
elif 18.5 <= bmi <24:
    chi, nal = '正常', '正常'
elif 24 <= bmi < 25:
    chi, nal = '偏胖', '正常'
elif 25 <= bmi < 28:
    chi, nal = '偏胖', '偏胖'
elif 28 <= bmi < 30:
    chi, nal = '肥胖', '偏胖'
else:
    chi, nal = '肥胖', '肥胖'
print('BMI指标为：国际{0},国内{1}'.format(nal,chi))