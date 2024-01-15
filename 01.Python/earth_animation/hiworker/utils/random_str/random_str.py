import random


def random_str(num):
    """
    生成一定长度的随机字符串
    :param num: 需要生成的字符串长度
    :return:
    """
    h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(h)

    return salt
