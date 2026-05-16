from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = defaultdict(int)
        # do a bucket sort with the index -> freq and val -> n
        # size of # of buckets = len(nums)
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        for n, c in count.items():
            buckets[c].append(n)

        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                res.append(number)
                if len(res) == k:
                    return res