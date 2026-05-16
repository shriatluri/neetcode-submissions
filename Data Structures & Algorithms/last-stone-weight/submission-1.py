import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            new = stone1 - stone2
            if new != 0:
                heapq.heappush(max_heap, -new)



        return -max_heap[0] if max_heap else 0
       


        