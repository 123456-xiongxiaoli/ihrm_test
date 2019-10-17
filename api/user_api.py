"""
封装登陆ihrm业务操作
"""
# 定义操作类
from app import IHRM_URL


class LoginIhrm:
    # 定义业务操作方法
    # 登陆操作
    def login(self, session,mobile,password):
        data = {
            "mobile": mobile,
            "password": password
        }
        # session.post(url="",json="")
        return session.post("http://182.92.81.159/api/sys/login", json=data)
