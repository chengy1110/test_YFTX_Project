from selenium.webdriver.common.by import By

from pages.basePages import basePage


class TaskFormList(basePage):
    # 新建任务按钮
    buildtaskform_btn = (By.CLASS_NAME,'create-product-btn more-create-btn')

    def click_buildtaskform_btn(self):
        self.click(self.buildtaskform_btn)

