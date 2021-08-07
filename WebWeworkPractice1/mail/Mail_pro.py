import zmail

from WebWeworkPractice1.mail.readreport import NewReport


class Mail(NewReport,Yaml):

    """后去最新测试报告"""
    report_path = NewReport().report()
    # 实例化yaml文件对象
    yaml = Yaml().read_yaml()
    # 分别取yaml文件内的值
    send_mail = yaml["mail"]["send_mail"]
    receive_mail = yaml["mail"]["receive_mail"]
    mail_code = yaml["mail"]["mail_code"]

    def mail(self):
        """发送邮件"""
        mail = {
            "subject": 'web自动化测试报告',
            "content_html": '报告详情查看附件',
            "attachments": self.report_path
        }

        server = zmail.server(self.send_mail,self.mail_code)
        # 如果有多个收件人，则用列表
        server.send_mail(self.receive_mail,mail)