class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter = {}
        for self in magazine:
            if self in letter:
                letter[self] += 1
            else:
                letter[self] = 1
        for self in ransomNote:
            if self not in letter or letter[self] == 0:
                return False
            letter[self] -= 1
        return True 