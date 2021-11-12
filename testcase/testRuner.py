import HTMLTestRunner
import unittest
import time
import os

#在测试报告目录下找到最新的报告文件,打印且返回最新报告的名称
def find_new_report(report_dirc):
    lists = os.listdir(report_dirc)
    lists.sort(key=lambda fn:os.path.getmtime(report_dirc+"\\"+fn))
    new_report = os.path.join(report_dirc,lists[-1])
    print(new_report)
    return new_report

def all_case():
    #执行用例的目录
    curent_dirc=os.path.dirname(os.path.realpath(__file__))
    case_dir = curent_dirc
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            #添加测试用例到testcase
            testcase.addTest(test_case)
    print(testcase)
    return testcase

if __name__ =="__main__":
    forword_dirc=os.path.abspath(os.path.join(os.getcwd(), ".."))
    report_dirc = forword_dirc + "\\"+"result\\"
    print(report_dirc)
    now = time.strftime("%Y%m%d")
    report_name = report_dirc+"自动化测试报告.html"
    fp = open(report_name,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                            title="自动化测试报告",
                            description=None)
    runner.run(all_case())
    fp.close()