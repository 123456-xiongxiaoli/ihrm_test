"""
组织测试套件，执行测试用例
"""
#导包
import time
import unittest
from BeautifulReport import BeautifulReport

#实例化测试套件对象
from case.test_emp import TestEmployee
from case.test_login import IhrmTest
suite=unittest.TestSuite()
#添加测试用例到测试套件
suite.addTest(IhrmTest("test_login_success"))
suite.addTest(TestEmployee("test_add_emp"))
# suite.addTest(TestEmployee("test_updata_emp"))
# suite.addTest(TestEmployee("test_find_emp"))
# suite.addTest(TestEmployee("test_dele_emp"))



#定义执行对象
runner=unittest.TextTestRunner()
runner.run(suite)


