class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     def isPalindrome(string):
    #         n = len(string)
    #         l = 0
    #         r = n - 1

    #         while l <= r:
    #             if string[l] != string[r]:
    #                 return False
    #             l += 1
    #             r -= 1
    #         return True

    #     longest = ""
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             substring = s[i:j]
    #             if isPalindrome(substring) and len(substring) > len(longest):
    #                 longest = substring
    #     return longest
    def longestPalindrome(self, s: str) -> str:
        # Helper function to expand around center
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring
            return s[left + 1:right]
        
        longest = ""
        
        for i in range(len(s)):
            # Odd-length palindromes: expand around the center `i`
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            # Even-length palindromes: expand around the center `i, i+1`
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest
