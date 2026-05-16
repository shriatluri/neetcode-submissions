class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # use a stack for new fleets and start with the closest ones
        cars = sorted(zip(position, speed), reverse = True)

        # use this for new fleets
        stack = []

        for pos, spd in cars:
            hour = (target - pos) / spd
            if not stack or hour > stack[-1]:
                stack.append(hour)
        return len(stack)

