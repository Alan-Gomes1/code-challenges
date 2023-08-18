from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float('-inf')
        window_sum = start = 0

        for end in range(len(nums)):
            window_sum += nums[end]
            if end - start + 1 == k:
                max_average = max(max_average, float(window_sum) / float(k))
                window_sum -= nums[start]
                start += 1

        return max_average
