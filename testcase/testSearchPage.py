import sys
import unittest
from selenium import webdriver

from pages.loginPage import LoginPage
from pages.searchPage import SearchPage
from time import sleep
from common.screenshotPicture import ScreenshotPicture

class TestSearchPage(unittest.TestCase):
    sys.setrecursionlimit(100000)
    driver = webdriver.Chrome()

    def setUp(self,text1 = 'chengy3',text2 = 'qwe123'):
        self.driver.get('http://delivertest.gisquest.com/logout')
        self.driver.maximize_window()

        login_page = LoginPage(self.driver)
        login_page.input_username_text(text1)
        login_page.input_pwd_text(text2)
        login_page.click_login_btn()
        sleep(2)

    def testSearch(self,text='333',image_path='..\\picture\\'):
        self.driver.switch_to.frame("google_con_frame")
        search_page = SearchPage(self.driver)
        screenshot_picture = ScreenshotPicture(self.driver)


        search_page.input_search_text(text)
        search_page.click_search_btn()

        screenshot_picture.screenshot_image1(image_path)

        sleep(2)


    def tearDown(self) :
        self.driver.quit()


