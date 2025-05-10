import base64

import pytest
from py._xmlgen import html

from utils.common import current_time_format
from utils.config import ConfigParser


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    """
    对报告中表格的表头进行修改 增加Description和Time列
    @param cells:
    @return:
    """
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    """
    对报告中表格的每一行进行修改 增加Description和Time列结果
    """
    if hasattr(report, 'description'):
        cells.insert(2, html.td(report.description))
    else:
        cells.insert(2, html.td(''))
    cells.insert(3, html.td(current_time_format(), class_='col-time'))
    cells.pop()


def pytest_addoption(parser):
    """
    添加命令行自定义参数 允许case接受的环境参数
    """
    parser.addoption(
        "--env",
        action="store",
        default=ConfigParser.get_config(sector='env', item='default'),
        choices=['ol', 'qa'],  # 2:测试环境 4:生产环境
        help="assign which env to use",
    )


@pytest.fixture(scope='session')
def env(pytestconfig):
    env = pytestconfig.getoption('--env')
    return env


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    在case指定成功或者失败时都截图 report中
    """
    # 获取钩子方法的调用结果
    outcome = yield
    report = outcome.get_result()

    pytest_html = item.config.pluginmanager.getplugin('html')
    extra = getattr(report, 'extra', [])

    report.description = str(item.function.__doc__)
    if report.when in ['call', 'setup']:
        print('测试报告：%s' % report)
        print('步骤：%s' % report.when)
        print('nodeid：%s' % report.nodeid)
        print('description:%s' % str(item.function.__doc__))
        print(('运行结果: %s' % report.outcome))

        screen = _capture_screenshot_as_base64(request=item)
        extra.append(pytest_html.extras.png(screen))

    report.extra = extra


def _capture_screenshot_as_base64(request):
    """
    获取base64截图
    """
    if hasattr(request.module, "BrowserFactory"):
        browser = getattr(request.module, "BrowserFactory")
        if browser:
            try:
                screenshot_bytes = browser.get_page().screenshot()  # 修改后的代码
                return base64.b64encode(screenshot_bytes).decode()
            except Exception as e:
                print(f"base64 截图失败:{e}")
                return ''
    else:
        return ''
