#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
# import re
# class Solution(object):
#     def myAtoi(self, s):
#         num = num.strip() # 去掉前后的空格
#         if not num: # 如果是空的，直接返回0，不用操作了
#             return 0
#         # 如果不是空的，才继续
#         res = re.findall(r"^[+-]?\d+", num) # 使用正则表达式找出"+", "-", 数字 开始，到第一个非数字字符处停止的数字。该正则是 "^[+-]?\d+"，可以用 http://tool.chinaz.com/regex/ 进行校验。
#         if not res: # 如果匹配完，是空的，直接返回0，不用操作了
#             return 0
#         res = int(res[0]) # list的第一个字符串转int
#         return max(min(res, 2 ** 31 - 1), -2 ** 31) # 返回在范围内的值
import re
class Solution(object):
    def myAtoi(self, num):
        num = num.strip()
        if not num:
            return 0
        res = re.findall(r"^[+-]?\d+", num)
        if not res:
            return 0
        res = int(res[0])
        return max(min(res, 2 ** 31 - 1), -2 ** 31)

# @lc code=end

