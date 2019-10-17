"""
项目架构：
    核心：api + case + data
    -api  封装请求相关业务（使用requests 向服务器发送请求）
    -case 封装 unittest相关实现（调用api的 请求业务，参数化调用 data中测试数据，自身还需要实现断言业务）
    -data 封装测试数据
    测试报告：report +tools + run_suite.py
    -report 保存生成的测试报告
    -tools 存储的第三方工具
    -run_suite.py 组织测试套件

"""
import os
import unittest
import requests
#封装不同接口中 URL相同的前缀（协议 + 域名）
BASE_URL="http://localhost/"

#项目路径
#路径使用优先级：动态获取绝对路径>相对路径>写死的绝对路径
PRO_PATH=os.getcwd()