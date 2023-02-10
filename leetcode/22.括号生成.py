#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object): # 回溯法
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '') # 开始回溯
        return res
    
    def dfs(self, res, left, right, path): # 回溯
        if left == 0 and right == 0:
            res.append(path) # 把当前的可能情况append到res里
            return
        if left > 0:  # 如果左括号数大于0，那说明还能生成左括号
            self.dfs(res, left-1, right, path + '(') # 继续回溯，将(加入path中
        if left < right: # 如果剩余要生成的右括号数大于左括号数，才能生成右括号
            self.dfs(res, left, right - 1, path + ')')
# @lc code=end

