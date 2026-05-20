class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            # store value and its index
            complement = target - nums[i]
            if complement in nums_dict:
                if i != nums_dict[complement]:
                    return [nums_dict[complement], i]
            # add to dict after checking complement so duplicates arent skipped.
            nums_dict[nums[i]] = i