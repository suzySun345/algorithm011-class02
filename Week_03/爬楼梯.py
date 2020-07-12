class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: 
            return 1
        p = 0
        q = 1
        r = 1
        for i in range(2,n+1):
            p=q
            q=r
            r=p+q
            
        return b