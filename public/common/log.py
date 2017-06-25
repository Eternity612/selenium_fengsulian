import  logging
import os.path
import time

class Logger(object):

    def __init__(self,log_path="F:\\My_Project\\selenium_fengsulian\\report\\log\\"):
        '''
        log_path指定保存日志的文件路径，输出日志级别INFO
        '''

        #创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #输出格式
        self.formatter = logging.Formatter('%(sactime)s-%(filename)s[line:%(lineno)d] \
                        - %(funcName)s- %(levename)s:%(message)s')

        #指定导出log文件夹的路径地址
        self.log_path = log_path

    def log_file(self,level=logging.INFO):
        '''log文件导出到本地文件'''
        nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
        log_path = os.path.join(os.path.dirname(os.getcwd()), self.log_path)
            
        log_name = log_path + nowTime + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(level)

        fh.setFormatter(self.formatter)
            
        self.logger.addHandler(fh)

        fh.close()

    def console(self, level=logging.INFO):
        '''定义console日志级别和格式'''
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def log(self):
        '''输出log'''
        self.log_file()
        self.console()
        return self.logger
if __name__ == "__main__":
    log = Logger().log()
    log.info("打开浏览器")
    log.info("登录")
    log.warning("警告！")
    log.error("异常")