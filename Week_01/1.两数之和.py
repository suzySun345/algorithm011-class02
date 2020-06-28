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
        hashmap={}
        
        for i,num in enumerate(nums):
            hashmap[num] = i
        for i,num in enumerate(nums):
            j = hashmap.get(target - num, -1)
            if j != -1 and i!=j:
                return [i,j]


            
            
# @lc code=end

