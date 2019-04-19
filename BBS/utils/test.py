# _*_ coding: utf-8 _*_
# @time     : 2019/04/18
# @Author   : Amir
# @Site     : 
# @File     : test.py
# @Software : PyCharm

# import string
#
# # 得到大小写字母的列表
# source = list(string.ascii_letters)
# print('string.ascii_letters:', string.ascii_letters)
# print('source:', source)
# # 得到大小写字母的列表 + 0到9的数字字符串
# source.extend(map(lambda x: str(x), range(0, 10)))
# # 随机取六位作为验证码
# # captcha = "".join(random.sample(source, 6))
#
#
# p = map(lambda x: str(x), range(0, 10))
# print(p)
# print(list(p))


# print(type(0b00000001))


import memcache


# 建立连接
mc = memcache.Client(['127.0.0.1:11211'], debug=True)

# 设置数据
mc.set('username', 'amir', time=120)

print(mc.get('username'))