class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value -> index

        for i, num in enumerate(nums):
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i

# Time complexity: O(n)
# Space complexity: O(n)

        # O(n^2) solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []