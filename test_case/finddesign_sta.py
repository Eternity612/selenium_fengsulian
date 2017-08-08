import sys,unittest,time
sys.path.append("./page_obj")
sys.path.append("./public/common")

from selenium import webdriver
from public.common.base import *
from public.common.log import Log
from public.common.login_pub import Login_pub
from page_obj.loginPage import url
from page_obj.finddesignPage import FinddesignPage

log = Log()

class Finddesign_test(unittest.TestCase):
    '''找设计功能测试'''

    @classmethod
    def setUpClass(cls):
        log.info("===================testStart===================")
        cls.driver = browser("chrome")
        log.info("启动浏览器。")
        cls.finddesign = FinddesignPage(cls.driver)
        cls.finddesign.open(url)
    '''
    def addcookie(self):
        cookies = [
            {'domain': 'www.fengsulian.com', 'secure': False, 'path': '/', 'name': 'JSESSIONID',
             'value': '3145f0fe-8213-4498-ba22-92ce78eb427c'},
            {'path': '/', 'name': 'Hm_lvt_58e82c0bcec24e2073991faa04cb3f35', 'expiry': 1531038859,
             'value': '1499479744', 'domain': '.fengsulian.com', 'secure': False},
            {'domain': '.fengsulian.com', 'secure': False, 'path': '/',
             'name': 'Hm_lpvt_58e82c0bcec24e2073991faa04cb3f35', 'value': '1499502859'}
        ]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(3)
        self.driver.refresh()
        '''
    def test_finddedign_1(self):
        '''"找设计"页面测试'''
        #登录
        #self.add_cookie()
        Login_pub(self.driver).login('18675956153', '123456xyf')
        self.finddesign.click_finddesign()
        self.finddesign.click_default()
        self.finddesign.click_enterprise()
        #text1=self.driver.find_element_by_cs_selector(".person_des>h1").text
        #Page.assertEqual(self.driver,text1,self.driver.click_enterprise())
        #print(text1,self.driver.click_enterprise())
        #log.info("断言结束，用例执行完毕！")
        Page.screen_shot(self)

        self.driver.back()
        self.finddesign.view_card()
        self.finddesign.next_page()


    def test_finddesign_2(self):
        '''"找设计"页面测试_翻页'''
        self.driver.back()
        self.finddesign.view_card()

        self.finddesign.click_enterprise()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.info("关闭浏览器。")
        log.info("===================testEnd=====================")

if __name__ == "__main__":
    unittest.main()