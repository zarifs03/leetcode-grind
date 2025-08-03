class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value -> index

        for i, num in enumerate(nums):
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
                