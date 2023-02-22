#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): # 栈。因为后面的元素是相等的，所以使用栈把相等元素都弹出来，那么不等元素就是所求。
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stack1, stack2 = [], []
        while headA: # 如果链表a(headA是头结点）不是空的
            stack1.append(headA) # 把headA（它是个节点!带值也带索引！）append到stack1里，stack 1 be like：[<__main__.ListNode object at 0x000002523F23E140>, <__main__.ListNode object at 0x000002523F23CBE0>]，存的是一串对象哈
            headA = headA.next
        while headB:
            stack2.append(headB)
            headB = headB.next
        pre = None # 定义一个空的存储位置
        while stack1 and stack2: # 下面对栈处理就好了
            s1 = stack1.pop() # 取stack1最后一个节点（对象）
            s2 = stack2.pop() # 取stack2最后一个节点（对象）
            if s1 != s2: # 如果这俩节点不等
                return pre # 那就返回上一个节点（用pre记录下来的）
            else:
                pre = s1 # 用pre来记录前一个节点，其实随便s1还是s2，都一样
        return pre # 都找完了，没返回，那就说明俩stack一样的，那就返回
#【注意】list.pop()，不取返回值，就不返回，list会被更改；如果取了返回值，返回的值就是pop掉的，list也会被更改。

        
# @lc code=end

