#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        N = len(nums) # 数组长度
        nums.sort() # 从小到大排序
        res = [] # 初始化返回的结果，用于储存后面和为0的三个数
        for t in range(N-2): # 从头遍历到倒数第三个数（相当于先固定一个数，之后再用双指针）
            if t > 0 and nums[t] == nums[t-1]: # 如果当前位置的数大于0，并且这个数还和上一个位置的数值一样
                continue # 跳出此次for循环
            i, j = t+1, N-1 # 左指针为t+1、右指针为N-1
            
            while i<j: # 如果左指针小于右指针
                _sum = nums[t]+nums[i]+nums[j] # 计算当前三数求和值
               
                if _sum == 0: # 如果和等于0，说明成了
                    res.append([nums[t], nums[i], nums[j]]) # 返回一组和为0的数
                    # 继续向下搜索，还有没有能成的
                    i += 1 # 左指针加一
                    j -= 1 # 右指针减一
                    while i < j and nums[i] == nums[i-1]: # 如果左指针比右指针小，且向右移后左指针的数值跟没移之前的一样
                        i += 1 # 左指针再向右移一个
                    while i < j and nums[j] == nums[j+1]: # 如果左指针比右指针小，且向左移后右指针的数值跟没移之前的一样
                        j -= 1 # 右指针再向左移一个
                
                elif _sum<0: # 如果和小于0，说明还没加够，左指针再向右移一个
                    i += 1

                else: # 如果和大于0，说明加多了，右指针向左退一个
                    j -= 1
        return res
# @lc code=end

