#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object): # 用栈
    def isValid(self, s):
        stack = [] # 初始化栈

        for item in s:
            #如果是左括号，往栈里加对应的东西
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            # 如果是右括号了话
            elif not stack or stack[-1] != item: # 如果stack是空的，或者，stack最后一个括号跟当前的右括号不一样，那就有问题
                return False
            else:# 如果stack最后一个括号跟当前括号一样，那就把这个stack里最后一个右括号pop掉
                stack.pop()
        
        if not stack: # 如果遍历完这个括号字符串了，stack也是空的
            return True
        else: # 如果栈里还有，那就说明有问题
            return False
# @lc code=end

