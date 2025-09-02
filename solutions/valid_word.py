class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'
        vowels += vowels.upper()
        consonants = 'bcdfghjklmnpqrstvwxyz'
        consonants += consonants.upper()
        digits = '0123456789'

        allowed = vowels + consonants + digits

        has_vowel = False
        has_consonant = False

        if len(word) < 3:
            return False

        for c in word:
            if c in vowels: has_vowel = True
            if c in consonants: has_consonant = True
            if c not in allowed:
                return False
        
        return has_vowel and has_consonant
