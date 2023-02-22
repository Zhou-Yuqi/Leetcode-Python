#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# way 1：判断相邻节点是否相等
# 如果下一个元素和这个元素的值相等，这个元素的下个元素就等于下个元素的下个元素。再循环就好了。
# 在找到不同的元素之前，当前元素不走。找到之后再走。
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head: 
#             return None # 如果head（头结点）是空，那就说明这个链表都是空的了
#         prev, cur = head, head.next # prev为当前节点，next为下一个节点
#         while cur: #只要下一个节点不是空的，进入循环
#             if cur.val == prev.val: # 如果下一个节点的元素值和当前节点的元素值相同
#                 prev.next == cur.next # 当前节点的下一个节点的值，等于下一个节点的下一个节点的值（相当于做了排除重复元素的工作）
#             else:
#                 prev = cur # 如果不等的话，就把当前的节点，挪到下一个位置去；且，不改变这俩的元素值
#             cur = cur.next # 判断完，再挪动cur所指向的节点位置。（如果改变了元素值，即有重复
#         return head # 【注意】prev和cur虽然只是head和head.next，但还是会改变链表head的节点连接情况的

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# way 2:由于是排了序的list，故可以用set
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        val_set = set()
        val_set.add(head.val) # 先把head的元素值加进set
        root = ListNode(0) # 定义一个头结点
        root.next = head
        while head and head.next: # 只要当前的不是空，且当前的下一个也不是空
            if head.next.val in val_set: # 如果当前的下一个在set里，（其实第一个就是说明下一个与第一个一样了）
                head.next = head.next.next # 把head的下一个指向下一个的下一个
            else:
                head = head.next # 把head指向下一个，其实也就是往右移动
                val_set.add(head.val) # 再把移动后的元素值，加入set里
        return root.next # 其实是调过了虚拟的头结点ListNode(0)。【注意】在链表里面，root.next = head，其实就是和head共享一个指针，数字那些存储的地方都是一样的。

# @lc code=end

