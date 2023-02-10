#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
'''
之前的【LeetCode】46. Permutations 解题报告是没有重复数字的，这个题有重复数字。
我的做法很简单，就是在以前的基础上加了一个判断条件：path not in res。
这样的做法是在每个path生成之后才去做的判断，因此效率一点都不高。
最后竟然也能通过了。
'''
class Solution(object): # 递归
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, res, [])
        return res
    
    def helper(self, nums, res, path):
        if not nums and path not in res: # 如果nums不是空的，且，path不在res里（用于 在每个path生成之后才去做的判断）
            res.append(path)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i] + nums[i+1:], res, path + [nums[i]])

# @lc code=end

