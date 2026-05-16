class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        #new frequency array 
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in hashMap.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            

            