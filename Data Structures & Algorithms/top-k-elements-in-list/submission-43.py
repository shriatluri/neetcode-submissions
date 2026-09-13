class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort, list of groups that store the numbers that happen i times
        # return in reverse order
        count = Counter(nums) # num: freq, 5 : 2
        freq = [[] for i in range(len(nums) + 1)] # 0 to n

        for num, times in count.items():
            freq[times].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                if len(res) == k:
                    break
                res.append(num)
        return res
    