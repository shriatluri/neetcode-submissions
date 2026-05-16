class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        result = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            startA, endA = firstList[i]
            startB, endB = secondList[j]

            if max(startA, startB) <= min(endA, endB):
                result.append([max(startA, startB), min(endA, endB)])
            
            if endA < endB:
                i += 1
            else:
                j += 1
        
        return result



