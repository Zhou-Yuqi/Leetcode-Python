#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        flag = 1 # 标记这个数是正数
        if x < 0:
            flag = -1 # 标记这个数是负数
            x = -x
        r = int(str(x)[::-1]) # 把数字翻转过来
        if flag == 1 and r < 2**31 - 1: # 如果是正数
            return r
        elif flag == -1 and -r >= -2**31: # 如果是负数
            return -r
        return 0

# @lc code=end

