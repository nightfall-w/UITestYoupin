"""
@FileName：account_page.py
@Description：登录授权页面
@Author：baojun.wang
@Time：2025/5/10 17:05
"""
from pages.base_page import BasePage


class AccountPage(BasePage):
    """
    登录授权页面
    """

    def switch_to_login_by_password(self):
        """
        切换到-使用密码登录
        :return:
        """
        self.page.locator('a:text("密码登录")').click()

    def input_phone_code(self, username):
        """
        输入手机号
        :param username:
        :return:
        """
        phone_input = self.page.locator('input[name="account"]')
        phone_input.fill(username)
        assert phone_input.input_value() == username, f"手机号输入失败，输入框显示内容与输入值{username}不一致"

    def input_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        password_input = self.page.locator('input[name="password"]')
        password_input.fill(password)
        assert password_input.input_value() == password, f"密码输入失败，输入框显示内容与输入值{password}不一致"

    def click_privacy_agreement_checkbox(self):
        """
        点击统一隐私协议复选框
        """
        checkbox = self.page.locator('label:has-text("已阅读并同意") input[type="checkbox"]')
        checkbox.click()
        assert checkbox.is_checked(), "统一隐私协议复选框未勾选成功"

    def click_login_button(self):
        """
        点击登录按钮
        :return:
        """
        self.page.get_by_role('button', name='登录').click()
