from .base import *

class Profile(Page):
    '''
    个人资料
    '''
    #定位页面元素

    #当前登录用户
    current_user_loc = ("css selector",".loginIn.fl>span")
    #个人资料
    profile_loc = ("css selector",".nav_menu_bot>ul>li>a")
    #真实姓名
    reall_name_loc = ("css selector","#name")
    #性别（男）
    sex_male_loc = ("xpath",".//input[@value='男']")
    #性别（女）
    sex_female_loc = ("xpath",".//input[@value='女']")
    #电子邮箱
    email_loc = ("xpath",".//*[@id='email']")
    #位置（省、市、区）
    position_pro_loc = ("css selector",".selected")
    position_city_loc = ("css selector","#sArea2Id>li")
    position_area_loc = ("css selector","#sArea3Id>li")
    #详细地址
    detail_address_loc = ("xpath",".//input[@name='address']")

    #头像
    edit_loc = ("xpath",".//span[contains(text(),'编辑')]")
    #选择文件
    choose_file_loc = ("id","cropper_id")
    up_file_loc = ("xpath",".//div[contains(text(),'确定上传')]")

    #确定
    submit_button_loc = ("xpath",".//input[@value='确定']")
