#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[j] != nums[i]:
                if(i-j)>1:
                    nums[j+1], nums[i] = nums[i], nums[j+1]
                j = j+1
        
        return j+1
# @lc code=end

