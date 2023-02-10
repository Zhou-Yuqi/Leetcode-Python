#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):# 相当于，左指针去找，有没有等于val的，没有就前进，有就把右指针的数值换到这来，进入下一次搜索
        N = len(nums)
        l, r = 0, N - 1 # 左指针指向0，右指针指向最右边
        while l <= r: # 如果左指针小于等于右指针
            if nums[l] == val: # 如果左指针的值等于val
                nums[l] = nums[r] # 把右指针的值赋给左指针的位置
                r -= 1 # 右指针向左移一个【注意，左指针不动哈】
            else: # 如果左指针的值不等于val
                l += 1 # 左指针向右移一个
        return l
# @lc code=end

