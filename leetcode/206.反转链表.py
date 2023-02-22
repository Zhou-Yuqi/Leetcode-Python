#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object): # 迭代。迭代解法，每次找出老链表的下一个结点，插入到新链表的头结点，这样就是一个倒着的链。
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1) # 定义一个虚拟结点dummy。
        while head: # 只要原始链表不是空
            nodenext = head.next # nodenext记录原始head往下的顺序
            head.next = dummy.next # 将head的下一个，指向dummy.next。其实dummy.next就是用来维护当前head值得。因为要反转
            dummy.next = head # 维护dummy的下一个，一直指向head当前的值
            head = nodenext # 移动head到原始顺序中的下一个地方
        return dummy.next
        
# @lc code=end

