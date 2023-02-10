#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
class Solution(object): # 双指针
    def sortColors(self, nums):
        zero = 0 # zero指向第一个1的位置（0串的末尾）
        two = len(nums) - 1 # two指向第一个非2的位置
        i = 0 # 用i对nums进行遍历
        while i <= two: # 然后使用i从头到尾扫一遍，直到与two相遇
            if nums[i] == 0: # i遇到0就换到左边去
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1 
                zero += 1
            elif nums[i] == 1:  # 遇到1就跳过
                i += 1
            elif nums[i] == 2: # 遇到2就换到右边去
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1
# @lc code=end

