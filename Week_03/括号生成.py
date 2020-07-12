class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recury(n,left,right,s,res=[]):
            if left==n and right==n:
                res.append(s)
            if left<n:
                recury(n,left+1, right, s+'(',res)
            if right<left:
                recury(n,left,right+1,s+')',res)
            return res
        return recury(n,0,0,"")