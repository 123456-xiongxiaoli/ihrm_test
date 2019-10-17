# 导包
import json
import unittest
from log import print_Log
import logging
import requests
from parameterized import parameterized

import app
from api.user_api import LoginIhrm
from app import PATH

# 定义测试类
# 定义参数化
def obj_data():
    # 定义空列表
    data1 = []
    # 打开文件流
    with open(PATH+"/data/login_data.json",encoding="utf-8") as f:
        # 加载文件内容
        data2 = json.load(f)
        # print(data2)
        # 读取数据组装成元组，追加到列表内
        for i in data2.values():
            # print(i)
            data1.append((i.get("mobile"),
                          i.get("password"),
                          i.get("success"),
                          i.get("code"),
                          i.get("message")
                          ))
    # 返回列表
    # print(data1)
    return data1
# obj_data()
class IhrmTest(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.session = requests.Session()
        # 实例化api对象
        self.login_ihrm = LoginIhrm()

    # 销毁方法
    def tearDown(self):
        self.session.close()

    # 定义测试函数
    @parameterized.expand(obj_data())
    def test_ihrm_login(self, mobile, password,success,code,message):
        # 业务
        # 登陆ihrm系统
        # print_Log()
        # try:
        reponse1 = self.login_ihrm.login(self.session, mobile, password)
        print(reponse1)

        # 断言
        self.assertEqual(code,reponse1.json().get("code"))
        self.assertEqual(message,reponse1.json().get("message"))
        # except:
        #     logging.error("测试用例，登陆函数出现错误")

    #仅登陆成功（正向数据）
    def test_login_success(self):
        #调用登陆函数
        response3=self.login_ihrm.login(self.session,"13800000002","123456")
        #断言
        self.assertEqual(10000, response3.json().get("code"))
        self.assertEqual("操作成功！", response3.json().get("message"))
        token=response3.json().get("data")
        print("登陆成功令牌",token)
        app.TOKEN_LOGIN=token


