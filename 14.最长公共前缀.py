#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        pre = min(strs, key = len) # 用长度去找最小的词
        for i, c in enumerate(pre): # 遍历最短长度的词，i为索引、c为单词
            for word in strs: # 遍历strs里的每一个单词
                if word[i] != c: # 如果该单词的第i索引的字符，不等于c
                    return pre[:i] # 返回pre的i位置之前的东西（因为如果等于的话，会一直遍历一直找
        return pre # 如果都遍历完了都满足，那么说明这个最短的单词就是公共前缀
# @lc code=end

