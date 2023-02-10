#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.lower_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def lower_bound(self, nums, target):
        left, right = 0, len(nums) # 初始化左右指针为最左和最右加1
        while left < right: # 如果左指针小于右指针
            mid = int(left + (right - left) / 2) # mid为left和right之间的中间位置
            if nums[mid] < target: # 如果mid位置的值比target小，那就说明target只有可能在mid的右边
                left = mid + 1 # 左指针移动到mid右边的位置，接下来在右边找就行
            else: # 如果mid位置的值比target还要大（或者等于），那就说明target只有可能在mid左边
                right = mid # 右指针移动到mid上，接下来往左边找就行
        return left

    def higher_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left    
# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         left = self.lowwer_bound(nums, target)
#         right = self.higher_bound(nums, target)
#         if left == right:
#             return [-1, -1]
#         return [left, right - 1]
    
#     def lowwer_bound(self, nums, target):
#         # find in range [left, right)
#         left, right = 0, len(nums)
#         while left < right:
#             #mid = left + (right - left) / 2
#             mid = left + (right - left) / 2
#             mid = int(mid)
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left
    
#     def higher_bound(self, nums, target):
#         # find in range [left, right)
#         left, right = 0, len(nums)
#         while left < right:
#             mid = left + (right - left) / 2
#             mid = int(mid)
#             if nums[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left  
s = Solution()
nums = [5,7,7,8,8,10]
target = 8
re = s.searchRange(nums, target)
print(re)
# @lc code=end

