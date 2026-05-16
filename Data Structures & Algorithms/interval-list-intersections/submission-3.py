class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        result = []

        for element in firstList:
            firstStart = element[0]
            firstEnd = element[1]

            for element2 in secondList:
                secondStart = element2[0]
                secondEnd = element2[1]

                if max(firstStart, secondStart) <= min(firstEnd, secondEnd):
                    result.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])
        
        return result



