import sys,unittest,time
sys.path.append("./page_obj")
sys.path.append("./public/common")

from public.common.base import *
from public.common.login_pub import Login_pub
from page_obj.loginPage import url
from page_obj.finddesignPage import FinddesignPage

class Finddesign_test(unittest.TestCase,FinddesignPage):
    '''找设计功能测试'''

    def setUP(self):
        self.driver = FinddesignPage()
        self.driver.open(url)

    def test_finddedign_1(self):
        '''"找设计"页面测试'''
        Login_pub(self.driver).login('18675956153', '123456xyf')
        self.driver.click_finddesign()
        self.driver.click_default()
        self.driver.click_enterprise()
        Page.assertEqual(self.driver,text1,text2)
        Page.screen_shot(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()