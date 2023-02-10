#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for string in strs: # 遍历strs里的每一个单词
            sorted_str = ''.join(sorted(string)) # 把单词的字母排序之后，将这个排序后的“set”单词，作为res的key
            res[sorted_str].append(string) # 再把当前这个单词，append到defaultdict里key为res下的value里。
        return res.values() # 返回defaultdict的values，即为所有可能的字母单词们，而且是一组一组划分好的。
# @lc code=end

