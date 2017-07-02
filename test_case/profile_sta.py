import sys,unittest,time
sys.path.append("./page_obj")
sys.path.append("./public/common")

from public.common.base import *
from public.common.login_pub import Login_pub
from page_obj.loginPage import url
from page_obj.profilePage import ProfilePage

class Profile_test(unittest.TestCase,ProfilePage):
    """
    个人资料页面的用例
    """

    def setUp(self):
        self.driver = ProfilePage()
        self.driver.open(url)

    def test_profile01(self):
        '''个人资料修改'''
        # 登录
        Login_pub(self.driver).login('18675956153', '123456xyf')

        self.driver.open_profile()
        self.driver.real_name('张三')
        self.driver.choose_sex01()
        self.driver.email('790577657@qq.com')
        self.driver.choose_locator()
        self.driver.detail_address('杭州市西湖区')
        self.driver.upload_photo(r'E:\我的学习文档\selenium_fengsulian\data\cate.jpg')
        self.driver.submit()
        Page.screen_shot(self.driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
