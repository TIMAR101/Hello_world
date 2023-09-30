class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """ sums = []
        for i, row in enumerate(mat):
            sums.append([sum(row), i])
            sorted_sums = sorted(sums)
            k_rows = sorted_sums[:k]

        print(sums)
        print(sorted_sums)
        print(k_rows)"""

        sums = []

        for item in accounts:
            itemsum = sum(item)
            sums.append(itemsum)

        return max(sums)

class Solution1:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(acc) for acc in accounts])

class Solution2:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
