class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskLength = len(tasks)
        if n == 0:
            return taskLength

        # create dictionary which key is the kind of task, the value is number of the tasks
        taskCounts = defaultdict(int)
        for task in tasks:
            taskCounts[task] += 1

        countsList = taskCounts.values()
        countsList = list(countsList)

        # get the number of tasks of the most frequent tasks
        maxCount = max(countsList)
        # get the number of tasks which has the maximum appearance
        numberOfMaxCountTasks = countsList.count(maxCount)

        cpuUnits = taskLength
        # tasks which counts are not the max one can be insearted into the interval
        if numberOfMaxCountTasks <= n:
            cpuUnits = (n + 1) * (maxCount - 1) + numberOfMaxCountTasks
        # If the number of tasks which counts are not the max one is bigger than the interval
        # of the max number tasks, taskLength will be longer than cpuUnits calculated above.
        return max(taskLength, cpuUnits)
