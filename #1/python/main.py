class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        used_nums = []
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in used_nums:
                return [used_nums.index(complement), i]
            used_nums.append(nums[i])
        return []
