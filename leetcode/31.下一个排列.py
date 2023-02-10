#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums) # 数组的长度
        i = n - 1 # 数组最后一个位置的索引
        while i > 0 and nums[i] <= nums[i-1]: # 指针从后向前搜索，如果当前位置指针所指向的值比前一个指针指向的值要小（即降序）
            i -= 1 # 指针向左退一个（即一直找，找到不满足从后向前降序为止）
        # 现在i指向的地方，左边开始，已经不满足降序了，那就把i到最后(n-1)位置的值都反过来，做reverse操作
        self.reverse(nums, i, n-1)
        if i > 0: # 如果指针指向非第一个位置
            for j in range(i, n): # j遍历i到数组的最后个位置
                if nums[j] > nums[i-1]: # 一旦后面这个j指向的值大于i-1位置的值
                    self.swap(nums, i-1, j) # 把j和i-1位置的值调换，以找到下一个排列
                    break # 跳出for循环

    def reverse(self, nums, i ,j):
        #for k in range(i, (i + j) / 2 + 1): # 普通range里如果有小数点的数，会报错
        import numpy as np # 改用numpy
        for k in np.arange(i, (i + j) / 2 + 1): # 如果用np的话，k为float
            k = int(k) # 在swap前，需要把k转换成int
            self.swap(nums, k, i+j-k)
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
s = Solution()
nums = [1,2,3]
result = s.nextPermutation(nums)
print(result)
print(nums)
# @lc code=end

