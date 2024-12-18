import pandas as pd
from openpyxl import load_workbook

# 路径到您的模板文件
template_path = 'E:\新建文件夹\汇总.xlsx'
# 路径到您的数据文件
data_path = 'E:\新建文件夹\跟线辅导辅助表-3月用.xlsx'

# 读取数据
df = pd.read_excel(data_path, sheet_name='辅导清单')

# 创建数据透视表
pivot_table = df.pivot_table(values='2月销额', index='TDS', aggfunc='sum')

# 在追加模式下使用 ExcelWriter，尝试保留现有工作表
with pd.ExcelWriter(template_path, engine='openpyxl', mode='a') as writer:
    # 如果 'Pivot' 工作表已存在，这将会在追加模式下失败
    # 因为 Pandas 无法在追加模式下覆盖或删除现有的工作表
    # 所以我们希望在追加之前，手动检查并删除已存在的 'Pivot' 工作表
    # 这部分逻辑需要在使用 ExcelWriter 之前进行
    pivot_table.to_excel(writer, sheet_name='区域')

# 注意：由于使用了with语句，所以文件会在离开该语句块时自动保存
