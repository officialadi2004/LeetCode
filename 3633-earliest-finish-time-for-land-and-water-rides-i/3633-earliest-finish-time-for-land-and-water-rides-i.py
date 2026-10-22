class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        best_land = min(s + d for s, d in zip(landStartTime, landDuration))
        best_water = min(s + d for s, d in zip(waterStartTime, waterDuration))

        land_first = min(
            max(best_land, s) + d
            for s, d in zip(waterStartTime, waterDuration)
        )

        water_first = min(
            max(best_water, s) + d
            for s, d in zip(landStartTime, landDuration)
        )

        return min(land_first, water_first)