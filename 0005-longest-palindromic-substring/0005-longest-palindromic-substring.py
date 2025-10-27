class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(string):
            n = len(string)
            l = 0
            r = n - 1

            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if isPalindrome(substring) and len(substring) > len(longest):
                    longest = substring
        return longest
