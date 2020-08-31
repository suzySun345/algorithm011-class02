class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        s =  min(left_depth,right_depth)
        l =  max(left_depth,right_depth)
        return 1+(s or l)