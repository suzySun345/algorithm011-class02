#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        result = []
        target = set()
        for i in range(length-2):
            for j in range(i+1,length-1):
                for k in range(i+2,length):
                    if nums[i]+nums[j]+nums[k] == 0:
                        if not -nums[i] in target:
                            target.add(-nums[i])
                            res = [nums[i], nums[j], nums[k]]
                            result.append(res)
        return result
# @lc code=end

