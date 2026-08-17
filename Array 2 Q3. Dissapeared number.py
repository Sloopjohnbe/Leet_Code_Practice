"""Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        seen = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in seen]



    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        return [i + 1 for i, val in enumerate(nums) if val > 0]

    
Output = Solution()
print(Output.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(Output.findDisappearedNumbers2([4,3,2,7,8,2,3,1]))