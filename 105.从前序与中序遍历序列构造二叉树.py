#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class TreeNode(object): # 构建二叉树节点
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder): # 递归
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder: # 如果前序遍历与中序遍历为空
            return None
        root = TreeNode(preorder[0]) # 定义以根节点的节点
        index = inorder.index(preorder[0]) # 返回根节点在中序遍历中的索引位置
        root.left = self.buildTree(preorder[1:index+1], inorder[:index]) # 递归，调用buildtree，把1到index+1的前序遍历作为根节点的左子树的前序遍历；把index之前的中序遍历作为根节点的左子树的中序遍历
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:]) # 递归，调用buildtree，同上，构造右子树
        return root


        
# @lc code=end

