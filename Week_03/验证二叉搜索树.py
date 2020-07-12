class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.helper(root,res)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True
    
    def helper(self,root,res):

        if root:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)