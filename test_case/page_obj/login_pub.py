from .base import *


class Login_pub(Page):
    '''
    登录的公共方法
    '''
    # 登录框
    login_alert = ("css selector", ".notLogin>a")
    # 用户名
    username_loc = ("id", "username")
    # 密码
    pwd_loc = ("id", "password")
    # 登录按钮
    login_button = ("xpath", ".//input[@value='登录']")

    # 用户名为空
    username_null_loc = ("xpath", "html/body/div[4]")
    # 密码为空
    pwd_null_loc = ("xpath", "html/body/div[4]")
    # 用户名、密码错误
    username_err_loc = ("xpath", "html/body/div[4]")

    def __init__(self,driver):
        '''
        初始化driver参数 
        '''
        self.driver = driver

    def loginalert(self):
        self.driver.click(self.login_alert)

    def input_username(self,username):
        '''
        输入帐号 
        '''
        self.driver.send_keys(self.username_loc,username)

    def input_pwd(self,pwd):
        '''
        输入密码
        '''
        self.driver.send_keys(self.pwd_loc,pwd)

    def login_submit(self):
        '''
        点击登录按钮
        '''
        self.driver.click(self.login_button)

    #登录方法
    def login(self,username,pwd):
        '''
        登录方法  
        '''
        self.loginalert()
        self.input_username(username)
        self.input_pwd(pwd)
        self.login_submit()