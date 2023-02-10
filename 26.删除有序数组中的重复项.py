#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        N = len(nums) # 数组的长度
        if N <= 1: # 如果数组长度都小于等于1
            return N # 那就不用去删除了，直接返回这个值就行了
        left, right = 0, 1 # 左指针、右指针初始值分别为0,1； left其实是用来存储最终返回的不重复数组的长度的
        while right < N: # 如果右指针小于数组长度（也就是能够指向数组最后一个元素）
            # 排除重复情况
            while right < N and nums[right] == nums[left]: # 如果左指针指向的数和右指针指向的数是一样的
                right += 1 # 右指针向右边挪一个
            # 排除掉重复之后
            left += 1 # 再把左指针向右边挪一个，实际上是计算数组的长度
            if right < N: # 如果排除了重复之后的右指针，还是能指向数组的最后一个数的话
                nums[left] = nums[right] # 把左指针位置上的数字，替换成右指针上的数字，也即原地替换
        return left
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
s.removeDuplicates(nums)
# @lc code=end

