"""
@FileName：home_page.py
@Description：首页
@Author：baojun.wang
@Time：2025/5/9 12:30
"""
import time

from pages.base_page import BasePage


class HomePage(BasePage):
    """
    首页类
    """

    def click_login_button(self):
        self.page.locator('.m-safe-anchor:text("登录")').click()

    def click_register_button(self):
        self.page.locator('.m-safe-anchor:text("注册")').click()

    def wait_for_privacy_agreement_dialog(self):
        self.wait_for_element_visible(locator='.lib10-secret-dialog-footer')

    def click_privacy_agreement_dialog_agree_button_and_continue(self):
        """
        点击隐私协议的dialog弹窗中的同意并继续按钮
        """
        self.page.locator('.lib10-secret-dialog-footer .ok-btn').click()

    def username_is_exist(self):
        """
        判断首页顶部用户名是否存在
        """
        return self.page.locator('.m-username').is_visible()

    def get_current_username(self):
        """
        获取首页用户昵称 用来判断是否登录成功
        """
        return self.page.locator('.m-username').inner_text()
