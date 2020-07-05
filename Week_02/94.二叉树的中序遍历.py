#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = []
        results = []
        while root or len(q) > 0 :
            if root :
                q.append(root)
                root =root.left
            else:
                n = q.pop()
                results.append(n.val)
                if n.right:
                    root = n.right
        return results
# @lc code=end

