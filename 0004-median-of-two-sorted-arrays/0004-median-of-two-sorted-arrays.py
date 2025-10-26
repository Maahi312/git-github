class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B): A, B = B, A
        m, n = len(A), len(B)
        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i
            leftA = A[i-1] if i > 0 else float('-inf')
            rightA = A[i] if i < m else float('inf')
            leftB = B[j-1] if j > 0 else float('-inf')
            rightB = B[j] if j < n else float('inf')
            if leftA <= rightB and leftB <= rightA:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2 if (m + n) % 2 == 0 else max(leftA, leftB)
            elif leftA > rightB: r = i - 1
            else: l = i + 1
