import sys,time,random
sys.path.append("./public/common")
from public.common.log import Log
from public.common.base import *
from selenium import webdriver

log = Log()

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

    #页码
    page_num_loc = ("css selector",".lz_page>a")

    #查看名片
    view_card_loc = ("css selector",".viewCard")
    #查看名片弹框上的企业名称
    view_card_enterpise_loc = ("css selector",".title.cardName_ajax")
    #分享到QQ
    share_to_qq_loc = ("css selector",".card_qq")
    #分享
    share_loc = ("css selector",".btn_s1_h28_r")
    #分享界面QQ登录
    login_button_loc = ("css selector","#changeAccounts")
    #帐号密码登录
    username_pwd_loc = ("css selector","#switcher_plogin")
    username_loc = ("css selector","#u")
    pwd_loc = ("css selector","#p")
    login_loc = ("css selector","#login_button")

    '''
    def __init__(self):
        初始化driver参数
        self.driver = browser('chrome')

    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            orig = super(FinddesignPage,cls)
            cls.instance = orig.__new__(cls)
        return cls.instance
    '''

    def click_finddesign(self):
        '''点击找设计'''
        element = self.find_elements(self.find_design_loc)[1]
        element.click()
        log.info("点击'找设计'：{}".format(self.find_design_loc))

    def click_default(self):
        '''点击行业领域"默认按钮"'''
        element = self.find_elements(self.default_industry_loc)[0]
        element.click()
        log.info("点击行业领域'默认按钮：{}".format(self.default_industry_loc))

    def click_enterprise(self):
        '''随机点击一个企业'''
        #print(elements)
        #self.find_elements(self.enterprise_loc)[9].click()
        #for i in random.randint(0,10):
        i = random.randint(0,9)
        elements = self.find_elements(self.enterprise_loc)[i]
        t1 = elements.text
        elements.click()
        #print(i)
        log.info("随机点击的企业是：" + t1)
        t2 = self.find_element(self.new_enterpise_loc).text
        Page.assertEqual(self,t1,t2)
        log.info("断言随机点击的企业：%s" % t1)
    def next_page(self):
       #点击第2页
        element = self.find_elements(self.page_num_loc)[7]
        element.click()
        log.info("点击下一页到第2页。" )
        j = random.randint(0, 9)
        elements = self.find_elements(self.enterprise_loc)[j]
        t1 = elements.text
        elements.click()
        #print(j)
        log.info("随机点击的企业是：" + t1)
        t2 = self.find_element(self.new_enterpise_loc).text
        Page.assertEqual(self, t1, t2)
        log.info("断言随机点击的企业：%s" % t1)
        self.back()
        self.view_card()

       #点击第3页、第4页
        for i in range(1, 3):
            element = self.find_elements(self.page_num_loc)[8]
            element.click()
            log.info("点击下一页到第%d页。" % (i+2))
            j = random.randint(0, 9)
            elements = self.find_elements(self.enterprise_loc)[j]
            t1 = elements.text
            elements.click()
            #print(j)
            log.info("随机点击的企业是：" + t1)
            t2 = self.find_element(self.new_enterpise_loc).text
            Page.assertEqual(self, t1, t2)
            log.info("断言随机点击的企业：%s" % t1)
            self.back()

            self.view_card()
        #点击下一页，从第5页到第16页
        for i in range(3,15):
            element = self.find_elements(self.page_num_loc)[9]
            element.click()
            log.info("点击下一页到第%d页。" % (i + 2))
            j = random.randint(0, 9)
            elements = self.find_elements(self.enterprise_loc)[j]
            t1 = elements.text
            elements.click()
            #print(j)
            log.info("随机点击的企业是：" + t1)
            t2 = self.find_element(self.new_enterpise_loc).text
            Page.assertEqual(self, t1, t2)
            log.info("断言随机点击的企业：%s" % t1)
            self.back()

            self.view_card()

        #点击下一页到第17、18页
        for i in range(15,16):
            element = self.find_elements(self.page_num_loc)[9]
            element.click()
            log.info("点击下一页到第%d页。" % (i + 2))
            j = random.randint(0, 9)
            elements = self.find_elements(self.enterprise_loc)[j]
            t1 = elements.text
            elements.click()
            # print(j)
            log.info("随机点击的企业是：" + t1)
            t2 = self.find_element(self.new_enterpise_loc).text
            Page.assertEqual(self, t1, t2)
            log.info("断言随机点击的企业：%s" % t1)
            self.back()
            self.view_card()

            el = self.find_elements(self.page_num_loc)[6]
            el.click()
            log.info("点击下一页到第18页。")
            j = random.randint(0, 7)
            elements = self.find_elements(self.enterprise_loc)[j]
            t1 = elements.text
            elements.click()
            # print(j)
            log.info("随机点击的企业是：" + t1)
            t2 = self.find_element(self.new_enterpise_loc).text
            Page.assertEqual(self, t1, t2)
            log.info("断言随机点击的企业：%s" % t1)
    def view_card(self):
        '''查看名片，并分享'''
        i = random.randint(0,9)
        element = self.find_elements(self.view_card_loc)[i]
        t1 = self.find_elements(self.enterprise_loc)[i].text
        log.info("查看名片的企业是：%s" % t1)
        element.click()
        log.info("点击 %s-查看名片。" % t1)
        time.sleep(3)
        t2 = self.find_element(self.view_card_enterpise_loc).text
        log.info("查看名片上企业名称是：%s" % t2)
        Page.assertEqual(self,t1,t2)
        #点击分享到QQ
        self.click(self.share_to_qq_loc)
        log.info("点击分享到QQ。")
        eles = self.driver.find_element_by_css_selector("#normalPanel")
        #分享界面 QQ登录
        eles.find_element(self.login_button_loc)
        print("1111111111")
        eles.find_element(self.username_pwd_loc)
        eles.send_keys(self.username_loc,"1292027762",is_clear=True)
        eles.send_keys(self.pwd_loc,"19900124,xyf",is_clear=True)
        eles.click(self.login_loc)
        time.sleep(3)
        #点击分享
        eles.click(self.share_loc)
        log.info("点击分享。")