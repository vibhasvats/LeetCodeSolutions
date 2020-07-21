class Solution:
    def validMountainArray(self, A: [int]) -> bool:
        if len(A) < 3: return False
        max_val = max(A)
        index = A.index(max_val)
        if index == len(A) -1 or index == 0: return False
        for i in range(1, len(A)):
            if i <= index:
                if not A[i] > A[i-1]: return False
            elif i > index:
                if not A[i] < A[i-1]: return False
        return True

# Solution from leetcode
class SolutionF1:
    def validMountainArray(self, A: [int]) -> bool:
        if len(A) < 3:
            return False

        right = 0
        left = 9999

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                continue
            else:
                right = i - 1
                break

        for i in range(len(A) - 1, 0, -1):
            if A[i] < A[i - 1]:
                continue
            else:
                left = i
                break

        return right == left

#Solution from leetcode (A different method)
class SolutionF2:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        increasing = True

        if A[0] > A[1]:
            return False

        for i in range(1, len(A)):
            if increasing:
                if A[i] < A[i - 1]:
                    increasing = False
            else:
                if A[i] >= A[i - 1]:
                    return False
        return not increasing

# solution from leetcode
class SolutionF3:
    def validMountainArray(self, A: [int]) -> bool:

        if not A or len(A) < 3:
            return False

        l = 0
        r = len(A) - 1

        while l < r and A[l] < A[l + 1]:
            l += 1

        if l == 0 or l == r:
            return False

        while l < r and A[r] < A[r - 1]:
            r -= 1

        return l == r