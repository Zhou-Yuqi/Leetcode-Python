#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        '''
        nums: List
        target: int

        Return:
        List
        '''
        N = len(nums)
        pos = dict() # 定义空字典，key是数字、value是数字对应的索引
        for i, num in enumerate(nums): # enumerate 数组
            if target - num in pos: # 如果差值在字典里
                return [pos[target-num], i] # 去字典里找这个差值在原始数组里的索引，返回，并且也返回当前i这个索引
            else: # 如果差值没有在这个字典的key里
                pos[num] = i # 把当前的数值作为key、当前数值的索引作为value，存在字典里
                             # 其实就是说明，当前遍历到这个位置的时候，这个位置的数值可能还有可能在后面被用上嘛
                             # 如果说，先创造一个字典，包含数组里面的所有值和索引，那就太慢了
                             # 这样做会快一点哈
        return [0, 0]
# s = Solution()
# result = s.twoSum([3,2,4],6)
# print(result)
# @lc code=end

