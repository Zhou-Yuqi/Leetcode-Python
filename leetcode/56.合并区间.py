#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
# Definition for an interval.
class Solution(object):
    def merge(self, intervals):
        out = []
        for i in sorted(intervals):
            if out and i[0] <= out[-1][1]: # 如果out不是空的，且，i的左值小于等于out最后一个区间的右值
                out[-1][1] = max(out[-1][1], i[1]) # out最后一个区间的右值，取，当前值和i区间右值得最大值
            else:
                out += [i] # 把i加到out里
        return out
s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
re = s.merge(intervals)
print(re)

# @lc code=end

