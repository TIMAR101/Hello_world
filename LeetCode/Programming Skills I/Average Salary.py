def average(salary) -> float:

        result = (sum(salary) - min(salary) - max(salary)) / (len(salary)-2)

        return result

print(average([4000,3000,1000,2000]))

l = []

minimum = float("inf")
maximum = float("-inf")

print(minimum)
