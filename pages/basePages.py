import os
import sys
sys.path
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class basePage(object):
    "page基类，所有page都应该继承该类"
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_text(self,loc,text):
        self.find_element(*loc).send_keys(text)

    def click(self,loc):
        self.find_element(*loc).click()

    def dropdown_menu(self,loc1,loc2):
        ActionChains(self.driver).move_to_element(self.find_element(*loc1)).click().perform()
        ActionChains(self.driver).release()
        sleep(2)
        self.find_element(*loc2).click()

    def button_input(self,loc1,loc2):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc1)).click().send_keys(loc2).perform()

    def date_input(self,loc1,loc2):
        self.find_element(*loc1).clear()
        self.find_element(*loc1).send_keys(loc2)

    def handler_input(self, loc1,loc2,loc3):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc1)).click().perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element(*loc1)).click().send_keys(loc2).perform()
        self.find_element(*loc3).click()

    def upload(self,loc1,loc2):
        self.find_element(*loc1).click()
        os.system(loc2)


    def get_title(self):
        return self.driver.title