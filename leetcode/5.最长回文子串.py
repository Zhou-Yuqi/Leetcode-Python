#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
'''
动态规划：

dp[i, j] = 1                                        if i == j
         = s[i] == s[j]                             if j = i + 1
         = s[i] == s[j] && dp[i + 1][j - 1]         if j > i + 1 
'''
class Solution(object):
    def longestPalindrome(self, s): # 动态规划
        if len(set(s)) == 1: # 如果数组的不重复的字符的长度都是1，那就说明这个字符串都是一样的字符
            return s # 那么返回原始字符串就可以了
        
        n = len(s) # 计算字符串的长度
        start, end, maxL = 0, 0, 0
        dp = [[0] * n for _ in range(n)]
        print(dp)
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[i] == s[j]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i] and maxL < i - j + 1:
                    maxL = i - j + 1
                    start = j
                    end = i
            dp[i][i] = 1
        return s[start: end + 1]
s = Solution()
s1 = "babad"
re = s.longestPalindrome(s1)
print(re)
# @lc code=end

