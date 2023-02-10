#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         return haystack.find(needle) # python现成的find函数，直接能够返回要求的东西
class Solution:
    def strStr(self, haystack, needle): # 自己实现find函数
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        M, N = len(haystack), len(needle)
        for i in range(M - N + 1): # 注意，遍历的范围是M-N+1（因为M-N+1 - 1 + N = M,刚好是能取到的尾部索引（开区间）)
            if haystack[i : i + N] == needle: # 如果从i开始，到i+N位置，都是和needle相同
                return i # 那么返回i就好
        return -1
# @lc code=end

