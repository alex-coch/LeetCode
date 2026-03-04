from heapq import heappush, heappop, heappushpop

class MedianFinder:

    def __init__(self):
        self.min_heap = []  # Stores larger half of numbers
        self.max_heap = []  # Stores smaller half of numbers (negated for max heap behavior)

    def addNum(self, num: int) -> None:
        # Add to max_heap first, then move its maximum to min_heap
        # This ensures all elements in max_heap are <= all elements in min_heap
        heappush(self.min_heap, -heappushpop(self.max_heap, -num))

        # Balance the heaps: min_heap can have at most 1 more element than max_heap
        if len(self.min_heap) - len(self.max_heap) > 1:
            # Move smallest element from min_heap to max_heap
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        # If both heaps have equal size, median is average of both tops
        if len(self.min_heap) == len(self.max_heap):
            # min_heap[0] is smallest of larger half
            # -max_heap[0] is largest of smaller half
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        # If unequal size, min_heap has one extra element which is the median
        return float(self.min_heap[0])
