#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
        
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): # 双指针
    def removeElements(self, head, val):
        # 创建一个虚拟结点
        dummy = ListNode(-1)
        dummy.next = head
        # pre，头结点（指针），指向虚拟节点
        pre = dummy
        # cur，指针，指向原始的链表的第一个节点
        cur = head
        while cur: # 只要cur不是空（保证能指向原始链表的最后）
            # 开始判断cur是否需要跳过
            if cur.val == val: # 如果当前节点的值，跟想要找的一样
                pre.next = cur.next # 虚拟节点，的下一个，指向cur的下一个（本质上就是跳过了cur）
            else: # 如果不一样
                pre = pre.next # 头节点向后移一个
            cur = cur.next # cur往后移动，遍历cur，去判断需不需要移除
        return dummy.next

# @lc code=end

