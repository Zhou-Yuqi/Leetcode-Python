#
# @lc app=leetcode.cn id=71 lang=python
#
# [71] 简化路径
#

# @lc code=start
class Solution(object): # 用栈
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = list() # 初始化目录的路径词list
        dirs = path.split('/')
        for dir in dirs:
            if not dir or dir =='.': # 如果dir是空的，或者dir为.
                continue # 跳出此次for循环
            if dir == '..':
                if stack: # 如果stack不是空的
                    stack.pop() # 返回上级目录
            else: # 排除了特殊..情况后，就可以把当前这个路径词dir append到stack里了
                stack.append(dir)
        return '/' + '/'.join(stack) # 用/拼接路径词并返回
# @lc code=end

