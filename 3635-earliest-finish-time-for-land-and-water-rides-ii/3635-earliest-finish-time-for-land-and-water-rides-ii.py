class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):

        def prepare(starts, durations):
            rides = sorted(zip(starts, durations))
            starts = [x[0] for x in rides]
            n = len(rides)

            prefix = [0] * n
            suffix = [0] * n

            prefix[0] = rides[0][1]
            for i in range(1, n):
                prefix[i] = min(prefix[i - 1], rides[i][1])

            suffix[n - 1] = rides[n - 1][0] + rides[n - 1][1]
            for i in range(n - 2, -1, -1):
                suffix[i] = min(
                    suffix[i + 1],
                    rides[i][0] + rides[i][1]
                )

            return starts, prefix, suffix

        def best_finish(finish, data):
            starts, prefix, suffix = data
            left, right = 0, len(starts)

            # Find the first ride opening strictly after finish
            while left < right:
                mid = (left + right) // 2
                if starts[mid] <= finish:
                    left = mid + 1
                else:
                    right = mid

            ans = float('inf')

            # Rides already open: finish + minimum duration
            if left > 0:
                ans = min(ans, finish + prefix[left - 1])

            # Rides opening later: opening time + duration
            if left < len(starts):
                ans = min(ans, suffix[left])

            return ans

        land = prepare(landStartTime, landDuration)
        water = prepare(waterStartTime, waterDuration)

        ans = float('inf')

        for start, duration in zip(landStartTime, landDuration):
            ans = min(ans, best_finish(start + duration, water))

        for start, duration in zip(waterStartTime, waterDuration):
            ans = min(ans, best_finish(start + duration, land))

        return ans