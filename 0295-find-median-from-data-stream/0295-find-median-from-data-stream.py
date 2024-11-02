import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []  
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # Ensure the max element of small is not greater than the min element of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the sizes of the two heaps if necessary
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]  # Convert back to positive
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2


# Example usage:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
