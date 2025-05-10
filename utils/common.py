import datetime
import random
import time


def ts_10():
    """
    生成10位时间戳
    """
    return int(time.time())


def ts_13():
    """
    生成13位时间戳
    """
    return int(time.time() * 1000)


def random_integer():
    """
    随机整型
    """
    return random.randint(1, 900000)


def is_chinese(word):
    """
    判断字符串是否包含中文
    """
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def current_time_format():
    """
    当前时间格式化
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def current_time_format_ms():
    """
    当前时间格式化 毫秒级
    """
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")


def datestamp_to_datetime(datestamp):
    """
    时间戳转日期时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datestamp))


def time_start_end(type=1, num=1000, hours=0, days=0, minutes=0, seconds=0):
    """
    获取动态时间
    :param type: 不传默认为1，格式类型，1为格式2020/07/15 16:12:10 2为时间戳
    :param num: 不传默认为1000，即时13位时间戳  如需10位 num=1
    :param hours: 不传默认为0，前后2小时 ±2
    :param days: 不传默认为0，前后2天 ±2
    :param minutes: 不传默认0，前后2分钟 ±2
    :param seconds: 不传默认0，前后2秒 ±2
    :return:
    """
    if type == 1:
        # 时间入参方法:"2020/07/15 16:12:10"前/后1小时半，Time_Start_End(minutes=±90) or Time_Start_End(hours=±1,minutes±30)
        t = (datetime.datetime.today() + datetime.timedelta(days=days, hours=hours, minutes=minutes,
                                                            seconds=seconds)).strftime('%Y-%m-%d %H:%M:%S')
        return t
    elif type == 2:
        # 函数功能：获取当前时间的时间戳（13位）
        # 13位时间戳的获取方式跟10位时间戳获取方式一样
        # 两者之间的区别在于10位时间戳是秒级，13位时间戳是毫秒级
        t = (datetime.datetime.today() + datetime.timedelta(days=days, hours=hours, minutes=minutes,
                                                            seconds=seconds)).strftime('%Y-%m-%d %H:%M:%S')
        timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
        c = int(time.mktime(timeArray)) * num
        return c
