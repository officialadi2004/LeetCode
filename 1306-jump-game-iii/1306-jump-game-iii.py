class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        visited = [False] * n
        stack = [start]

        while stack:
            i = stack.pop()

            if visited[i]:
                continue

            visited[i] = True

            if arr[i] == 0:
                return True

            jump = arr[i]

            if i + jump < n:
                stack.append(i + jump)

            if i - jump >= 0:
                stack.append(i - jump)

        return False