import zmail


def test_send_mail():
    # 登录邮箱
    key = 'aqkvgrrolyxgbcic'
    server = zmail.server('cn.guozhichao@qq.com', key)
    server.send_mail('228354813@qq.com', {'subject': 'hello!', 'content_text': 'By zmail!'})


if __name__ == '__main__':
    test_send_mail()
