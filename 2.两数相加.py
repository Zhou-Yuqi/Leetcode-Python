#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution(object): # 递归
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         add = l1.val + l2.val
#         res = ListNode(add % 10)
#         res.next = self.addTwoNumbers(l1.next, l2.next)
#         if add >= 10:
#             res.next = self.addTwoNumbers(res.next, ListNode(1))
#         return res       
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        add = l1.val + l2.val
        res = ListNode(add % 10)
        res.next = self.addTwoNumbers(l1.next, l2.next)
        if add >= 10:
            res.next = self.addTwoNumbers(res.next, ListNode(1))
        return res
# s = Solution()
# # l1 = ListNode([2,4,3])
# # l2 = ListNode([5,6,4])
# re = s.addTwoNumbers(l1, l2)
# print(re)
# @lc code=end

