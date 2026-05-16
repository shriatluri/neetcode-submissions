class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n log n approach
        num_freq = {}
        for n in nums:
            num_freq[n] = 1 + num_freq.get(n, 0)

        arr = []
        for num, cnt in num_freq.items():
            arr.append([cnt,num])
        arr.sort(reverse = True)

        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res