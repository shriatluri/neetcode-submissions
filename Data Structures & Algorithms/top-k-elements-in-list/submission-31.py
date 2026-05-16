class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        # sort by value
        sorted_freq = sorted(freq.items(), key = lambda x: x[1])

        for i in range(k, 0, -1):
            output.append(sorted_freq[-i][0])
        return output