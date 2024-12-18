import pandas as pd

# 读取 "文件一" 的 sheet1
df = pd.read_excel('E:\新建文件夹\跟线辅导辅助表-3月用.xlsx', sheet_name='辅导清单')

# 创建数据透视表
pivot_table = df.pivot_table(values='2月销额', index='TDS', aggfunc='sum')

# 将数据透视表的数值取整
pivot_table = pivot_table.astype(int)

# 将数据透视表的结果写入 "文件二"
pivot_table.to_excel('E:\新建文件夹\汇总.xlsx', sheet_name='区域汇总')
