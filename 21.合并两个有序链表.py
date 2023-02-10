#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution: # 递归
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1 and not l2: # 如果两个有序链表都为空
#             return None
#         elif not l1: # 如果l1为空
#             return l2
#         elif not l2: # 如果l2为空
#             return l1
#         if l1.val <= l2.val: # 如果l1的head小于等于l2的head
#             node = l1 # 当前节点设置成为l1的head
#             node.next = self.mergeTwoLists(l1.next, l2) # 当前节点的下一节点，使用递归，继续合并l1下一节点之后的链表，和，l2的部分
#         else:
#             node = l2 # 当前节点设置成为l2的head
#             node.next = self.mergeTwoLists(l2.next, l1) #递归，同理
        
#         return node # 返回新生成的链表node 

'''
way2: 迭代
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0) # 定义新链表，head为0
        move = head # 维护move，当前move指向head的根节点
        if not l1: return l2
        if not l2: return l1
        while l1 and l2: # 如果l1和l2都不是空的
            if l1.val < l2.val: # 如果l1的当前节点小于l2当前的节点
                move.next = l1 # move的后一个节点为l1当前节点
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next # 维护move，move移动到下一个节点处
        # 如果l1和l2有一个是空的
        move.next = l1 if l1 else l2 # 如果l1不是空的，那就把l1补上；如果l2不是空的，那就把l2补上（反正他俩是有序的，直接拼即可）
        return head.next
l1 = ListNode(1)
l1.next = 2
l1.next = 4

l2 = ListNode(1)
l2.next = 3
l2.next = 4

s = Solution()
re = s.mergeTwoLists(l1, l2)
#print(l1.val)
#l1 = [1,2,4]
#l2 = [1,3,4]


# class Solution: # 递归
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1 and not l2:
#             return None
#         elif not l1:
#             return l2
#         elif not l2:
#             return l1
#         if l1.val <= l2.val:
#             node = l1
#             node.next = self.mergeTwoLists(l1.next, l2)
#         else:
#             node = l2
#             node.next= self.mergeTwoLists(l1, l2.next)
#         return node

# @lc code=end

