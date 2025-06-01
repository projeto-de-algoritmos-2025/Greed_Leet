# 2551. Put Marbles in Bags
# https://leetcode.com/problems/put-marbles-in-bags/description/
import heapq

class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0

        cut_costs_min = []
        cut_costs_max = []
        min_score = 0
        max_score = 0

        for i in range(len(weights) - 1):
            cut_costs_min.append(weights[i] + weights[i + 1])
            cut_costs_max.append(-(weights[i] + weights[i + 1]))

        heapq.heapify(cut_costs_min)
        heapq.heapify(cut_costs_max)

        for i in range(k-1):
            min_score += heapq.heappop(cut_costs_min)
            max_score += heapq.heappop(cut_costs_max) * -1

        return max_score - min_score