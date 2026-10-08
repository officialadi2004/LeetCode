class Solution:
    def canReach(self, arr, start):
        stack = [start]

        while stack:
            i = stack.pop()

            if arr[i] == 0:
                return True

            if arr[i] < 0:
                continue

            jump = arr[i]
            arr[i] = -1

            if i + jump < len(arr):
                stack.append(i + jump)

            if i - jump >= 0:
                stack.append(i - jump)

        return False