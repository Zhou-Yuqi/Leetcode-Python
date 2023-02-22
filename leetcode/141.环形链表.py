#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): # 双指针。快慢指针。
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: # 如果头结点不是空的，那么整个链表就不是空的（其实头结点就是链表的起始）
            return False
        slow, fast = head, head.next
        while fast and fast.next: # 如果快指针不是空，且快指针下一个也不是空（就保证快指针的下一个还存在）
            if fast == slow:
                return True
            fast = fast.next.next # 快指针跳两个
            slow = slow.next # 慢指针跳一个。【其实也就是，如果当前存在环的话，fast到下一个，再到下一个，这个结果就是slow的下一个的话，那么就存在环】
            # 搞不懂！背着吧！
        return False # 如果都找遍了都没有，那就是没了
        
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

s = Solution()
re = s.hasCycle(node1)
# @lc code=end

