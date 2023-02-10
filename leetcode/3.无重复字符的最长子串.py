#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0 # 左指针，右指针
        res = 0 # 初始化返回的result
        chars = dict() # 初始化空字典：value为值，key为索引
        for right in range(len(s)): # 右指针遍历长度
            if s[right] in chars: # 如果右指针指向的值在字典里了, 如果这个字符在字典中，说明这个字符在前面出现过，即这个区间已经不是题目要求的不含重复字符的区间了，因此，需要移动left
                left = max(left, chars[s[right]] + 1) # 移动left到哪里呢？有个快速的方法，那就是移动到right字符在字典中出现的位置（即s[right]在前面的位置）的下一个位置。
            chars[s[right]] = right # 把right指向的值加到字典里
            res = max(res, right - left + 1) # 计算当前区间的长度，是否比上一次的res要长
        return res
# @lc code=end

