#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object): # 递归
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = [] # 初始化result的空list
        self.helper(range(1, n + 1), k ,res, [])
        return res

    def helper(self, array, k, res, path):
        if k > len(array):
            return 
        if k == 0:
            res.append(path)
        else:
            self.helper(array[1:], k - 1, res, path + [array[0]])
            self.helper(array[1:], k , res, path)


# @lc code=end

