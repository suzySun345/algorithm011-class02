#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = {}
        for each_str in strs:
            key = tuple(sorted(each_str))
            dicts[key] = dicts.get(key,[]) + [each_str]
        return dicts.values()
# @lc code=end

