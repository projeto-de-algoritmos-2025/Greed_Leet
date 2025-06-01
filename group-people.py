# 1282. Group the People Given the Group Size They Belong To
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
import math
from collections import defaultdict

class Solution:
    def groupThePeople(self, group_sizes: list[int]) -> list[list[int]]:
        group_count = 0
        group_target = 0
        group_idx = -1
        dick = defaultdict(list)
        groups = []

        for person_id, group_size in enumerate(group_sizes):
            dick[group_size].append(person_id)


        for group_size, people in dick.items():
            for person_id in people:
                if group_count == group_target:
                    group_target = group_size
                    group_count = 0
                    group_idx += 1
                    groups.append([])
                groups[group_idx].append(person_id)
                group_count += 1

        return groups