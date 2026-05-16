from collections import Counter
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_of_dups = Counter(nums)
        res = []
        new_list = [[] for i in range(len(nums) + 1)]

        for num, count in num_of_dups.items():
            new_list[count].append(num)
        
        for i in range(len(new_list) - 1, 0, -1):
            for num in new_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res


        
        