import os

# 使用列表来存储库名
libs = ['pandas', 'numpy', 'matplotlib','PyPDF2']

try:
    for lib in libs:
        # 正确地拼接命令字符串
        os.system('pip install ' + lib)
    print('Successful')
except Exception as e:
    # 打印异常信息
    print('Failed Somehow', str(e))