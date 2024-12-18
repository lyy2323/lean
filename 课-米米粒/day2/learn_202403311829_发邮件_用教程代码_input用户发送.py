# 定义函数
def send_email(to, subject, content):
    # 1.将python内置的模块（功能导入）
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    # 2.构建邮件内容
    msg = MIMEText(content, "html", "utf-8")  # 内容
    msg["From"] = formataddr(["刘邦", "lyf@njpepsi.com"])  # 自己的名字和邮箱
    msg["to"] = to  # 目标邮箱
    msg["subject"] = subject  # 主题

    # 3. 发送邮件
    server = smtplib.SMTP_SSL("smtp.exmail.qq.com")
    server.login("lyf@njpepsi.com", "D8z7KSLu2URCAVuK")
    # 自己邮箱、目标邮箱
    server.sendmail("lyf@njpepsi.com", to, msg.as_string())
    server.quit()


# 执行函数
em_to = input("请输入邮箱：")
em_sub = input("请输入标题：")
em_con = input("请输入正文：")

send_email(em_to, em_sub, em_con)
