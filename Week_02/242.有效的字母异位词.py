#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for each in s:
            dic1[each] = dic1.get(each,0)+1
        for each in t:
            dic2[each] = dic2.get(each,0)+1
        if dic1 == dic2:
            return True
        else:
            return False
# @lc code=end

