#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子数组和
#

# @lc code=start
'''
动态规划
明显的DP方法去解决。

通过构建一个和原长一样长的数组， dp 数组的含义是以 dp[i] 为结尾的最大子数组的和。

状态转移公式：

dp[i] = dp[i - 1] + nums[i] 当 nums[i] >= 0 。
dp[i] = nums[i] 当 nums[i] < 0 。
题目求的最大子数组的和，就是 dp 数组的最大值。
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: # 如果为空
            return 0

        N = len(nums)
        cur, prev = 0, 0
        res = float("-inf")
        for i in range(N):
            cur = nums[i] + (prev if prev > 0 else 0) # 如果之前的加起来大于0，那可以继续；如果小于0，那不继续，默认为0，重新开始往后找？
            prev = cur
            res = max(res, cur)
        return res
s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
re = s.maxSubArray(nums)
print(re)
# @lc code=end

