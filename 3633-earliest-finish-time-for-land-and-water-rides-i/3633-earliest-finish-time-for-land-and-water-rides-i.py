class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        land_first = min(
            max(s + d, ws) + wd
            for s, d in zip(landStartTime, landDuration)
            for ws, wd in zip(waterStartTime, waterDuration)
        )

        water_first = min(
            max(ws + wd, s) + d
            for ws, wd in zip(waterStartTime, waterDuration)
            for s, d in zip(landStartTime, landDuration)
        )

        return min(land_first, water_first)