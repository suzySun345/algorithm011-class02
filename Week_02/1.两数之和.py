#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        dic1 = {}
        for i in range(length):
            j = dic1.get(target-nums[i],-1)
            if not j == -1:
                return [j,i]
            dic1[nums[i]] = i

            
            
# @lc code=end

