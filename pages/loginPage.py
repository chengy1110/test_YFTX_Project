from selenium.webdriver.common.by import By

from pages.basePages import basePage


class LoginPage(basePage):
    '输入用户名、密码，进行登录'
    username_input=(By.ID,'username')
    pwd_input = (By.ID, 'password')
    login_button=(By.CLASS_NAME,'login-btn')

    def input_username_text(self,name):
        self.input_text(self.username_input,name)

    def input_pwd_text(self,pwd):
        self.input_text(self.pwd_input, pwd)

    def click_login_btn(self):
        self.click(self.login_button)