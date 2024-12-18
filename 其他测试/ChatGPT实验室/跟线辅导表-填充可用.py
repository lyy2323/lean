import pandas as pd
from openpyxl import load_workbook

try:
    source_file_path = r"E:\SynologyDrive\Drive\24年\桌面-临时\跟线辅导表--自用\4月用\客户经销商信息20240412100623680516.xlsx"
    df = pd.read_excel(source_file_path, sheet_name='sheet1')
    columns_to_extract = ['客户名称', '订单额', '冰箱数量', '客户编码', '渠道类型', '上级经销商编码', '安排线路',
                          '大区', '营业所', 'TDS', 'CR', '小区号']
    data_to_insert = df[columns_to_extract]
    template_path = r"E:\SynologyDrive\Drive\24年\桌面-临时\跟线辅导表--自用\4月用\新的.xlsx"

    with pd.ExcelWriter(template_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        data_to_insert.to_excel(writer, sheet_name="Template", startrow=1, index=False, header=False)

    print("数据已成功填充至模板文件。")

except Exception as e:
    print("An error occurred:", e)
