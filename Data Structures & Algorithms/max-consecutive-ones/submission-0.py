class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        maximum = 0
        for n in nums:
            if n == 1:
                consec += 1
            else:
                maximum = max(maximum, consec)
                consec = 0
        return max(maximum, consec)
