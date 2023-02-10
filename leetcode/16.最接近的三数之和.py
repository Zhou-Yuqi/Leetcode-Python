#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        N = len(nums) # 数组的长度
        nums.sort() # 排个序，从小到大
        res = float('inf') # 将结果先初始化为正无穷，res一会儿用来存三个数的和
        for t in range(N): # 固定一个数
            i, j = t+1, N-1 # 双指针，初始值：左指针为固定数右边的一个、右指针为数组最后一个数
            while i < j: # 如果左指针小于右指针
                _sum = nums[t] + nums[i] + nums[j] # 三数之和
                if abs(_sum - target) < abs(res - target): # 如果当前三数之和比res（无穷大）更接近target值
                    res = _sum # 重新赋值res
                if _sum > target: # 如果和太大了
                    j -= 1 # 右指针向左退一个
                elif _sum < target: # 如果和太小了
                    i += 1
                else: # 如果和就等于target了
                    return target # 直接返回target值就行了（其实也是和值啦）
        # 如果for循环都遍历完了，还是没有和为target的
        return res # 那就摆烂了，返回一个最接近的了
# @lc code=end

