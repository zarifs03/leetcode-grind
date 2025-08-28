class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(acc) for acc in accounts])
    
# Time complexity: O(m x n)
# Space complexity: O(1)