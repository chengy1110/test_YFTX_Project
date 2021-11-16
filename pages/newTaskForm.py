import os
import sys
sys.path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from pages.basePages import basePage


class NewTaskForm(basePage):

    #任务名称字段
    task = (By.XPATH,'//*[@id="app"]/div/form/div[1]/div[2]/div[1]/div/div[1]/input')

    #所属项目字段，绩效考核
    project_btn=(By.XPATH,'//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[1]/div/input')
    project_option=(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/ul[1]/li[2]/ul/li[1]/span')

    #任务类型字段，选择需求
    tasktype_btn=(By.XPATH, '//*[@id="app"]/div/form/div[1]/div[2]/div[3]/div/div/div[1]/input')
    tasktype_chioce =(By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')

    #标签字段
    tag_btn=(By.XPATH, '//*[@id="tags"]/div/div/button/span')

    #开始日期
    start_date=(By.CSS_SELECTOR,'input[placeholder="开始日期"]')
    #截止日期
    end_date=(By.CSS_SELECTOR,'input[placeholder="截止日期"]')
    #预计工时
    tasktime=(By.CSS_SELECTOR,'input[placeholder="请输入预计工时"]')
    #任务积分
    taskgrade= (By.CSS_SELECTOR, 'input[placeholder="请输入任务积分"]')
    #优先级，选择高
    grade_btn = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div[2]/div[5]/div[5]/div/div/div/span/span/i')
    grade_chioce = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li[1]/span')
    #处理人，选择李子川
    handler_btn = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div[2]/div[5]/div[6]/div/div/div[1]/span/span/i')
    handler_chioce = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li/span')

    #描述信息
    describe_btn = (By.CLASS_NAME, 'w-e-text')
    #附件按钮
    file_btn=(By.XPATH,'//*[@id="app"]/div/form/div[2]/div[2]/div[2]/div/div/div/div/button/span')
    #提交按钮
    commite_btn=(By.XPATH,'//*[@id="app"]/div/form/div[2]/div[2]/div[3]/div/div/button[2]/span')

    #任务名称
    def input_task(self,task_text1):
        self.input_text(self.task,task_text1)

    #所属项目
    def chioce_project(self):
        self.dropdown_menu(self.project_btn,self.project_option)


    # 任务类型
    def chioce_tasktype(self):
        self.dropdown_menu(self.tasktype_btn,self.tasktype_chioce)

    #标签
    def input_tag(self,task_text2):
        self.button_input(self.tag_btn,task_text2)


    #开始日期
    def input_start_date(self,start_date_text3):
        self.date_input(self.end_date,start_date_text3)


    #截止日期
    def input_end_date(self, end_date_text4):
        self.date_input(self.start_date,end_date_text4)

    #预计工时
    def input_tasktime(self, tasktime_text5):
        self.input_text(self.tasktime, tasktime_text5)

    #任务积分
    def input_taskgrade(self, taskgrade_text6):
        self.input_text(self.taskgrade, taskgrade_text6)

    #优先级
    def chioce_grade(self):
        self.dropdown_menu(self.grade_btn,self.grade_chioce)

    #处理人
    def chioce_handler(self,handler_text7):
        self.handler_input(self.handler_btn,handler_text7,self.handler_chioce)


    #描述信息
    def input_descreb(self, describe_text8):
        self.input_text(self.describe_btn, describe_text8)

    #附件上传
    def file_upload(self,path_text9):
        self.upload(self.file_btn,path_text9)

    #点击确定
    def click_commite_btn(self):
        self.click(self.commite_btn)
