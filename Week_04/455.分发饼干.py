#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        cookie = 0
        child = 0
        while cookie<len(s) and child<len(g):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child
        
# @lc code=end

