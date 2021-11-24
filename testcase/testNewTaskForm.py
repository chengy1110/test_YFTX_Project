import os
import unittest
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.loginPage import LoginPage
from pages.newTaskForm import NewTaskForm



class TestNewTaskForm(unittest.TestCase):
    sys.setrecursionlimit(100000)
    driver=webdriver.Chrome()

    def setUp(self,text1 = 'chengy3',text2 = '1'):
        self.driver.get('http://delivertest.gisquest.com/logout')
        self.driver.maximize_window()
        sleep(2)

        login_page = LoginPage(self.driver)
        login_page.input_username_text(text1)
        login_page.input_pwd_text(text2)
        login_page.click_login_btn()
        sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[7]/span').click()
        sleep(2)



    def testNewTaskForm(self,task_text1="新建任务工单测试",task_text2="标签测试",start_date_text3="2021-08-09",end_date_text4="2021-10-09",
                        tasktime_text5="0.2",taskgrade_text6="2",handler_text7="李子川",describe_text8="测试描述信息",path_text9="D:/auto/AutoIt3_file/new_test.exe"):

        newTaskForm_page = NewTaskForm(self.driver)

        self.driver.switch_to.frame("google_con_frame")
        #点击新建按钮
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/a').click()
        sleep(1)

        
        #新建页面，填写任务名称
        newTaskForm_page.input_task(task_text1)
        #选所属项目
        newTaskForm_page.chioce_project()
        # 选任务类型
        newTaskForm_page.chioce_tasktype()
        #添加标签
        newTaskForm_page.input_tag(task_text2)
        # 选开始日期
        newTaskForm_page.input_start_date(start_date_text3)
        # 选截止日期
        newTaskForm_page.input_end_date(end_date_text4)
        # 填预计工时
        newTaskForm_page.input_tasktime(tasktime_text5)
        # 填任务积分
        newTaskForm_page.input_taskgrade(taskgrade_text6)
        # 选优先级
        newTaskForm_page.chioce_grade()
        # 选处理人
        newTaskForm_page.chioce_handler(handler_text7)
        # 填描述信息
        newTaskForm_page.input_descreb(describe_text8)
        #上传附件
        newTaskForm_page.file_upload(path_text9)
        sleep(3)
        # 提交
        newTaskForm_page.click_commite_btn()





