"""
@FileName：test_login.py
@Description：
@Author：baojun.wang
@Time：2025/5/10 15:59
"""
import time

from browser import BrowserFactory
from case.base_case import BaseCase
from pages.account_page import AccountPage
from pages.home_page import HomePage
from utils.config import ConfigParser
from utils.logging import logger


class TestLogin(BaseCase):
    def teardown_class(self):
        """
        所有case运行结束后销毁浏览器实例
        """
        BrowserFactory.close_all()
        logger.info("所有case运行结束，销毁浏览器实例")

    def test_login(self):
        """
        case： 测试登录
        """
        # 实例化一个页面对象
        page = BrowserFactory.get_page()
        # 从配置文件读取当前环境对应的域名
        domain = ConfigParser.get_config('Domain', self.env())
        logger.info(f"当前环境为：{self.env()}，打开页面地址：{domain}")
        # 打开页面
        page.goto(domain)
        # 实例化一个首页对象
        home_page = HomePage(page)
        # 点击登录按钮
        home_page.click_login_button()
        # 等待隐私协议弹窗出现
        home_page.wait_for_element_visible(locator='.lib10-secret-dialog-footer')
        # 点击隐私协议弹窗中的同意并继续按钮
        home_page.click_privacy_agreement_dialog_agree_button_and_continue()

        # 实例化一个账户页面对象
        account_page = AccountPage(home_page.page)
        # 切换到-使用密码登录
        account_page.switch_to_login_by_password()
        #  输入手机号
        account_page.input_phone_code(ConfigParser.get_config(sector='PhoneCode', item=self.env()))
        # 输入密码
        account_page.input_password(ConfigParser.get_config(sector='PassWord', item=self.env()))
        # 点击隐私协议复选框
        account_page.click_privacy_agreement_checkbox()
        #  点击登录按钮
        account_page.click_login_button()

        time.sleep(3)
        # 判断首页用户名是否存在
        assert home_page.username_is_exist(), "登录失败: 首页顶部用户名不存在"
        logger.info(f"登录成功，当前用户名为：{home_page.get_current_username()}")
