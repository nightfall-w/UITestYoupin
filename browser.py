"""
@FileName：browser.py
@Description：实例化浏览器对象
@Author：baojun.wang
@Time：2025/5/9 11:14
"""
# browser_factory.py
from playwright.sync_api import sync_playwright


class BrowserFactory:
    """
    浏览器实例的抽象类，将浏览器进行封装，方便在case中直接引用
    """
    _browser = None
    _context = None
    _page = None

    @classmethod
    def get_browser(cls):
        """
        获取浏览器实例/实例化一个浏览器对象
        :return:
        """
        if not cls._browser:
            cls._playwright = sync_playwright().start()
            cls._browser = cls._playwright.chromium.launch(headless=False)
        return cls._browser

    @classmethod
    def get_context(cls):
        """
        获取浏览器会话/创建一个独立会话，类似于在浏览器中创建一个全新的隐私窗口（Incognito Window），但可以更灵活地控制其行为和状态。
        :return:
        """
        if not cls._context:
            browser = cls.get_browser()
            cls._context = browser.new_context()
        return cls._context

    @classmethod
    def get_page(cls):
        """
        获取当前页面/新打开一个页面
        :return:
        """
        if not cls._page:
            context = cls.get_context()
            cls._page = context.new_page()
        return cls._page

    @classmethod
    def close_all(cls):
        """
        关闭浏览器并销毁对象
        :return:
        """
        if cls._page:
            cls._page.close()
            cls._page = None
        if cls._context:
            cls._context.close()
            cls._context = None
        if cls._browser:
            cls._browser.close()
            cls._playwright.stop()
            cls._browser = None
            cls._playwright = None
