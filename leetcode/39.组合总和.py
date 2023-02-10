#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        res = [] # 初始化返回的结果的list
        candidates.sort() # 将数组进行排序（由小到大）
        self.dfs(candidates, target, 0, res, []) # 递归
        return res # 返回res
    
    def dfs(self, nums, target, index, res, path): # 递归
        if target < 0: # 如果目标值小于0，找不到的（因为默认数组里都是正数）
            return 
        elif target == 0: # 如果目标值等于0，说明找到了一组path了
            res.append(path) # 把path（空list）append到res上
            return 
        
        for i in range(index, len(nums)):
            if nums[index] > target: # 如果当前index上的数组的值大于目标值，说明没得找了
                return # 返回空值（path退回上一个值，target也退回减去之前）为啥？？
            # 如果不满足上面那条，就说明还能找
            # 把target减去当前i上值，作为新的target; i作为新的index; 再调用dfs，再次递归找合适的path
            self.dfs(nums, target - nums[i], i, res, path + [nums[i]])
s = Solution()
candidates = [2,3,6,7]
target = 7
re = s.combinationSum(candidates, target)
print(re)
# @lc code=end