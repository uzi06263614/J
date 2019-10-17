"""
    组织测试套件生成测试报告
    流程：
        1.导包
        2.创建套件对象
        3.创建文件流，并使用工具执行套件，将执行结果写入文件流

"""
# 导包
import time
import unittest

from BeautifulReport import BeautifulReport

from Test_TPshop.case.test_tpshop import TestUser

# 2.创建套件对象


suite = unittest.TestSuite()
# 添加测试类或测试函数
suite.addTest(unittest.makeSuite(TestUser))
# 先创建文件
# file_to = "./report/report" + time.strftime("%Y%m%d-%H%M%S") + ".html"
# 打开文件流，工具执行套件，并将结果写出
# with open(file_to,"wb")as f:
#     runner=HTMLTestRunner(f,title="我的测试报告",description="v1.0")
#     runner.run(suite)
BeautifulReport(suite).report(filename="report.html", description="v1.0",log_path="./report/")
