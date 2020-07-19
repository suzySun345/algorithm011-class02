#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10 and five:
                ten += 1
                five -= 1
            elif bill == 20 and five and ten:
                ten -= 1
                five -= 1
            elif bill == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True
        
# @lc code=end

