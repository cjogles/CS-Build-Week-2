# Understanding:
#     - I have an array of ints.
#     - return two indices that are addresses to the two ints that add up to the input target.
#     - assume each input would have EXACTLY one solution.
#     - you may not use the same element twice.
# Planning:
#     - iterate through the array
#     - for each number in array, iterate one more time through the list starting at the index above the one your at in the first loop
#     - if the iterable in the first loop is greater then the target, skip that one.
#     - if the iterable in the first loop is less then, check each value in the second loop. if the second interable is greater then the target,
#     - skip it, otherwise, add the second iterable to the first iterable and see if it adds up to target, if it does, return those two indices.
#     - I think this way you will find the indices that add up the elements to the input target.
# Execution:
#     - see twoSum below
# Reflection:
#     - At first I wrongly assumed that all the ints in my array nums were positive.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # this solution only works with positive numbers
        # for i in range(len(nums)):
        #     if nums[i] > target:
        #         continue
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] > target:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

jackson = Solution()
jackson.twoSum(, )