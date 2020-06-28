#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        print(nums)
# @lc code=end

