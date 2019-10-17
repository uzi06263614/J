"""
编写unittest有关实现
"""
# 导包
import json
import unittest
import requests

from Test_TPshop import app
from Test_TPshop.api.user_api import UserLogin
# 参数化步骤1，导包
from parameterized import parameterized


def read_json():
    data = []
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8")as f:
        for value in json.load(f).values():
            # print("value=",value)
            username = value.get("username")
            password = value.get("password")
            verify_code = value.get("verify_code")
            status = value.get("status")
            msg = value.get("msg")
            ele = (username, password, verify_code, status, msg)
            data.append(ele)
    # 返回列表
    return data


# 创建测试类
class TestUser(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        self.session = requests.Session()
        self.user_login = UserLogin()

    # 资源销毁函数
    def tearDown(self):
        self.session.close()

    # 测试函数1：获取验证码
    def test_get_verify_code(self):
        # 1.请求业务
        # 创建UserLogin对象
        # 调用get_verify_coode函数
        response = self.user_login.get_verify_coode(self.session)
        # 断言业务
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))

    # 测试函数2：登录
    def test_login_succes(self):
        # 1.请求业务
        # 调用get_verify_coode函数
        response1 = self.user_login.get_verify_coode(self.session)
        # 调用login函数
        response2 = self.user_login.login(self.session, "13499999999", "123456", "8888")
        print(response2.json())
        # 断言业务
        # 函数3：以参数化的方式读取测试数据然后执行登录

    """
    参数化：动态的生成或导入数据
    流程：
        1.导包
        2.定义一个获取数据的函数
        3.测试函数声明
    """

    @parameterized.expand(read_json())
    def test_login(self, username, password, verify_code, status, msg):
        print("-" * 100)
        # print(username, password, verify_code, status, msg)
        # 1.请求业务
        # 调用api包下对象的相关函数
        # 1.1获取验证码
        response1 = self.user_login.get_verify_coode(self.session)
        # 1.2执行登陆
        response2 = self.user_login.login(self.session, username, password, verify_code)
        # 2.断言
        print(response2.json())
        self.assertEqual(status, response2.json().get("status"))
        self.assertIn(msg, response2.json().get("msg"))
