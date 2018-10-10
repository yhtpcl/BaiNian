import os,sys
sys.path.append(os.getcwd())
import pytest
import allure
from Page.page_login import PageLogin
from Base.get_driver import get_driver
from Base.read_login_yaml import ReadYaml


def get_data():
    datas=ReadYaml("login.yaml").base_read_yaml()
    arrs=[]
    for data in datas.values():
        arrs.append((data.get("username"),data.get("password"),data.get("expect"),data.get("toast_expect")))
    return arrs
class TestLogin():
    def setup_class(self):
        self.login=PageLogin(get_driver())
        self.login.page_click_me()
        self.login.page_click_info()
    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize(("username,password,expect,toast_expect"),get_data())
    def test_login(self,username,password,expect,toast_expect):
        # 默认为TRUE,如果expect为TRUE代表有值也就是正向用例,需要进行以下操作
        # 通过模拟功能测试得出思路
        if expect:
            # 进行异常捕获
            try:
                #  输入用户名
                self.login.page_input_username(username)

                # 输入密码
                self.login.page_input_pwd(password)

        #         点击登录
                self.login.page_click_dl_btn()

        #         断言登录后的名称
                assert expect in self.login.page_get_nickname()
                allure.attach("登录状态: ","登录成功")

        #         退出登录
                self.login.page_exit()

        #         点击我的
                self.login.page_click_me()

        #         点击已有账户立即登录
                self.login.page_click_info()

            #     如果出现异常就截图保存
            except:
                # 调用截图方法
                self.login.base_get_screenshot()
                # 打开截图
                with open("./Image/filed.png","rb") as f:
                    # 写入报告中,三个参数:描述,读取文件,写入报告格式声明   png
                    allure.attach("登录失败描述",f.read(),allure.attach_type.PNG)
                raise
        #     相反也就是expect为空,对应的就是逆向,需要执行的操作
        else:
            try:
                # 输入用户名

                self.login.page_input_username(username)
                # 输入密码：
                self.login.page_input_pwd(password)
                # 点击登录
                self.login.page_click_dl_btn()
                # 断言toast_expect消息
                # 调用获取toast消息方法,动态判断登录后的是否相等
                assert toast_expect in self.login.base_get_toast(toast_expect)
                allure.attach("登录状态","逆向断言成功")
            except:
                self.login.base_get_screenshot()
                with open("./Image/filed.png","rb") as f :
                    allure.attach("登录失败描述",f.read(),allure.attach_type.PNG)
                raise