"""
测试员工模块的增删改查接口

"""
# 导包
import unittest


# 创建测试类
import requests

from api.emp_api import EmployeeTest


class TestEmployee(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        self.session=requests.Session()
        self.emp_test=EmployeeTest()

    # 资源销毁函数
    def tearDown(self):
        pass

    # 测试函数1：增
    def test_add_emp(self):
        #增加业务
        response = self.emp_test.add_emp(self.session,"小熊rdh","16888691064","9000875698")
        #断言业务
        print("添加成功结果：",response.json())



    # 测试函数1：改
    def test_updata_emp(self):
        response1 = self.emp_test.updata_emp(self.session,"1184400337775448064","楼忒1314")
        print(response1.json())
    # 测试函数1：查
    def test_find_emp(self):
        response2 = self.emp_test.find_emp(self.session, "1184400337775448064")
        print("查询结果：",response2.json())
    # 测试函数1：删
    def test_dele_emp(self):
        response3 = self.emp_test.del_emp(self.session, "1184400337775448064")
        print("删除结果：",response3.json())