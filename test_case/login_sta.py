import sys,unittest,time
sys.path.append("./page_obj")
sys.path.append("./public/common")

import ddt
#from public.common.log1 import Log
from config import globalparam
from public.common.read_excel import ExcelUtil
from public.common.base import Page,browser
from page_obj.loginPage import LoginPage,url
from public.common.log import Log

log = Log()

data = ExcelUtil("Sheet1",globalparam.data_path+ '\\' + "username_pwd.xlsx")
testData = data.dict_data()

#testData = [{'pwd': '123456xyf', 'expect_result': 'True', 'username': '18675956153'}]

@ddt.ddt
class Login_test(unittest.TestCase):
    '''
    登录页面的case
    '''


    def setUp(self):
        #self.logger = Log()
        #self.logger.info('############################### START ###############################')
        self.driver = browser("chrome")
        self.login = LoginPage(self.driver) #login参数是LoginPage的实例
        self.login.open(url)

    """
    def login_case(self,username,pwd):
        '''
        登录用例的方法
        '''
        #第1步：点击登录按钮，弹出登录名、密码输入框
        self.login.loginalert()
        #第2步：输入用户名
        self.login.input_username(username)
        #第3步，输入密码
        self.login.input_pwd(pwd)
        #第4步，点击登录按钮登录
        self.login.login_submit()
        '''
        #第5步：测试结果,判断是否登录成功
        result = self.driver.is_text_in_element(('css selector','.loginIn.fl>span'),'FSL_77340077')
        #第6步：期望结果
        expect_result = expect
        self.assertEqual(result, expect_result)
        '''
        """

    @ddt.data(*testData)
    def test_login(self,data):
        """登录测试用例"""
        #print(data["username"],data["pwd"])
        self.login.login(data["username"],data["pwd"])
        time.sleep(3)
        #Page.screen_shot(self.driver)
        result = self.login.is_login_sucess()
        #print(result)
        Page.assertEqual(self, str(result),data["expect_result"])
        Page.assertEqual(self, str(result), data["expect_result"])
        log.info("执行断言函数：{0},{1}".format(str(result),data["expect_result"]))
        #用例执行完截图
        Page.screen_shot(self)
        log.info("用例执行完截图")

    def tearDown(self):
        self.driver.quit()
        # self.logger.info('###############################  End  ###############################')

if __name__ == "__main__":
    unittest.main()
