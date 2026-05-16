class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count the occurances
        count = {}
        #the value in the count dict
        freq = [[] for i in range(len(nums) + 1)]
        #count the occurances
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            #this value n, occurs c number of times 
            freq[c].append(n)
        
        res = []
        #start at the end and go to 0 in desc order
        for i in range(len(freq) - 1, 0, -1):
            #append lists to result
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
