#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0: # 如果nums1和nums2里都还有数
            if nums1[m - 1] > nums2[n - 1]: # 从最后开始比。如果nums最后一个（m-1）数比nums2最后一个（n-1）的要大，就说明要把nums当前这个m-1位置的值，往后稍稍
                nums1[m + n - 1] = nums1[m - 1] # 把nums1在m-1位置的数值，放到最后（m+n-1）去
                m -= 1 # 就当指针用了，虽然它是传进来的nums1长度，也可以把它回退一个
            else: # 如果nums1后面的数值比nums2后面的数值要小，就说明nums2的值放在nums1最后面（m+n-1）就行
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1 # 当指针用了，回退
        nums1[:n] = nums2[:n] # 如果n没遍历完的话，就说明nums1已经遍历完了，且都已经插进去合适的位置了
                              # 那就要处理一下nums2前面这段没遍历的部分。
                              # 把nums2之前这段放在nums1最前面这段，就可以了。（因为nums2是有序的）
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s = Solution()
re = s.merge(nums1, 3, nums2, 3)
# @lc code=end

