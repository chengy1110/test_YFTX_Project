from PIL import ImageGrab
import time
from selenium import webdriver

class ScreenshotPicture(object):
    def __init__(self,driver):
        self.driver=driver

    def screenshot_image1(self,image_path):
         nowTime = time.strftime("%Y-%m-%d_%H-%M-%S")
         imageName = image_path + "//" + "bug_image{}.png".format(nowTime)
         self.driver.save_screenshot(imageName)

         try:
             self.driver.save_screenshot(imageName)
             print("%s ：截图成功！！！")
         except BaseException as pic_msg:
             print("截图失败：%s" % pic_msg)

