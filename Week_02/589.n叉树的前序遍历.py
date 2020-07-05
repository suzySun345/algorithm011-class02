#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        q = [root]
        if root != None:
            while q:
                node = q.pop()
                res.append(node.val)
                q += [child for child in node.children[::-1] if child]
        return res
# @lc code=end

