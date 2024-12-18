# 定义函数
def send_email(to, subject, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 邮件发送者和接收者
    sender = 'lyf@njpepsi.com'
    receivers = ['18936388511@163.com']

    # 创建 MIMEText 对象
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("发件人名称", 'utf-8')
    message['To'] = to
    message['Subject'] = Header(subject, 'utf-8')

    # 通过SSL方式发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)  # 使用SMTP_SSL连接端口465
        smtpObj.login(sender, 'D8z7KSLu2URCAVuK')  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送邮件
        smtpObj.quit()  # 关闭连接
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: 无法发送邮件")


# 执行函数：
em_to = input("请输入邮箱地址：")
em_sub = input("请输入主题：")
em_txt = input("请输入正文：")
send_email(em_to, em_sub, em_txt)
