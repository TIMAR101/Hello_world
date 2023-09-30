class Solution:
    def kWeakestRows(self, mat, k):

        Sold = {}
        FinList = []

        for num, item in enumerate(mat):

            Sold[num] = sum(item)
            # Sold[sum(item)] = num


        for __ in range(k):

            minrow= min(Sold.values())

            for k, v in Sold.items():
                if v == minrow:
                    FinList.append(k)
                    Sold.pop(k)
                    break



        return FinList
class Solution1:
    def kWeakestRows(self, mat, k: int):
        sums = []
        for i, row in enumerate(mat):
            sums.append([sum(row), i])
            sorted_sums = sorted(sums)
            k_rows = sorted_sums[:k]

        print(sums)
        print(sorted_sums)
        print(k_rows)

        res = []
        for val in k_rows:
            res.append(val[1])
        return res
S1 = Solution1()

print(S1.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))



