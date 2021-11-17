import os
import sys
from selenium import webdriver
import unittest

sys.path.append('pages/loginPage')
from pages.loginPage import LoginPage
from time import sleep
import ddt

from pages.excelUtil import ExcelUtil

forword_dirc=os.path.abspath(os.path.join(os.getcwd(), ".."))
filepath = forword_dirc + "\\"+"test_data"+"\\"+"test_data.xls"
sheetName = "Sheet1"
data = ExcelUtil(filepath, sheetName)
print(data.dict_data())

@ddt.ddt
class TestLoginPage(unittest.TestCase):
    sys.setrecursionlimit(100000)
    driver = webdriver.Chrome()

    def setUp(self) :
        self.driver.get('http://delivertest.gisquest.com/logout')
        self.driver.maximize_window()

    @ddt.data(*data.dict_data())
    @ddt.unpack
    def testLogin(self,name,pwd):
        login_page=LoginPage(self.driver)
        login_page.input_username_text(name)
        login_page.input_pwd_text(pwd)
        login_page.click_login_btn()
        sleep(2)

        # Assert  断言
        self.assertTrue('delivertest.gisquest.com/toHome1' in self.driver.current_url)
        print("断言1 登录成功跳转url：{0}".format(self.driver.current_url))


    """def tearDown(self) :
        self.driver.quit()"""

