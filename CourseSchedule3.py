class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        if len(courses) == 0:
            return 0

        # sort courses by their deadline
        courses.sort(key=operator.itemgetter(1))

        numOfCoursesCanBeFinished = 0
        daysPassed = 0
        maxHeap = []
        heapify(maxHeap)

        for i in range(len(courses)):
            # As the heap is a max heap (not min heap),
            # change the absolute value so that it woks as a min heap
            heappush(maxHeap, -1 * courses[i][0])
            daysPassed += courses[i][0]
            numOfCoursesCanBeFinished += 1

            # If daysPassed exceeds the deadline, reduce the numOfCoursesCanBeFinished and dayPassed
            # which means giving up to take this course and trying next course
            if daysPassed > courses[i][1]:
                # same as -= courses[i][0]
                daysPassed += heappop(maxHeap)
                numOfCoursesCanBeFinished -= 1

        return numOfCoursesCanBeFinished
