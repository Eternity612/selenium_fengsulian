import os,time
from selenium import webdriver

def screen_shot(self,file_path):
    nowtime = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    try:
        self.get_screenshot_as_file(filepath + nowtime + '.jpg')
    except Exception as e:
        print("截图失败，原因是 %s" % e)

if __name__ == "__main__":
    screen_shot('F:\\1.jpg')