from selenium.webdriver.common.by import By
# 定位我的
me_btn="我"
# 定位"已有账号,立即登录"
user="已有账号"
# 定位账号输入框
username=By.ID,"com.yunmall.lc:id/logon_account_textview"
# 定位密码输入框
uesrpwd=By.ID,"com.yunmall.lc:id/logon_password_textview"
# 定位点击登录按钮
login_btn=By.ID,"com.yunmall.lc:id/logon_button"
# 定位设置按钮
setting_btn=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 将 短信提醒 滑动至 修改密码
msg_id="短信提醒"
update_pwd="修改密码"
# 定位退出
exit="退出"
# 定位点击确认
exit_ok="确认"
# 登录后的定位元素
login_nickname=By.ID,"com.yunmall.lc:id/tv_user_nikename"