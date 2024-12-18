score = eval(input('请输入：'))
if score <= 60:
    grade = 'D'
elif 61 <= score <= 75:
    grade = 'C'
elif 76 <= score <= 90:
    grade = 'B'
elif score >= 91:
    grade = 'A'
print('你的输入级别是{}'.format(grade))