# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 将一句话的单词进行倒置，标点不倒置。比如 I like beijing. 经过函数后变为：beijing. like I
# 输入描述:
# 每个测试输入包含1个测试用例：  I like  beijing. 输入用例长度不超过100
# 输出描述:
# 依次输出倒置之后的字符串,以空格分割
# 示例1
# 输入
#
# I like  beijing.
# 输出
#
# beijing. like I

string=raw_input()
string_list=list(string.strip().split())
string_list.reverse()
new_string=' '.join(string_list)
print new_string