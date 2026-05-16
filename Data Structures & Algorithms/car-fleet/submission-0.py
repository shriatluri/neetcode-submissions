class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # perfect use case of the zip function
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort(reverse = True)

        fleets = 0
        current_fleet_time = 0.0

        # itterate over the cars starting from the one closest to the target
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if time_to_target > current_fleet_time:
                current_fleet_time = time_to_target
                fleets += 1
        return fleets

