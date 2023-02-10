#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums) - 1 # 左右指针初始化为最左边和最右边
        while left <= right: # 如果左指针小于等于右指针，才进行
            mid = (left + right) / 2 # 计算两个指针的中间位置（那如果是小数咋办？）
            if nums[mid] == target: # 如果中间位置是target值
                return mid
            if nums[mid] < nums[right]: # 如果中间位置值小于右指针位置的值，说明从mid到right都是按升序的，还没找到旋转点
                if target > nums[mid] and target <= nums[right]: # 如果target在mid和right指向的值之间，说明target存在，
                    left = mid + 1 # 左指针变为mid右边的一个，接下来在这里面找就可以了
                else: # 如果target不在这之间，那就说明target只可能存在在前面那段，那就在前面找
                    right = mid - 1
            else: # 如果中间位置值大于等于右指针位置的值，说明旋转点肯定在mid这或者前面
                if target < nums[mid] and target >= nums[left]: # 如果target值在左指针和mid指向的值之间，说明targte存在，
                    right = mid - 1 # 右指针变为mid左边的一个，接下来在前面这里面找就可以了
                else: # 如果target值不在这之间，那就说明target只可能在后面那段，那就去后面那段找
                    left = mid + 1
        return -1 # 如果啥也找不到了，那就说明target不在里面，返回-1
# @lc code=end

