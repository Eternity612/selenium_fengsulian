import sys,unittest,time
sys.path.append("./page_obj")
sys.path.append("./public/common")

from public.common.base import *
from public.common.login_pub import Login_pub
from page_obj.loginPage import url
from page_obj.profilePage import ProfilePage
from public.common.log import Log

log = Log()

class Profile_test(unittest.TestCase):
    """
    个人资料页面的用例
    """

    def setUp(self):
        log.info("--------测试开始--------")
        self.driver = browser("chrome")
        log.info("启动浏览器。")
        self.profilepage = ProfilePage(self.driver)
        self.profilepage.open(url)
        log.info("输入地址%s" % url)

    def test_profile01(self):
        '''个人资料修改'''
        # 登录
        Login_pub(self.driver).login('18675956153', '123456xyf')

        self.profilepage.open_profile()
        self.profilepage.real_name('张三')
        self.profilepage.choose_sex01()
        self.profilepage.email('790577657@qq.com')
        self.profilepage.choose_locator()
        self.profilepage.detail_address('杭州市西湖区')
        self.profilepage.upload_photo(r'E:\我的学习文档\selenium_fengsulian\data\cate.jpg')
        self.profilepage.submit()
        Page.screen_shot(self)

    def tearDown(self):
        self.driver.quit()
        log.info("关闭浏览器。")
        log.info("--------测试结束--------")

if __name__ == "__main__":
    unittest.main()
