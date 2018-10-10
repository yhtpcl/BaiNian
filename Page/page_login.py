import allure

from Base.base import Base
import Page


class PageLogin(Base):
    # 点击"我"
    @allure.step("点击'我'")
    def page_click_me(self):
        self.base_get_xpath(Page.me_btn).click()

    @allure.step("点击'已有账号立即登录'")
    # 点击""已有账号立即登录
    def page_click_info(self):
        self.base_get_xpath(Page.user).click()

    @allure.step("输入账号")
    # 输入账号
    def page_input_username(self,user):
        self.base_input(Page.username,user)

    @allure.step("输入密码")
    # 输入密码
    def page_input_pwd(self,text):
        self.base_input(Page.uesrpwd,text)

    @allure.step("点击'登录'")
    # 点击登录
    def page_click_dl_btn(self):
        self.base_click(Page.login_btn)

    @allure.step("点击设置按钮")
    # 点击设置按钮
    def page_page_setting_btn(self):
        self.base_click(Page.setting_btn)

    @allure.step("从'短信提醒'滑动到'修改密码'")
    # 从元素1滑动到元素2
    def page_drag_and_drop(self):
        el1=self.base_get_xpath(Page.msg_id)
        el2=self.base_get_xpath(Page.update_pwd)
        self.base_drag_and_drop(el1,el2)

    @allure.step("点击'退出'")
    # 点击退出
    def page_click_exit(self):
        self.base_get_xpath(Page.exit).click()

    @allure.step("点击'确认'")
    # 确认退出
    def page_click_exit_btn(self):
        self.base_get_xpath(Page.exit_ok).click()

    # 将登录流程封装成一个方法
    def page_login(self,text,pwd):
        # 调用点击我的
        self.page_click_me()
        # 调用"已有账号立即登录"
        self.page_click_info()
        # 调用输入账号
        self.page_input_username(text)
#         调用输入密码
        self.page_input_pwd(pwd)
#         调用点击登录
        self.page_click_dl_btn()

    @allure.step("获取nickname")
    #     为了断言,是否成功登录,调用获取文本方法
    def page_get_nickname(self):
        return self.base_get_text(Page.login_nickname)
#         封装退出方法
    def page_exit(self):
        # 调用查找设置方法
        self.page_page_setting_btn()
#         调用元素滑动方法
        self.page_drag_and_drop()
#         调用点击退出方法
        self.page_click_exit()
        #         调用确定退出
        self.page_click_exit_btn()