"""
封装case中所需要的请求业务
"""

#定义测试类：
from Test_TPshop import app


class UserLogin:
    # 函数1：验证码获取请求
    def get_verify_coode(self, session):
        # session.get("验证码的URL")
        return session.get(app.BASE_URL + "index.php?m=Home&c=User&a=verify")

    # 函数2：登录请求
    def login(self, session, username, password, verify_code):
        # session.post("登录的URL",data="登录数据")
        myLoginData = {"username": username,
                       "password": password,
                       "verify_code": verify_code}
        return session.post(app.BASE_URL + "localhost/index.php?m=Home&c=User&a=do_login", data=myLoginData)



