#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        j = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                if i != j:
                    nums[j],nums[i] = nums[i],nums[j]
                j = j + 1
# @lc code=end

