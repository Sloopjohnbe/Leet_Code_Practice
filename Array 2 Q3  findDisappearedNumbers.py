"""Array 2 Q3 findDisappearedNumbers

Given an array nums of n integers where nums[i] is in the range [1,n], return an array of all the integer in the range [1,n] that do not appear in nums.

Ex
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
"""

#7980ms
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output =[]
        n = len(nums)   
        for i in range(1, n + 1):
            if i not in nums:
                output.append(i)
        return(output)

Output = Solution()
print(Output.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

