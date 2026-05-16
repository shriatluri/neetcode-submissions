class MedianFinder:
    def __init__(self):
        # small and large heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # push to the max heap and only swap if needed
        # Python defaults to a min heap so we append the negative num for a max
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        # move if needed, over 1 differnece, always keeps in check
        if len(self.small) > len(self.large) + 1:
            # turn back into positive number
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * (self.small[0])
        elif len(self.small) < len(self.large):
            return self.large[0]
        # even in both
        return (-1 * self.small[0] + self.large[0]) / 2.0
        