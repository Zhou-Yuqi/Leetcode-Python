#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        N = len(nums) # 数组的长度
        nums.sort() # 数组排序，从小到大
        res = [] # 初始化结果空list
        i = 0 # 第一个固定指针
        while i < N - 3: # 如果第一个固定指针指向的数是在倒数第三个数之前的
            j = i + 1 # 第二个固定指针为第一个固定指针右边的
            while j < N - 2: # 如果第二个固定指针指向的数是在倒数第二个数之前的
                k = j + 1 # 左指针，初始值为第二个固定指针右边一个
                l = N - 1 # 右指针，初始值为长度-1，即指向最后一个数
                remain = target - nums[i] - nums[j] # remain为target减掉两个固定指针数的结果，即左右指针找其和为remain即可
                while k < l: # 如果左指针小于右指针
                    if nums[k] + nums[l] > remain: # 如果结果大了
                        l -= 1 # 右指针退一个
                    elif nums[k] + nums[l] < remain: # 如果结果小了
                        k += 1 # 左指针加一个
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        
                        # 去掉重复的情况
                        while k < l and nums[k] == nums[k + 1]: # 如果左指针小于右指针，且左指针下一个数值与当前左指针数值相同
                            k += 1 # 左指针再加一个，代表跳过这次搜索
                        while k < l and nums[l] == nums[l-1]: # 如果左指针小于右指针，且右指针退一个的数值与当前右指针的数值相同
                            l -= 1 # 右指针再退一个，代表跳过这次搜索
                        
                        # 去掉重复情况后，再
                        k += 1 # 右移左指针
                        l -= 1 # 左移右指针
                # 去掉第二个固定指针的重复情况
                while j < N - 2 and nums[j] == nums[j + 1]:
                    j += 1
                # 去掉之后，再
                j += 1 # 第二个固定指针加一
            # 去掉第一个固定指针的重复情况
            while i < N - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res
# @lc code=end

