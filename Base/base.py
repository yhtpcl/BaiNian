from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Base():
    def __init__(self,driver):
        self.driver=driver
    #    封装查找元素方法
    def base_find_element(self,loc,timeout=30,poll=0.5):
        # 实例化
        driver=self.driver
        # 设置显示等待,给个默认值,谁调用就需要传入定位路径
        return WebDriverWait(driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 封装点击元素方法
    def base_click(self,loc):
        self.base_find_element(loc).click()
    #     封装输入内容方法
    def base_input(self,loc,text):
        e1=self.base_find_element(loc)
        e1.clear()
        e1.send_keys(text)
    #     封装截图方法
    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file("./Image/filed.png")
    #     封装获取toast弹出框方法
    def base_get_toast(self,massage):
        massage="//*[contains(@text,'"+massage+"')]"
        loc=(By.XPATH,massage)
        # self.base_get_xpath(massage)
        return self.base_find_element(loc,poll=0.1).text
    # 封装定位Xpath元素方法
    def base_get_xpath(self,text):
        loc=By.XPATH,"//*[contains(@text,'"+ text +"')]"
        return self.base_find_element(loc)
    # 从元素1滑动到元素2
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)
    #     获取文本信息
    def base_get_text(self,loc):
        return self.base_find_element(loc).text