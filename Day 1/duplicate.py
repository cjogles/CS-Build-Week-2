# Understand:
#     I have an array of ints called nums
#     return true if any ints are duplicates, false otherwise
# Plan:
#     iterate through each number
#     for each number in nums, check if that num is a duplicate
#     if so, return True
#     after doing so and you haven't returned true the whole time, then return false
# Execute:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
