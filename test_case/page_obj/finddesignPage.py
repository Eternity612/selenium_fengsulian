import sys,time,random
sys.path.append("./public/common")
from public.common.log import Logger
from public.common.base import *
from selenium import webdriver

class FinddesignPage(Page):
    '''找设计页面操作'''
    #定位页面元素 找设计
    find_design_loc = ("css selector",".nav_bar.fl>ul>li>a")
    #默认行业领域
    default_industry_loc = ("css selector",".class_action_con.class_action_dom.nearBusinessTypeParent>a")
    #随机点击的企业名
    enterprise_loc = ("css selector",".fr>a>h2")
    #点击企业后，新的页面上的企业名（用于断言）
    new_enterpise_loc = ("css selector",".person_des>h1")

    def __init__(self):
        '''初始化driver参数'''
        self.driver = browser('chrome')

    def click_finddesign(self):
        '''点击找设计'''
        element = self.find_elements(self.find_design_loc)[1]
        element.click()
        log.info("点击'找设计'：{}".format(self.find_design_loc))

    def click_default(self):
        '''点击行业领域"默认按钮"'''
        element = self.find_elements(self.default_industry_loc)[0]
        text1 = element.text
        element.click()
        return text1
        log.info("点击行业领域'默认按钮：{}".format(self.default_industry_loc))

    def click_enterprise(self):
        '''随机点击一个企业'''
        elements = self.find_elements(self.enterprise_loc)
        for i in range(random.randint(1,50)):
            text2 = elements[i].text
            elements[i].click()
            log.info("随机点击一个企业")
            return text2