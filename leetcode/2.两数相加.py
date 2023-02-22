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
class Solution(object):# 递归
    def addTwoNumbers(self, l1, l2):
        # 如果l1和l2有一个为空，则返回另一个
        if not l1:
            return l2
        if not l2:
            return l1

        # 如果都不为空
        add = l1.val + l2.val # 把两个链表节点的值相加
        res = ListNode(add % 10) # 把 add 模 10 作为当前的链表节点的值
        res.next = self.addTwoNumbers(l1.next, l2.next) # 把两个链表的 next 节点相加
        if add >= 10: # 如果当前相加的结果 add>=10
            res.next = self.addTwoNumbers(res.next, ListNode(1)) # 需要把 next 节点相加得到的结果 + 1
        return res


# def print_linked_list(head):
#     if not head or not head.next:
#         return []
#     result = []    
#     while head:
#         result.insert(0, head.val)
#         head = head.next
#     return result

def stringToListNode(input):
    numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)# 分别将列表中每个数转换成节点
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

s = Solution()
l1 = stringToListNode([2,4,3])
l2 = stringToListNode([5,6,4])
re = s.addTwoNumbers(l1, l2)

# 将链表转换成字符串
def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

re_2 = listNodeToString(re)
print('re_2:', re_2)
# @lc code=end

