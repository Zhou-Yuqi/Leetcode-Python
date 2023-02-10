#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums): # 贪心算法
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        for i, num in enumerate(nums):
            if i > reach: # 如果当前位置的索引大于能达到的最大reach
                return False
            reach = max(reach, i + num) # 维护reach，为当前索引+能够移动的步数 和， 与， 当前reach的最大值
        return True
# @lc code=end

