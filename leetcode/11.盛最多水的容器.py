#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        ans = 0 # 初始化答案
        l = 0 # 左指针
        r = len(height) - 1 # 右指针
        while l < r:
            ans = max(ans, min(height[l], height[r])*(r-l)) # 更新最大面积
            if height[l] < height[r]: # 如果右指针的高度大于左指针的高度
                l += 1
            else: # 如果左指针的高度大于右指针的高度
                r -= 1
        return ans
# @lc code=end

