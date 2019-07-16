# *_*coding:utf-8 *_*
# date:
__author__ = 'beiliangshizi'

# 题目描述
# 假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，形成一个数组如下：
# a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy
# 其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，输入是任意一个编码，输出这个编码对应的Index.
# 输入描述:
# 输入一个待编码的字符串,字符串长度小于等于100.
# 输出描述:
# 输出这个编码的index
# 示例1
# 输入
#
# baca
# 输出
#
# 16331

def f(string):
    _sum = 0
    curSum = 0
    for i in range(4):
        curSum *= 25
        if i < len(string):
            curSum += ord(string[i]) - ord("a")
        _sum += curSum
        if i < len(string) - 1:
            _sum += 1
    return _sum


if __name__ == "__main__":
    string = raw_input()
    print f(string)