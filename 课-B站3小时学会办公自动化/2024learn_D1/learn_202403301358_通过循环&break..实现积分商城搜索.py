import requests

print("开始")
while True:  # 'true' 改为 'True'
    key = input("请输入关键字：")
    if key == "q" or key == "Q":  # 在这一行末尾添加 ':'
        break
    res = requests.post(
        url="https://jf.10086.cn/cmcc-web-shop/search/query",
        data={
            "firstKeyword": key,
            "integral": None,
            "pageNum": 1,
            "pageSize": 60,
            "province": None,
            "sortColumn": "default",
            "sortType": "DESC"
        },
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/123.0.0.0 Safari/537.36"
        }
    )
    print(res.json())
print("结束")
