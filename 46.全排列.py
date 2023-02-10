#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
# '''
# 方法1：库函数
# '''
# from itertools import permutations
# class Solution(object):
#     def permute(self, nums):
#         return list(permutations(nums))

# '''
# 方法2：回溯法
# '''
# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         visited = [0] * len(nums)
#         res = []
        
#         def dfs(path):
#             if len(path) == len(nums):
#                 res.append(path)
#             else:
#                 for i in range(len(nums)):
#                     if not visited[i]:
#                         visited[i] = 1
#                         dfs(path + [nums[i]])
#                         visited[i] = 0
        
#         dfs([])
#         return res

'''
方法三：递归
'''
class Solution(object):
    def permute(self, nums):
        res = [] # 初始化result的list
        self.dfs(nums, res, []) # 开始递归
        return res

    def dfs(self, nums, res, path): 
    # dfs()是对nums进行全排列，已有的排列结果放到path中，
    # 当nums为空时说明递归完成，把path放入res中。
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i+1:], res, path + [nums[i]])

s = Solution()
nums = [1,2,3]
re = s.permute(nums)
print(re)
# @lc code=end

