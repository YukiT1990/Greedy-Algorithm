class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # It is impossible to travel if sum(cost) is bigger than sum(gas)
        # as the initial gas is 0.
        if (sum(gas) - sum(cost) < 0):
            return -1

        gasTank = 0
        start = 0

        # As there are only one solution,
        # simply remove the case in which the gas tank will be below 0.
        for i in range(len(cost)):
            # immediately before arriving the next gas stop
            gasTank += gas[i] - cost[i]

            if gasTank < 0:
                start = i + 1
                gasTank = 0

        return start
