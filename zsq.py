# coding=utf-8
import codecs

import chardet


# 定义一个装饰器
def zsq(func):
	# 创建一个新的函数
	def new_func(*args, **kwargs):
		# 开始装饰
		print('装饰')
		# 执行原函数
		return func(*args, **kwargs)
	
	# 返回新函数
	return new_func

