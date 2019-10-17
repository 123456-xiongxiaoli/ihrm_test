"""
组织测试套件，执行测试用例
"""
#导包
import time

from case.test_login import IhrmTest


from tools.HTMLTestRunner import HTMLTestRunner
import unittest


#实例化测试套件对象
suite=unittest.TestSuite()
#添加测试用例到测试套件
suite.addTest(unittest.makeSuite(IhrmTest))
#定义文件路径和文件名
file_path="./report/report.html"
#打开文件流
with open(file_path,"wb") as f:

    #实例化HTMLTestRunner对象
    runner_test=HTMLTestRunner(f,title="人力资源测试报告",description="Chrome")
    #执行测试套件
    runner_test.run(suite)

