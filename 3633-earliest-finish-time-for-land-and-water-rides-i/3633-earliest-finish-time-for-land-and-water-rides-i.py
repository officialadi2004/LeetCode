class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')

        for i in range(len(landStartTime)):
            land_end = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_end = max(land_end, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, water_end)

                water_first_end = waterStartTime[j] + waterDuration[j]
                land_end2 = max(water_first_end, landStartTime[i]) + landDuration[i]
                ans = min(ans, land_end2)

        return ans