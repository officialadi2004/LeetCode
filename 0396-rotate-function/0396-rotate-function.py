class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)

        total = sum(nums)

        # F(0)
        current = 0
        for i in range(n):
            current += i * nums[i]

        answer = current

        # Calculate F(k) from F(k-1)
        for k in range(1, n):
            current = current + total - n * nums[n - k]
            answer = max(answer, current)

        return answer