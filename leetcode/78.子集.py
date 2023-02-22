#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object): # 递归
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 当前的元素一定使用，
        # 然后递归把后面的元素是否选择一些放入当前元素后面。
        res = [] # 初始化result的空list
        self.dfs(nums, 0, res, []) # 递归
        return res

    def dfs(self, nums, index, res, path):
        res.append(path)
        # 在当前index元素使用的情况下，
        # 从nums的index后面
        # 抽取0个或者全部数字放入path的后面，
        for i in range(index, len(nums)): 
            self.dfs(nums, i + 1, res, path + [nums[i]])

# @lc code=end

