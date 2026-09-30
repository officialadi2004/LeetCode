class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        initial = 0
        spent = 0

        for actual, minimum in tasks:
            initial = max(initial, spent + minimum)
            spent += actual

        return initial