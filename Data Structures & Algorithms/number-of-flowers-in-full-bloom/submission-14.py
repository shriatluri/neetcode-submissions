class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = sorted((j,i) for i, j in enumerate(people))

        start = [flower[0] for flower in flowers]
        end = [flower[1] for flower in flowers]

        result = [0] * len(people)

        heapq.heapify(start)
        heapq.heapify(end)
        count = 0

        for person in people:
            while start and person[0] >= start[0]:
                count += 1
                heapq.heappop(start)
            
            while end and person[0] > end[0]:
                count -= 1
                heapq.heappop(end)

            result[person[1]] = count

        return result