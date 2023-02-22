#
# @lc app=leetcode.cn id=80 lang=python
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
# class Solution(object): # 双指针
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         N = len(nums)
#         if N <= 1: # 如果长度小于等于1，不用搞了
#             return N
#         left, right = 0, 1 # 双指针。left指针指向第一个要判断的位置；right指针指向后面的位置。
#         while right < N: # 如果left指针能遍历完
#             while right < N and nums[right] == nums[left]: # 如果right指针能遍历完，且，两个指针指向的数值一样
#                 right += 1
#             # 直到right和lieft不等的时候
#             left += 1
#             if right < N: # 再次判断，right移动之后，是否还满足能遍历完的条件
#                 nums[left] = nums[right] # 把后面这个数值移到前面来
#         return left
# s = Solution()
# nums = [0,0,1,1,1,1,2,3,3]
# re = s.removeDuplicates(nums)
class Solution(object): # 双指针
    def removeDuplicates(self, nums):
        i = 0 # 其实i就是n数值的索引
        for n in nums: # 遍历nums中的数值
            if i < 2 or n != nums[i - 2]: # 如果出现i小于2，或者，(i大于等于2的时候）,n不等于i-2处的值，即，i处指向的值（n），跟i前两个位置的值nums[i-2]，不同的话，就说明是可以的
                nums[i] = n # 
                i += 1
        return i
s = Solution()
nums = [0,0,1,1,1,1,2,3,3]
re = s.removeDuplicates(nums)
# 【理解】
# i是用来存储索引的，当不满足条件的时候，i就会指向00 11 后面那个地方的位置，直到遍历出来的n的值，跟i-2处的值不同，才把这个n放在i处
#   指针1：（慢指针）i，指向了不满足题目要求的第一个位置
#   指针2：（快指针）for n in nums，对所有的数字进行遍历
# 这样当遍历到一个新的数字而且这个新的数字和慢指针指向的前两个数字不同时，把它交换到这个不满足的位置，然后两个指针同时右移即可。
# @lc code=end

