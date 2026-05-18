class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ints: List[int] = []
        for n in operations:
            if n == "+":
                ints.append(ints[-1] + ints[-2])
            elif n == "D":
                ints.append(ints[-1] * 2)
            elif n == "C":
                ints.pop()
            else:
                ints.append(int(n))
        return sum(ints)
            