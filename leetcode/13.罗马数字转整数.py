#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s): # 从后向前遍历
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = roman[s[-1]] # 字符串的最后一个字符，所对饮的数字
        N = len(s)
        for i in range(N-2, -1, -1): # 从字符串的倒数第二个字符开始，反向遍历，直到0处（也即第一个字符）
            if roman[s[i]] < roman[s[i+1]]: # 如果当前位置的字符，比右边的字符，对应的数字要小
                res -= roman[s[i]] # 减掉当前位置的值
            else:
                res += roman[s[i]]
        return res

# @lc code=end

