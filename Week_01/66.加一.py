#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
        else:
            digits[-1] = digits[-1] + 1

        return digits


# @lc code=end

