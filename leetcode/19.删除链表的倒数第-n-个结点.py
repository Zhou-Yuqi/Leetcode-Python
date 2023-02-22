#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object): # 双指针
    # 具体到解法，这个题肯定是使用快慢指针啊，
    # 两个之间的距离是n，所以当快指针指向结尾的时候，慢指针正好指向了倒数第n个。
    # 因为要删除慢指针的位置，所以需要一个pre指针记录一下前面的那个节点的位置。
    
    # 由于有可能删除首节点，所以使用哑结点当做新的头可以解决。
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0) # 哑结点
        root.next = head # 哑结点的next，才去接head
        fast, slow, pre = root, root, root
        while n - 1: # 只有n=0的时候，才不满足
            fast = fast.next # 快指针往右
            n -= 1
        while fast.next: # 当fast指向最后一个位置的时候，就会终止了
            # 全都往后移动
            fast = fast.next 
            pre = slow
            slow = slow.next
        pre.next = slow.next
        return root.next

# 将链表转换成字符串
def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

# 列表转成链表
def stringToListNode(input):
    numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)# 分别将列表中每个数转换成节点
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

# @lc code=end

