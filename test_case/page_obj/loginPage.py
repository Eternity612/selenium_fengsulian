import sys
sys.path.append("./public/common")
from public.common.base import *
from time import  sleep
from selenium import webdriver

url= "http://www.fengsulian.com/"

class LoginPage(Page):
    '''
    用户登录
    '''

    #定位器，定位页面元素

    #登录框
    login_alert = ("css selector",".notLogin>a")
    #用户名
    username_loc = ("id","username")
    #密码
    pwd_loc = ("id","password")
    #登录按钮
    login_button = ("xpath",".//input[@value='登录']")
    #登录成功后的用户名
    login_sucess_loc = ('css selector','.loginIn.fl>span')
    #用户名为空
    username_null_loc = ("xpath","html/body/div[4]")
    #密码为空
    pwd_null_loc = ("xpath","html/body/div[4]")
    #用户名、密码错误
    username_err_loc = ("xpath","html/body/div[4]")

    def __init__(self):
        self.driver = browser('chrome')

    def loginalert(self):
        self.click(self.login_alert)

    def input_username(self,username):
        '''
        输入帐号 
        '''
        self.send_keys(self.username_loc,username)

    def input_pwd(self,pwd):
        '''
        输入密码
        '''
        self.send_keys(self.pwd_loc,pwd)

    def login_submit(self):
        '''
        点击登录按钮
        '''
        self.click(self.login_button)

    #登录方法
    def login(self,username,pwd):
        '''
        登录方法  
        '''
        self.loginalert()
        self.input_username(username)
        self.input_pwd(pwd)
        self.login_submit()

    def is_login_sucess(self):
        '''
        判断是否获取到登录名称
         '''
        try:
            text = self.driver.find_element_by_css_selector(".loginIn.fl>span").text
            #text = self.find_element("css selector",".loginIn.fl>span").text
            return True
        except:
            #print(e)
            return False



'''
    #用户名为空提醒
    def uesrname_null(self):
        return self.find_element(self.username_null_loc).text
    
    #密码为空提醒
    def pwd_null(self):
        return self.find_element(self.pwd_null_loc).text
    
    #帐号、密码错误
    def username_err(self):
        return self.find_element(self.username_err_loc).text
    '''
if __name__ == "__main__":
    dr = webdriver.Chrome()
    dr.get('http://www.fengsulian.com/')
    sleep(5)
    A = LoginPage()
    A.login('18675956153','123456xyf')
    A.is_login_sucess()