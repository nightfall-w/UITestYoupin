"""
@FileName：base_page.py
@Description：页面基础
@Author：baojun.wang
@Time：2025/5/9 13:34
"""


class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_element_visible(self, locator):
        """
        等待元素可见

        locator: 元素选择器
        """
        self.page.wait_for_selector(locator)
