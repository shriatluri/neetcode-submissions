class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)

        for i in range(len(numbers)):
            two_sum = numbers[l - 1] + numbers[r - 1]
            if two_sum > target:
                r -= 1
            elif two_sum < target:
                l += 1
            else:
                return [l, r]
            