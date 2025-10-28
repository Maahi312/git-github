class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        row = [''] * numRows
        curr = 0
        next = False
        for char in s:
            row[curr] += char
            if curr == 0 or curr == numRows - 1:
                next = not next
            curr += 1 if next else -1
        return ''.join(row)