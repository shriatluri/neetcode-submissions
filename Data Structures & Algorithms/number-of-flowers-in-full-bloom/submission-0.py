class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        peopleSorted = sorted((j, i) for i, j in enumerate(people))

        result = [0] * len(people)
        count = 0

        start = [flower[0] for flower in flowers]
        end = [flower[1] for flower in flowers]
        heapq.heapify(start)
        heapq.heapify(end)

        for time, index in peopleSorted:
            while start and start[0] <= time:
                heapq.heappop(start)
                count += 1

            while end and end[0] < time:
                heapq.heappop(end)
                count -= 1
            result[index] = count
        
        return result
                        
        
