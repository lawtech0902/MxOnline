# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/3/7 下午7:58'
"""

from users.models import EmailVerifyRecord
from MxOnline.settings import DEFAULT_FROM_EMAIL

from random import Random
from django.core.mail import send_mail


# 生成随机字符串
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = u"慕学在线网注册激活链接"
        email_body = u"请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email], fail_silently=False)
        if not send_status:
            pass

    elif send_type == 'forget':
        email_title = u"慕学在线网重置密码链接"
        email_body = u"请点击下面的链接重置密码: http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email], fail_silently=False)
        if not send_status:
            pass

    elif send_type == 'update_email':
        email_title = u"慕学在线网邮箱修改验证码"
        email_body = u"你的邮箱验证码为：{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email], fail_silently=False)
        if not send_status:
            pass
