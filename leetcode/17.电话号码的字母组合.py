#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object): # 循环
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        # 定义字典（哈希表）
        d = {'2': "abc", '3': "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}
        # 初始化res
        res = ['']
        for e in digits:
            res = [w + c for c in d[e] for w in res] # 取出res里每个字符，拼接上，数字串里每一个数字他所对应的字母组，对这个字幕组遍历每个结果
        return res
# @lc code=end

