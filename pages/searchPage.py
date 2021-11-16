from selenium import webdriver
import sys
sys.path
from pages.basePages import basePage
from selenium.webdriver.common.by import By

class SearchPage(basePage):

    search_input=(By.CLASS_NAME,'el-input__inner')
    search_btn=(By.CLASS_NAME,'el-icon-search')


    def input_search_text(self,text):
        self.input_text(self.search_input,text)

    def click_search_btn(self):
        self.click(self.search_btn)


