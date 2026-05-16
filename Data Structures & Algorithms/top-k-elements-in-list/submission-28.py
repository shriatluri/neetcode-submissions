from collections import Counter
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dup_dict = Counter(nums)

        ordered_list = [[] for _ in range(len(nums) + 1)]

        for key, value in dup_dict.items():
            ordered_list[value].append(key)
        
        res = []
        for i in range(len(ordered_list) - 1, 0, -1):
            for num in ordered_list[i]:
                res.append(num)

                if len(res) == k:
                    return res
        
        return res

        



        



        
        