import inspect
import json
import os
import re
import sys

from utils.config import ConfigParser
from utils.logging import logger


class BaseCase:
    """
    测试用例基类
    """

    @staticmethod
    def get_stack():
        """
        获取调用栈
        """
        frame_info_list = inspect.stack()
        for frame_info in frame_info_list:
            if frame_info.function in ['_importtestmodule', 'runtest', 'pytest_fixture_setup', 'collect']:
                f_locals = frame_info[0].f_locals
                stack_info = f_locals.get('self')
                if not stack_info:
                    stack_info = f_locals.get('request')
                return stack_info
        else:
            raise Exception('不能从调用栈中获取到目标值！')

    @classmethod
    def parameters(cls):

        stack_info = cls.get_stack()
        case_file_dir = stack_info.fspath.dirname
        case_file_name = stack_info.fspath.basename
        env = cls.env()
        with open(os.path.join(case_file_dir, 'parameter.json'), 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            return json_data.get(env.lower()).get(case_file_name)

    @staticmethod
    def env():
        """
        获取env（环境标识 qa/ol）
        """
        try:
            stack_info = BaseCase.get_stack()
            env = stack_info.config.option.env
        except Exception as e:
            logger.error(f"获取env失败，报错信息：{e}")
            env = ConfigParser().get_config(sector='env', item='default')
            logger.info(f"获取env失败，使用默认env：{env}")
        return env

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass
