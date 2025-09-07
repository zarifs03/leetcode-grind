class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_dict = {}

        for char in magazine:
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
        
        for char in ransomNote:
            if char in letter_dict and letter_dict[char] > 0:
                letter_dict[char] -= 1
            else:
                return False
        
        return True
    
# Time complexity: O(m + n)
# space complexity: O(k)

    