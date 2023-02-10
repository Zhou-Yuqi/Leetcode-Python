#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        xs = str(x)
        xs_2 = xs[::-1]
        if xs == xs_2:
            return True
        else:
            return False
# @lc code=end

