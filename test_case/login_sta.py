import sys,unittest,time
sys.path.append("./page_obj")
sys.path.append("./pub_code")

import ddt
from pub_code import read_excel
from page_obj.base import *
from page_obj.loginPage import LoginPage,url

testData = read_excel.ExcelUntil("sheet1",r"F:\My_Project\selenium_fengsulian\data\username_pwd.xlsx")
'''testData = [
    {"username":"18675956153","pwd":"123456"},
    {"username":"","pwd":"123456xyf"},
    {"username":"18675956153","pwd":""}
]
'''

@ddt.ddt
class Login_test(unittest.TestCase,LoginPage):
    '''
    登录页面的case
    '''


    def setUp(self):
        self.driver = LoginPage()
        self.driver.open(url)

    def login_case(self,username,pwd):
        '''
        登录用例的方法
        '''
        #第1步：点击登录按钮，弹出登录名、密码输入框
        self.driver.loginalert()
        #第2步：输入用户名
        self.driver.input_username(username)
        #第3步，输入密码
        self.driver.input_pwd(pwd)
        #第4步，点击登录按钮登录
        self.driver.login_submit()
        ''''#第5步：测试结果,判断是否登录成功
        result = self.driver.is_text_in_element(('css selector','.loginIn.fl>span'),'FSL_77340077')
        #第6步：期望结果
        expect_result = expect
        self.assertEqual(result, expect_result)
        '''

    @ddt.data(*testData)
    def test_login01(self,data):
        """
        登录测试用例
        """
        self.login_case(data["username"],data["pwd"])
        result = self.driver.is_login_sucess()
        self.assertEqual(data["test_result"],["expect_result"])

    '''
    @ddt.data(*testData)
    def test_login02(self,data):
        '''
        #输入正确的帐号、错误的密码
    '''
        self.login_case(data["username"],data["pwd"])
        print(data["username"], data["pwd"])
        #po = LoginPage()
        result = self.driver.is_text_in_element(self.username_err_loc, '账号密码不匹配,请重新输入!')
        self.assertEqual(result,True)

    @ddt.data(*testData)
    def test_login03(self,data):
        '''
        #用户名为空
    '''
        self.login_case(data["username"],data["pwd"])
        print(data["username"], data["pwd"])
        result = self.driver.is_text_in_element(self.username_null_loc,"请输入手机号码")
        self.assertEqual(result,True)

    @ddt.data(*testData)
    def test_login04(self,data):
        '''
        #密码为空
    '''
        self.login_case(data["username"],data["pwd"])
        result = self.driver.is_text_in_element(self.pwd_null_loc,"请输入您的密码")
        self.assertEqual(result,True)
        print(data["username"], data["pwd"])
        '''

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
