import HTMLTestRunner,time,os,unittest

import smtplib
from config import globalparam
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendemail(new_file):
    _from  = "790577657@qq.com"
    _pwd   = "qwmzgnsieatxbbei"
    _to    = "1292027762@qq.com"
    with open(filename,"rb") as f:
        _body = f.read()
    
    msg = MIMEText(_body,"html","utf-8")
    msg["Subject"] = "自动化测试报告_风速链登录"
    msg["date"] = time.strftime("%a, %d %b %Y %H:%M:%S %z")
    msg["From"] = _from
    msg["To"] = _to
    try:
      smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
      smtp.login(_from,_pwd)
      smtp.sendmail(_from,_to,msg.as_string())
      smtp.quit()
      print("Mail sends successfully！")
    except smtplib.SMTPException as e:
      print("Mail sending failed,the reason is %s" % e)

def findreport():
    #result_dir = r"./report/testreport/"
    result_dir = globalparam.report_path + '\\'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+ "\\" +fn))
           #if not os.path.isdir(result_dir+ "\\" +fn) else 0)
    print('The latest test_file is ：' + lists[-1])
    new_file = os.path.join(result_dir,lists[-1])
    print(new_file)
    sendemail(new_file)

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
    filename = (globalparam.report_path + '\\' + now + 'result.html')
    fp = open(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title = u'风速链自动化测试测试报告',
    description=u'用例执行情况')
    discover = unittest.defaultTestLoader.discover(globalparam.case_path,
                                                   pattern='*_sta.py')

    runner.run(discover)
    fp.close()

    findreport()
