class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # define sort condition
        # the one the difference of elem[0] - elem[1] is the smallest(the biggest minus number) comes first
        def returnDifferenece(elem):
            return elem[0] - elem[1]
        costs.sort(key=returnDifferenece)

        # add up the first element in the first half and
        # the second element in the second half
        minimumCost = 0
        n = len(costs)//2
        firstSum = sum(costs[i][0] for i in range(n))
        secondSum = sum(costs[i][1] for i in range(n,len(costs)))
        minimumCost = firstSum + secondSum
        return minimumCost
